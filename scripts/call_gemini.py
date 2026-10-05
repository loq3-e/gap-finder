"""
手法/プロンプト.md のプロンプトに学習者データを差し込み、Gemini APIに投げて
出力JSONをスキーマ検証するスクリプト。

事前準備:
    pip install google-genai python-dotenv
    プロジェクト直下に .env ファイルを作成し、以下の1行を書く（.gitignore済み）
        GEMINI_API_KEY=ここにキー
    キーは https://aistudio.google.com/apikey で発行

使い方（1ケースだけ試す）:
    python scripts/call_gemini.py \
        --problem "行列 A=[[1,2],[3,4]]、B=[[0,1],[1,0]] のとき、(AB)^T を求めよ。" \
        --answer "AB = [[2,1],[4,3]]\n(AB)^T = A^T B^T = [[3,1],[4,2]]" \
        --explanation "転置を取るときも、積の順番はそのままでいいと思った。"

使い方（複数ケースをJSONファイルでまとめて実行）:
    python scripts/call_gemini.py --cases-file 手法/m3_cases.json --out 手法/M3実行結果.json

JSONファイルの形式（1ケース分）:
    {
      "case_id": "ケース1",
      "problem": "...",
      "answer": "...",
      "explanation": "..."
    }
の配列。
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT_FILE = ROOT / "手法" / "プロンプト.md"
MODEL = "gemini-3.6-flash"


def load_prompt_prefix() -> str:
    """プロンプト.mdから[入力データ]の直前までを読み込む（テンプレート部分）"""
    text = PROMPT_FILE.read_text(encoding="utf-8")
    marker = "[入力データ]"
    idx = text.index(marker)
    return text[:idx].rstrip()


def load_valid_concept_ids() -> set[str]:
    """プロンプト.md内の概念IDリスト(```json ... ```)からid一覧を取り出す"""
    text = PROMPT_FILE.read_text(encoding="utf-8")
    m = re.search(r"```json\n(.*?)\n```", text, re.S)
    if not m:
        raise RuntimeError("プロンプト.md内に概念IDリストのJSONブロックが見つかりません")
    concepts = json.loads(m.group(1))
    return {c["id"] for c in concepts}


def build_prompt(prefix: str, problem: str, answer: str, explanation: str) -> str:
    input_block = (
        f"[入力データ]\n"
        f"問題文：{problem}\n"
        f"学習者の解答：{answer}\n"
        f"自己説明：{explanation}\n"
    )
    return f"{prefix}\n\n{input_block}"


def call_gemini(client, prompt_text: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=prompt_text)
    return response.text


def validate_output(raw_text: str, valid_ids: set[str]) -> tuple[dict | None, list[str]]:
    errors = []
    text = raw_text.strip()
    # Geminiが ```json ... ``` で包んでくる場合に備えて剥がす
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.S)
    if fence:
        text = fence.group(1)

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return None, [f"JSONパース失敗: {e}"]

    for key in ("a", "b", "c", "d"):
        if key not in data:
            errors.append(f"キー'{key}'が欠落")

    if "c" in data and data["c"] not in ("high", "medium", "low"):
        errors.append(f"cの値が不正: {data.get('c')!r}（high/medium/lowのいずれかであるべき）")

    if "a" in data:
        if not isinstance(data["a"], list):
            errors.append("aがリストではない")
        else:
            for item in data["a"]:
                cid = item.get("id")
                if cid not in valid_ids:
                    errors.append(f"概念IDリスト外の値: {cid!r}")

    return data, errors


def run_one_case(client, prefix: str, valid_ids: set[str], case: dict) -> dict:
    prompt_text = build_prompt(prefix, case["problem"], case["answer"], case["explanation"])
    raw_text = call_gemini(client, prompt_text)
    data, errors = validate_output(raw_text, valid_ids)

    result = {
        "case_id": case.get("case_id", "(unnamed)"),
        "raw_output": raw_text,
        "parsed": data,
        "schema_errors": errors,
    }

    if "expected_concepts" in case:
        predicted_ids = {item["id"] for item in data["a"]} if data and data.get("a") else set()
        expected_ids = set(case["expected_concepts"])
        result["expected_concepts"] = sorted(expected_ids)
        result["predicted_concepts"] = sorted(predicted_ids)
        result["overlap"] = sorted(predicted_ids & expected_ids)
        result["extra_predicted"] = sorted(predicted_ids - expected_ids)
        result["missing_expected"] = sorted(expected_ids - predicted_ids)

    return result


def main():
    parser = argparse.ArgumentParser(description="プロンプト.mdのフローをGemini APIで実行する")
    parser.add_argument("--problem", help="問題文")
    parser.add_argument("--answer", help="学習者の解答")
    parser.add_argument("--explanation", help="自己説明")
    parser.add_argument("--cases-file", type=Path, help="複数ケースをまとめたJSONファイル")
    parser.add_argument("--out", type=Path, help="結果を書き出すJSONファイル（省略時は標準出力のみ）")
    parser.add_argument("--sleep", type=float, default=1.0, help="ケース間の待機秒数（レート制限対策）")
    args = parser.parse_args()

    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
    except ImportError:
        pass

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit(
            "エラー: GEMINI_API_KEY が見つかりません。"
            f"プロジェクト直下に .env ファイルを作成し、GEMINI_API_KEY=... と書いてください（{ROOT / '.env'}）。"
        )

    try:
        from google import genai
    except ImportError:
        sys.exit("エラー: google-genai がインストールされていません。`pip install google-genai` を実行してください。")

    client = genai.Client(api_key=api_key)
    prefix = load_prompt_prefix()
    valid_ids = load_valid_concept_ids()

    if args.cases_file:
        cases = json.loads(args.cases_file.read_text(encoding="utf-8"))
        results = []
        for i, case in enumerate(cases):
            print(f"[{i+1}/{len(cases)}] {case.get('case_id', '?')} を実行中...", file=sys.stderr)
            result = run_one_case(client, prefix, valid_ids, case)
            results.append(result)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            if i < len(cases) - 1:
                time.sleep(args.sleep)

        if args.out:
            args.out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"結果を {args.out} に保存しました。", file=sys.stderr)

    elif args.problem and args.answer and args.explanation:
        case = {"problem": args.problem, "answer": args.answer, "explanation": args.explanation}
        result = run_one_case(client, prefix, valid_ids, case)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    else:
        parser.error("--cases-file か、--problem/--answer/--explanation の組を指定してください。")


if __name__ == "__main__":
    main()
