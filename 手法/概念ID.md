[
  {
    "id": "LA-MAT-01",
    "name": "行列の定義",
    "definition": "行列がm×n個のスカラーを長方形に並べたものであり、成分・行・列・サイズ(m×n)で表されることの理解",
    "prerequisites": [],
    "evidence_patterns": ["成分の添字(a_ij)や行列のサイズ(m×n)を正しく読み取れない"],
    "misconceptions": ["行(row)と列(column)を取り違える"]
  },
  {
    "id": "LA-MAT-02",
    "name": "行列の和・スカラー倍",
    "definition": "同じサイズの行列同士の和、行列のスカラー倍が成分ごとの演算で定義されることの理解",
    "prerequisites": ["LA-MAT-01"],
    "evidence_patterns": ["サイズの異なる行列同士を足そうとする、あるいは和の条件を確認せず計算する"],
    "misconceptions": ["異なるサイズの行列でも和が定義できると思っている"]
  },
  {
    "id": "LA-MAT-03",
    "name": "行列の積",
    "definition": "行列の積ABが、Aの列数とBの行数が一致する場合に定義され、(AB)_ij=Σ a_ik b_kj で計算されることの理解",
    "prerequisites": ["LA-MAT-01"],
    "evidence_patterns": ["積の対応する行と列の内積計算を誤る、または積の可能条件（列数=行数）を確認しない"],
    "misconceptions": ["行列の積が成分ごとの積（アダマール積）だと誤解している", "AB=BAが常に成り立つと思っている"]
  },
  {
    "id": "LA-MAT-04",
    "name": "転置行列",
    "definition": "行列Aの転置A^Tが行と列を入れ替えたものであることの理解、(AB)^T=B^T A^T などの性質",
    "prerequisites": ["LA-MAT-03"],
    "evidence_patterns": ["転置の際に添字の入れ替え(a_ij→a_ji)を誤る"],
    "misconceptions": ["(AB)^T = A^T B^T だと誤解している（正しくはB^T A^T）"]
  },
  {
    "id": "LA-MAT-05",
    "name": "単位行列・零行列",
    "definition": "単位行列Iが積の単位元であること（AI=IA=A）、零行列の性質の理解",
    "prerequisites": ["LA-MAT-03"],
    "evidence_patterns": ["単位行列との積で行列が変化しないことを説明できない"],
    "misconceptions": ["零行列との積が常に零行列にならないと思っている"]
  },
  {
    "id": "LA-MAT-06",
    "name": "対称行列・対角行列",
    "definition": "対称行列(A=A^T)、対角行列などの定義と性質の理解",
    "prerequisites": ["LA-MAT-04"],
    "evidence_patterns": ["対称行列の判定でA=A^Tの確認を行わず見た目だけで判断する"],
    "misconceptions": ["対称行列であれば対角行列でもあると誤解している（対角行列は対称行列の特殊な場合に過ぎない）"]
  },
  {
    "id": "LA-MAT-07",
    "name": "正則行列の定義",
    "definition": "正方行列Aが正則であるとは、AB=BA=Iとなる行列Bが存在することであるという理解",
    "prerequisites": ["LA-MAT-05"],
    "evidence_patterns": ["逆行列が存在することと正則であることの関係を説明できない"],
    "misconceptions": ["正方行列であれば必ず逆行列を持つと思っている"]
  },
  {
    "id": "LA-LEQ-01",
    "name": "連立一次方程式の行列表現",
    "definition": "連立一次方程式をAx=bとして行列・ベクトルで表現できることの理解",
    "prerequisites": ["LA-MAT-03"],
    "evidence_patterns": ["連立方程式をAx=bの形に正しく変換できない"],
    "misconceptions": ["係数行列Aとベクトルbの対応関係を取り違える"]
  },
  {
    "id": "LA-LEQ-02",
    "name": "拡大係数行列",
    "definition": "連立方程式を拡大係数行列[A|b]で表し、行基本変形により解くことの理解",
    "prerequisites": ["LA-LEQ-01"],
    "evidence_patterns": ["拡大係数行列[A|b]の列の対応を誤る"],
    "misconceptions": ["拡大係数行列と係数行列の階数の違いを意識せず解の個数を判断する"]
  },
  {
    "id": "LA-LEQ-03",
    "name": "行基本変形",
    "definition": "行の入れ替え・定数倍・他の行への加算という3種の基本変形が解を変えないことの理解",
    "prerequisites": ["LA-LEQ-02"],
    "evidence_patterns": ["行基本変形の操作（入れ替え・定数倍・加算）以外の変形を行い解が変わってしまう"],
    "misconceptions": ["列に対しても行と同様の基本変形を自由に行ってよいと思っている"]
  },
  {
    "id": "LA-LEQ-04",
    "name": "階段行列・簡約階段形",
    "definition": "行基本変形によって行列を階段形（簡約階段形）に変形できることの理解",
    "prerequisites": ["LA-LEQ-03"],
    "evidence_patterns": ["階段形に変形した結果が正しい形（各行の先頭成分が右にずれていく）になっていない"],
    "misconceptions": ["階段形であれば簡約階段形の条件（主成分の列が他0）も満たすと思っている"]
  },
  {
    "id": "LA-LEQ-05",
    "name": "行列の階数（rank）",
    "definition": "階段形における0でない行の数として階数が定義されることの理解",
    "prerequisites": ["LA-LEQ-04"],
    "evidence_patterns": ["階数と自由変数の個数の関係を説明できない"],
    "misconceptions": ["階数は行の数（方程式の数）と常に一致すると思っている"]
  },
  {
    "id": "LA-LEQ-06",
    "name": "解の存在・一意性の判定",
    "definition": "rank(A)とrank([A|b])の比較により、解なし・一意解・無数の解を判定できることの理解",
    "prerequisites": ["LA-LEQ-05"],
    "evidence_patterns": ["方程式の数と未知数の数だけを見て解の個数を判断し、rankを確認しない"],
    "misconceptions": ["未知数の数=方程式の数なら必ず一意解を持つと思っている"]
  },
  {
    "id": "LA-LEQ-07",
    "name": "同次連立方程式の解空間",
    "definition": "Ax=0の解全体が部分空間をなすことの理解（基本解・自由変数によるパラメータ表示）",
    "prerequisites": ["LA-LEQ-06"],
    "evidence_patterns": ["自由変数によるパラメータ表示ができず、特殊解のみを答えとしてしまう"],
    "misconceptions": ["同次方程式の解は常にゼロベクトルのみだと思っている"]
  },
  {
    "id": "LA-DET-01",
    "name": "2次・3次行列式の定義",
    "definition": "2次・3次正方行列に対するサラスの公式等による行列式の定義の理解",
    "prerequisites": ["LA-MAT-01"],
    "evidence_patterns": ["サラスの公式の符号(+,-)の対応を誤る"],
    "misconceptions": ["行列式を成分の単純な総和だと誤解している"]
  },
  {
    "id": "LA-DET-02",
    "name": "余因子・余因子展開",
    "definition": "余因子と余因子展開によってn次行列式を定義・計算できることの理解",
    "prerequisites": ["LA-DET-01"],
    "evidence_patterns": ["余因子の符号(-1)^{i+j}を取り違える"],
    "misconceptions": ["余因子展開はどの行・列で展開しても符号の付け方が同じだと思い込んでいる"]
  },
  {
    "id": "LA-DET-03",
    "name": "行列式の基本性質（多重線形性・交代性）",
    "definition": "行の入れ替えで符号が変わる、同じ行があれば0になる等の性質の理解",
    "prerequisites": ["LA-DET-02"],
    "evidence_patterns": ["同じ行（列）が2つある行列式が0になる理由を説明できない"],
    "misconceptions": ["行列式が単なる計算手続きであり、性質（交代性など）とは無関係だと思っている"]
  },
  {
    "id": "LA-DET-04",
    "name": "行基本変形と行列式の関係",
    "definition": "行基本変形が行列式に与える影響（定数倍でその分掛かる、行の入替で符号反転、加算で不変）の理解",
    "prerequisites": ["LA-DET-03", "LA-LEQ-03"],
    "evidence_patterns": ["行の定数倍操作をした際に行列式もその分だけ変化することを反映せず計算する"],
    "misconceptions": ["行基本変形をしても行列式の値は常に変わらないと思っている"]
  },
  {
    "id": "LA-DET-05",
    "name": "行列式の積の性質",
    "definition": "det(AB)=det(A)det(B)であることの理解",
    "prerequisites": ["LA-DET-03", "LA-MAT-03"],
    "evidence_patterns": ["det(AB)をdet(A)+det(B)のように誤って計算する"],
    "misconceptions": ["det(A+B)=det(A)+det(B)だと誤解している"]
  },
  {
    "id": "LA-DET-06",
    "name": "行列式と正則性の同値性",
    "definition": "正方行列Aが正則であることと det(A)≠0 であることが同値であるという理解",
    "prerequisites": ["LA-DET-05", "LA-MAT-07"],
    "evidence_patterns": ["det(A-λI)=0 のような式をそのまま適用して計算を進め、なぜdet=0という条件を使うのかを説明できない"],
    "misconceptions": ["det=0という条件を暗記のみで運用し、非正則性との関係を理解していない"]
  },
  {
    "id": "LA-DET-07",
    "name": "クラメルの公式",
    "definition": "正則な係数行列を持つ連立方程式の解を行列式の比で表せることの理解",
    "prerequisites": ["LA-DET-06", "LA-LEQ-01"],
    "evidence_patterns": ["クラメルの公式の分子の行列（列を置き換える対象）を取り違える"],
    "misconceptions": ["クラメルの公式が非正則な（det=0の）連立方程式にも使えると思っている"]
  },
  {
    "id": "LA-INV-01",
    "name": "逆行列の定義",
    "definition": "AA^{-1}=A^{-1}A=Iを満たすA^{-1}が逆行列であることの理解",
    "prerequisites": ["LA-MAT-07"],
    "evidence_patterns": ["AA^{-1}=Iのみ確認しA^{-1}A=Iを確認しない"],
    "misconceptions": ["逆行列は常に存在すると思っている"]
  },
  {
    "id": "LA-INV-02",
    "name": "余因子行列による逆行列の公式",
    "definition": "A^{-1} = (1/det A) adj(A) （余因子行列）で逆行列を求められることの理解",
    "prerequisites": ["LA-DET-06", "LA-DET-02"],
    "evidence_patterns": ["余因子行列の転置(adjugate)を取らずに逆行列を計算する"],
    "misconceptions": ["逆行列の公式でdet(A)で割る操作を忘れる、あるいはdet(A)=0のときも公式が使えると思っている"]
  },
  {
    "id": "LA-INV-03",
    "name": "掃き出し法による逆行列の計算",
    "definition": "[A|I]を行基本変形して[I|A^{-1}]を得る手順の理解",
    "prerequisites": ["LA-INV-01", "LA-LEQ-03"],
    "evidence_patterns": ["[A|I]の変形途中でA側が単位行列にならないのに計算を止めてしまう"],
    "misconceptions": ["掃き出し法の際、左右の行列に異なる行基本変形を適用してもよいと思っている"]
  },
  {
    "id": "LA-INV-04",
    "name": "逆行列の性質（(AB)^{-1}=B^{-1}A^{-1}等）",
    "definition": "逆行列に関する性質、特に積の逆行列の順序が入れ替わることの理解",
    "prerequisites": ["LA-INV-01", "LA-MAT-03"],
    "evidence_patterns": ["(AB)^{-1}を計算する際に順序を保たず A^{-1}B^{-1} としてしまう"],
    "misconceptions": ["(AB)^{-1}=A^{-1}B^{-1}だと誤解している（積の非可換性を考慮していない）"]
  },
  {
    "id": "LA-VS-01",
    "name": "ベクトル空間の公理",
    "definition": "和とスカラー倍について閉じ、8つの公理を満たす集合がベクトル空間であることの理解",
    "prerequisites": [],
    "evidence_patterns": ["公理の一部（結合律や分配律など）を確認せずベクトル空間であると判断する"],
    "misconceptions": ["矢印や座標で表せる幾何ベクトルだけがベクトル空間の元だと思っている"]
  },
  {
    "id": "LA-VS-02",
    "name": "部分空間",
    "definition": "ベクトル空間の部分集合が、和とスカラー倍について閉じていれば部分空間であることの理解",
    "prerequisites": ["LA-VS-01"],
    "evidence_patterns": ["和とスカラー倍について閉じているかを確認せず部分空間だと判断する"],
    "misconceptions": ["原点を含む集合であれば自動的に部分空間だと誤解している"]
  },
  {
    "id": "LA-VS-03",
    "name": "一次結合・生成系（span）",
    "definition": "ベクトルの一次結合、およびベクトル集合が張る部分空間（span）の理解",
    "prerequisites": ["LA-VS-02"],
    "evidence_patterns": ["与えられたベクトルの一次結合でない表現を一次結合だと誤認する"],
    "misconceptions": ["生成系（span）がベクトル空間全体を必ず生成すると思い込んでいる"]
  },
  {
    "id": "LA-VS-04",
    "name": "一次独立・一次従属",
    "definition": "c1v1+...+cnvn=0 が自明解のみを持つとき一次独立であるという理解",
    "prerequisites": ["LA-VS-03", "LA-LEQ-07"],
    "evidence_patterns": ["連立方程式 c1v1+...+cnvn=0 に帰着させず、直感のみで独立性を判断する"],
    "misconceptions": ["ベクトルの本数が空間の次元以下であれば自動的に一次独立だと思っている"]
  },
  {
    "id": "LA-VS-05",
    "name": "基底",
    "definition": "一次独立かつ生成系となるベクトルの組が基底であることの理解",
    "prerequisites": ["LA-VS-04"],
    "evidence_patterns": ["生成系であることは確認するが一次独立性の確認を怠り基底だと判断する"],
    "misconceptions": ["基底は一意に定まる（他の基底は存在しない）と思っている"]
  },
  {
    "id": "LA-VS-06",
    "name": "次元",
    "definition": "基底に含まれるベクトルの個数が空間の次元として一意に定まることの理解",
    "prerequisites": ["LA-VS-05"],
    "evidence_patterns": ["異なる基底から異なる次元の値を算出してしまう"],
    "misconceptions": ["次元はベクトルの成分の個数と常に一致すると思っている"]
  },
  {
    "id": "LA-VS-07",
    "name": "座標（基底に関する成分表示）",
    "definition": "基底を固定したときベクトルが一意な座標（係数の組）で表されることの理解",
    "prerequisites": ["LA-VS-05"],
    "evidence_patterns": ["基底を明示せずに座標（成分表示）を答えてしまう"],
    "misconceptions": ["同じベクトルの座標はどの基底を選んでも変わらないと思っている"]
  },
  {
    "id": "LA-LM-01",
    "name": "線形写像の定義",
    "definition": "f(u+v)=f(u)+f(v), f(cu)=cf(u) を満たす写像が線形写像であることの理解",
    "prerequisites": ["LA-VS-01"],
    "evidence_patterns": ["f(u+v)=f(u)+f(v)とf(cu)=cf(u)の両方を確認せず線形写像だと判断する"],
    "misconceptions": ["原点を通る直線・平面への写像であれば自動的に線形写像だと誤解している"]
  },
  {
    "id": "LA-LM-02",
    "name": "表現行列",
    "definition": "基底を固定すると線形写像が行列で表現できることの理解",
    "prerequisites": ["LA-LM-01", "LA-VS-07"],
    "evidence_patterns": ["基底の取り方を明示せずに表現行列を計算してしまう"],
    "misconceptions": ["表現行列は基底の選び方によらず一意に定まると思っている"]
  },
  {
    "id": "LA-LM-03",
    "name": "核（kernel）",
    "definition": "f(v)=0となるvの集合が部分空間（核）をなすことの理解",
    "prerequisites": ["LA-LM-01", "LA-VS-02"],
    "evidence_patterns": ["核を求める際にf(v)=0を解く連立方程式に帰着させず直感で答える"],
    "misconceptions": ["核はゼロベクトルのみからなると思い込んでいる"]
  },
  {
    "id": "LA-LM-04",
    "name": "像（image）",
    "definition": "写像の像f(V)が部分空間をなすことの理解",
    "prerequisites": ["LA-LM-01", "LA-VS-02"],
    "evidence_patterns": ["像が定義域の部分集合ではなく終域全体を指すと誤認する"],
    "misconceptions": ["像は常に終域全体と一致すると思っている"]
  },
  {
    "id": "LA-LM-05",
    "name": "階数・退化次数の定理（次元定理）",
    "definition": "dim(ker f) + dim(im f) = dim(V) が成り立つことの理解",
    "prerequisites": ["LA-LM-03", "LA-LM-04", "LA-VS-06"],
    "evidence_patterns": ["dim(ker f)とdim(im f)を別々に求めた後、その和がdim(V)になることを確認しない"],
    "misconceptions": ["核が0次元（単射）であれば像も定義域全体を覆うと誤解している"]
  },
  {
    "id": "LA-EIG-01",
    "name": "固有値の定義",
    "definition": "Av=λv を満たすλが固有値であることの理解",
    "prerequisites": ["LA-MAT-03"],
    "evidence_patterns": ["特性方程式の意味を説明できない"],
    "misconceptions": ["固有値を単なる計算結果としてしか捉えていない"]
  },
  {
    "id": "LA-EIG-02",
    "name": "非自明解の存在条件",
    "definition": "(A-λI)v=0 が非自明解を持つ条件がdet=0であることの理解",
    "prerequisites": ["LA-DET-06"],
    "evidence_patterns": ["公式のみ適用し理由づけがない"],
    "misconceptions": ["det=0を暗記のみで運用"]
  },
  {
    "id": "LA-EIG-03",
    "name": "特性方程式",
    "definition": "det(A-λI)=0を展開して得られる特性方程式（固有方程式）とその根が固有値であることの理解",
    "prerequisites": ["LA-EIG-02", "LA-DET-02"],
    "evidence_patterns": ["特性方程式det(A-λI)=0の展開計算でλの次数や符号を誤る"],
    "misconceptions": ["特性方程式の根がそのまま固有ベクトルの成分だと誤解している"]
  },
  {
    "id": "LA-EIG-04",
    "name": "固有空間",
    "definition": "固有値λに対する固有ベクトル全体と零ベクトルからなる集合Ker(A-λI)が部分空間（固有空間）をなすことの理解",
    "prerequisites": ["LA-EIG-01", "LA-LM-03"],
    "evidence_patterns": ["固有ベクトルを1つ求めた時点で固有空間全体（他の固有ベクトルとの関係）を考慮しない"],
    "misconceptions": ["固有ベクトルは各固有値に対して一意に1つだけ存在すると思っている"]
  },
  {
    "id": "LA-EIG-05",
    "name": "固有値の代数的重複度",
    "definition": "特性多項式における固有値λの根としての重複度（代数的重複度）の理解",
    "prerequisites": ["LA-EIG-03"],
    "evidence_patterns": ["特性多項式の因数分解で重複度を数え間違える"],
    "misconceptions": ["重複度は常に1であり、重根は例外的なものだと思っている"]
  },
  {
    "id": "LA-EIG-06",
    "name": "固有値の幾何的重複度",
    "definition": "固有空間の次元（幾何的重複度）が代数的重複度以下であることの理解",
    "prerequisites": ["LA-EIG-04", "LA-EIG-05", "LA-VS-06"],
    "evidence_patterns": ["固有空間の次元を求めずに代数的重複度と同じ値を幾何的重複度として答える"],
    "misconceptions": ["幾何的重複度と代数的重複度は常に一致すると思っている"]
  },
  {
    "id": "LA-DIAG-01",
    "name": "対角化可能性の定義",
    "definition": "A=PDP^{-1}となる正則行列Pと対角行列Dが存在するときAが対角化可能であることの理解",
    "prerequisites": ["LA-EIG-04", "LA-INV-01"],
    "evidence_patterns": ["A=PDP^{-1}の関係式でP,Dの役割（P:固有ベクトル,D:固有値）を取り違える"],
    "misconceptions": ["対角化とはAを直接対角行列に書き換える操作だと誤解している"]
  },
  {
    "id": "LA-DIAG-02",
    "name": "固有ベクトルによる対角化の手順",
    "definition": "固有ベクトルを列に並べた行列Pにより、P^{-1}APが対角行列になることの理解",
    "prerequisites": ["LA-DIAG-01", "LA-VS-04"],
    "evidence_patterns": ["固有ベクトルを並べる順序とDの対角成分の順序を対応させずに計算する"],
    "misconceptions": ["固有ベクトルの並べる順序はDの対角成分の順序と無関係だと思っている"]
  },
  {
    "id": "LA-DIAG-03",
    "name": "対角化可能性の判定条件",
    "definition": "Aがn次正方行列のとき、固有ベクトルがn個一次独立に取れること（＝各固有値で幾何的重複度=代数的重複度）が対角化可能性の必要十分条件であることの理解",
    "prerequisites": ["LA-EIG-06", "LA-DIAG-02"],
    "evidence_patterns": ["固有値がすべて求まった時点で対角化可能と判断し、固有ベクトルの一次独立性を確認しない"],
    "misconceptions": ["固有値の重複がある場合でも常に対角化可能だと思っている"]
  },
  {
    "id": "LA-DIAG-04",
    "name": "対角化の応用（A^nの計算等）",
    "definition": "対角化を用いてA^n = P D^n P^{-1} のように行列のべき乗を効率よく計算できることの理解",
    "prerequisites": ["LA-DIAG-02"],
    "evidence_patterns": ["A^n = P D^n P^{-1}の関係を使わずAを愚直にn回掛けて計算しようとする"],
    "misconceptions": ["D^nの計算で対角成分をn倍する（べき乗ではなく積と誤解する）"]
  },
  {
    "id": "LA-IP-01",
    "name": "内積の定義（公理）",
    "definition": "対称性・線形性・正定値性を満たす内積の公理の理解",
    "prerequisites": ["LA-VS-01"],
    "evidence_patterns": ["内積の対称性・線形性・正定値性のいずれかを確認せず内積だと判断する"],
    "misconceptions": ["内積は幾何ベクトルの成分同士の積の和（標準内積）に限られると思っている"]
  },
  {
    "id": "LA-IP-02",
    "name": "ノルムと直交",
    "definition": "内積から導かれるノルム||v||=√<v,v>、および<u,v>=0で直交と定義されることの理解",
    "prerequisites": ["LA-IP-01"],
    "evidence_patterns": ["<u,v>=0の確認をせずに直交していると判断する"],
    "misconceptions": ["ノルムが1のベクトル同士は自動的に直交すると思っている"]
  },
  {
    "id": "LA-IP-03",
    "name": "正規直交基底",
    "definition": "基底ベクトルが互いに直交し、かつノルム1であるとき正規直交基底と呼ばれることの理解",
    "prerequisites": ["LA-IP-02", "LA-VS-05"],
    "evidence_patterns": ["基底が直交していることは確認するがノルムが1であることを確認しない"],
    "misconceptions": ["直交する基底であれば自動的に正規直交基底だと思っている（ノルム1の条件を見落とす）"]
  },
  {
    "id": "LA-IP-04",
    "name": "シュミットの直交化法",
    "definition": "任意の基底から正規直交基底を構成する手続き（グラム・シュミットの直交化）の理解",
    "prerequisites": ["LA-IP-03"],
    "evidence_patterns": ["直交化の手続きで前のベクトルへの射影を引く操作を一部省略する"],
    "misconceptions": ["シュミットの直交化を行うと基底が張る空間自体が変わってしまうと誤解している"]
  },
  {
    "id": "LA-IP-05",
    "name": "直交行列",
    "definition": "Q^T Q = I を満たす行列Qが直交行列であり、その列が正規直交基底をなすことの理解",
    "prerequisites": ["LA-IP-03", "LA-MAT-04", "LA-INV-01"],
    "evidence_patterns": ["Q^T Q = Iの確認をせず列ベクトルが単位ベクトルであることのみで直交行列と判断する"],
    "misconceptions": ["直交行列の逆行列を求める際に余因子行列など通常の方法を使い、Q^{-1}=Q^Tであることに気づかない"]
  },
  {
    "id": "LA-IP-06",
    "name": "対称行列の直交対角化",
    "definition": "実対称行列が直交行列により対角化可能である（スペクトル定理）ことの理解",
    "prerequisites": ["LA-IP-05", "LA-DIAG-03"],
    "evidence_patterns": ["対称行列でない行列にも直交行列による対角化が可能だと考えて計算を進める"],
    "misconceptions": ["すべての正方行列が直交行列で対角化できると誤解している（対称行列に限られることを見落とす）"]
  }
]
