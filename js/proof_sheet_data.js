// In-Scope Proof Cheat Sheet Data (Filtered strictly up to Slides 1.5 Section 1)
// Covering Ch. 1, 2, 4, 5, 6, 7, 8 (Excludes Ch. 9 CCA, Padding Oracle, AE)

const PROOF_SHEET_DATA = [
  {
    "id": "proof-1",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "夏農完善保密性充分必要條件形式推導",
    "source": "課本定理 / 投影片 1.2",
    "technique": "貝氏定理展開與條件機率獨立性分析",
    "target": "對所有明文 $m \\in \\mathcal{M}$ 與密文 $c \\in \\mathcal{C}$，$\\Pr[C = c \\mid M = m] = \\Pr[C = c]$，若且唯若明文與密文隨機變數相互獨立，且對任意明文對 $m_0, m_1$，$\\Pr[C = c \\mid M = m_0] = \\Pr[C = c \\mid M = m_1]$。",
    "steps": [
      "【步驟一：完善保密性定義形式化】由 Shannon 完善保密性定義，攻擊者在觀測到密文 $C = c$ 後，明文之後驗機率（A Posteriori Probability）必須嚴格等於先驗機率（A Priori Probability）：$\\forall m \\in \\mathcal{M}, \\forall c \\in \\mathcal{C}$ 且 $\\Pr[C = c] > 0$，恆有 $\\Pr[M = m \\mid C = c] = \\Pr[M = m]$。",
      "【步驟二：應用貝氏定理進行條件反轉】根據條件機率定義與貝氏定理（Bayes' Theorem），後驗機率可精確展開為：$\\Pr[M = m \\mid C = c] = \\frac{\\Pr[C = c \\mid M = m] \\cdot \\Pr[M = m]}{\\Pr[C = c]}$。",
      "【步驟三：代數化簡與消去先驗機率】將步驟一之定義代入步驟二之恆等式：$\\Pr[M = m] = \\frac{\\Pr[C = c \\mid M = m] \\cdot \\Pr[M = m]}{\\Pr[C = c]}$。因任取之明文具備正先驗機率 $\\Pr[M = m] > 0$，兩端同除以 $\\Pr[M = m]$，可得：$\\frac{\\Pr[C = c \\mid M = m]}{\\Pr[C = c]} = 1 \\iff \\Pr[C = c \\mid M = m] = \\Pr[C = c]$。",
      "【步驟四：導出任意明文對之密文分佈恆等性】因條件機率 $\\Pr[C = c \\mid M = m]$ 恆等於無條件邊際機率 $\\Pr[C = c]$，故對任意兩筆相異明文 $m_0, m_1 \\in \\mathcal{M}$，皆有：$\\Pr[C = c \\mid M = m_0] = \\Pr[C = c] = \\Pr[C = c \\mid M = m_1]$。",
      "【步驟五：全機率公式反向閉環驗證】反向推導：若對所有 $m_0, m_1$，$\\Pr[C = c \\mid M = m]$ 為定值 $\\alpha_c$，由全機率公式可得：$\\Pr[C = c] = \\sum_{m \\in \\mathcal{M}} \\Pr[C = c \\mid M = m] \\Pr[M = m] = \\alpha_c \\sum_{m \\in \\mathcal{M}} \\Pr[M = m] = \\alpha_c \\cdot 1 = \\alpha_c$。故 $\\Pr[C = c \\mid M = m] = \\Pr[C = c]$ 充分必要成立。Q.E.D。"
    ],
    "algorithm": "判定準則：檢驗對任意明文 $m$，方程式 $\\text{Enc}(K, m) = c$ 在金鑰空間 $\\mathcal{K}$ 中的解個數是否恆定相等（即 $|\\{k \\in \\mathcal{K} : \\text{Enc}(k, m) = c\\}| = \\text{const}$）。若每筆明文對應相同數量的金鑰，則密文分佈與明文獨立。",
    "pitfall": "考試扣分點：許多考生誤以為金鑰長度足夠即保密。金鑰長度足夠（$|\\mathcal{K}| \\ge |\\mathcal{M}|$）僅為必要條件，必須證明條件機率分佈嚴格相等且解的個數均勻。"
  },
  {
    "id": "proof-2",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "夏農金鑰長度下界定理反證法完整推導",
    "source": "課本 Theorem 2.10 / 練習一 29 (Ex 2.14)",
    "technique": "嚴格反證法（Proof by Contradiction）與鴿籠原理",
    "target": "任何具備解密正確性（Decryption Correctness）且達成完善保密性（Perfect Secrecy）的對稱加密方案，其金鑰空間大小必滿足 $|\\mathcal{K}| \\ge |\\mathcal{M}|$。",
    "steps": [
      "【步驟一：反證法假設】假設存在一加密方案 $(\\text{Enc}, \\text{Dec})$ 同時滿足解密正確性與完善保密性，但其金鑰空間基數小於明文空間基數，即假設 $|\\mathcal{K}| < |\\mathcal{M}|$。",
      "【步驟二：選取具正機率之合法密文】任取一筆可能被生成的密文 $c \\in \\mathcal{C}$，滿足邊際機率 $\\Pr[C = c] > 0$（若無此密文則密文空間為空，矛盾）。",
      "【步驟三：定義密文之可能解密原像集合】針對此固定密文 $c$，考慮遍歷所有可能金鑰 $k \\in \\mathcal{K}$ 所能解密出的明文集合，記為：$S(c) = \\{\\text{Dec}(k, c) \\mid k \\in \\mathcal{K}\\} \\subseteq \\mathcal{M}$。",
      "【步驟四：應用函數確定性界定集合基數】因解密演算法 $\\text{Dec}$ 為確定性函數（Deterministic Function），每把金鑰 $k$ 經 $\\text{Dec}(k, c)$ 計算至多產生一個唯一明文。故像集大小受限於金鑰個數：$|S(c)| \\le |\\mathcal{K}|$。結合步驟一之反證假設，可得嚴格不等式：$|S(c)| \\le |\\mathcal{K}| < |\\mathcal{M}|$。",
      "【步驟五：由鴿籠原理鎖定無法生成的明文】由於集合 $S(c)$ 的元素個數嚴格小於明文空間 $\\mathcal{M}$ 的總數，根據鴿籠原理（Pigeonhole Principle），明文空間中必存在至少一筆明文 $m^* \\in \\mathcal{M}$，滿足：$m^* \\notin S(c)$（即 $m^* \\in \\mathcal{M} \\setminus S(c)$）。",
      "【步驟六：導出條件機率為零】分析明文為 $m^*$ 時產生密文 $c$ 的機率。若存在金鑰 $k^* \\in \\mathcal{K}$ 使得 $\\text{Enc}(k^*, m^*) = c$，則由解密正確性必有 $\\text{Dec}(k^*, c) = m^*$，這將導致 $m^* \\in S(c)$，與步驟五之結論 $m^* \\notin S(c)$ 產生矛盾！因此，在金鑰空間中不存在任何能將 $m^*$ 加密為 $c$ 的金鑰，由此推得：$\\Pr[C = c \\mid M = m^*] = 0$。",
      "【步驟七：導出機率矛盾並完成閉環】根據完善保密性之要求（步驟一），對所有合法明文 $m$，密文條件機率恆等於無條件機率：$\\Pr[C = c \\mid M = m^*] = \\Pr[C = c]$。然而步驟二已知 $\\Pr[C = c] > 0$，步驟六卻證明 $\\Pr[C = c \\mid M = m^*] = 0$，產生致命矛盾（$0 > 0$ 不成立）！因此假設 $|\\mathcal{K}| < |\\mathcal{M}|$ 不成立，原命題必定成立：$|\\mathcal{K}| \\ge |\\mathcal{M}|$。Q.E.D。"
    ],
    "algorithm": "反例構造驗證法：給定任何被宣稱 $|\\mathcal{K}| < |\\mathcal{M}|$ 卻具保密性的方案，計算 $S(c) = \\{\\text{Dec}(k, c) : k \\in \\mathcal{K}\\}$。由 $|S(c)| < |\\mathcal{M}|$ 必可挑出 $m^* \\notin S(c)$，證明 $\\Pr[C=c \\mid M=m^*] = 0$，直接擊潰其保密性論述。",
    "pitfall": "考試扣分點：證明過程中必須明確定義集合 $S(c)$，且務必點出「$\\text{Dec}$ 為確定性函數」這一關鍵依據（否則無法推導 $|S(c)| \\le |\\mathcal{K}|$）。"
  },
  {
    "id": "proof-3",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "OTP 挑戰者博弈不可區分性推導",
    "source": "課本 Lemma 2.3 / 練習一 15",
    "technique": "全機率展開與對稱性消去",
    "target": "在 IND-OTS 挑戰者博弈中，對任意攻擊者 $\\mathcal{A}$，猜中隨機位元 $b$ 之機率恆滿足 $\\Pr[b' = b] = \\frac{1}{2}$，優勢嚴格為 0。",
    "steps": [
      "【步驟一：挑戰者博弈互動模型】攻擊者提交兩筆等長相異明文 $M_0, M_1 \\in \\{0, 1\\}^n$。挑戰者均勻隨機抽取挑戰位元 $b \\leftarrow \\{0, 1\\}$（即 $\\Pr[b=0]=\\Pr[b=1]=1/2$）及獨立均勻金鑰 $K \\leftarrow \\{0, 1\\}^n$。",
      "【步驟二：密文生成與條件機率表達】挑戰密文計算為 $C^* = K \\oplus M_b$。對任意固定密文向量 $c \\in \\{0, 1\\}^n$，在給定挑戰位元 $b=0$ 下：$\\Pr[C^* = c \\mid b = 0] = \\Pr[K \\oplus M_0 = c] = \\Pr[K = c \\oplus M_0]$。同理，在給定 $b=1$ 下：$\\Pr[C^* = c \\mid b = 1] = \\Pr[K \\oplus M_1 = c] = \\Pr[K = c \\oplus M_1]$。",
      "【步驟三：金鑰均勻分佈之不變性】因金鑰 $K$ 嚴格均勻選自 $\\{0, 1\\}^n$，對任意固定位元串 $x \\in \\{0, 1\\}^n$，恆有 $\\Pr[K = x] = 2^{-n}$。因此：$\\Pr[K = c \\oplus M_0] = 2^{-n}$ 且 $\\Pr[K = c \\oplus M_1] = 2^{-n}$。由此證明密文分佈完全獨立於 $b$：$\\Pr[C^* = c \\mid b = 0] = \\Pr[C^* = c \\mid b = 1] = 2^{-n}$。",
      "【步驟四：攻擊者輸出機率之全機率求和】攻擊者接收密文 $c$ 後以決定性或隨機化方式輸出猜測位元 $b' = \\mathcal{A}(c)$。計算條件輸出機率：$\\Pr[b'=1 \\mid b=0] = \\sum_{c \\in \\{0,1\\}^n} \\Pr[\\mathcal{A}(c)=1] \\cdot \\Pr[C^*=c \\mid b=0] = 2^{-n} \\sum_{c} \\Pr[\\mathcal{A}(c)=1]$。同理，$\\Pr[b'=1 \\mid b=1] = \\sum_{c \\in \\{0,1\\}^n} \\Pr[\\mathcal{A}(c)=1] \\cdot \\Pr[C^*=c \\mid b=1] = 2^{-n} \\sum_{c} \\Pr[\\mathcal{A}(c)=1]$。",
      "【步驟五：優勢與勝率精確計算】兩條件機率完全相等：$\\Pr[b'=1 \\mid b=1] - \\Pr[b'=1 \\mid b=0] = 0$。根據不可區分優勢定義：$\\mathbf{Adv} = |\\Pr[b'=1 \\mid b=1] - \\Pr[b'=1 \\mid b=0]| = 0$。攻擊者猜對勝率為：$\\Pr[b'=b] = \\frac{1}{2}\\Pr[b'=0 \\mid b=0] + \\frac{1}{2}\\Pr[b'=1 \\mid b=1] = \\frac{1}{2} + \\frac{1}{2}\\mathbf{Adv} = \\frac{1}{2}$。證明完畢。"
    ],
    "algorithm": "不可區分性結論：任何演算法（無論具備多少計算算力）在 OTP 密文上的輸出行為完全獨立於挑戰明文之選擇，資訊理論上不可攻破。",
    "pitfall": "證明中切勿只口語敘述「因為 XOR 很安全」；必須明確寫出條件機率與全機率求和式，展示求和項在兩邊完全抵消的過程。"
  },
  {
    "id": "proof-4",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "模 10 加法 OTP 完善保密性形式證明",
    "source": "作業一 1(b)",
    "technique": "阿貝爾群同構與唯一加法反元素",
    "target": "在十進位數字 $\\{0, \\dots, 9\\}$ 上，方案 $\\text{Enc}(K, M) = (K + M) \\bmod 10$ 具備解密正確性與完善保密性。",
    "steps": [
      "【步驟一：方案定義與空間界定】明文空間、金鑰空間與密文空間皆為十進位字元集：$\\mathcal{M} = \\mathcal{K} = \\mathcal{C} = \\mathbb{Z}_{10} = \\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\}$。加密演算法為 $\\text{Enc}(K, M) = (K + M) \\bmod 10$，解密演算法為 $\\text{Dec}(K, C) = (C - K) \\bmod 10$。",
      "【步驟二：解密正確性形式化推導】對任意金鑰 $K \\in \\mathbb{Z}_{10}$ 與任意明文 $M \\in \\mathbb{Z}_{10}$，計算複合函數：$\\text{Dec}(K, \\text{Enc}(K, M)) = (((K + M) \\bmod 10) - K) \\bmod 10$。利用模運算之分配律與線性性質：$((K + M) - K) \\bmod 10 = (K + M - K) \\bmod 10 = M \\bmod 10$。因定義 $M \\in \\{0, \\dots, 9\\}$，故 $M \\bmod 10 = M$ 恆成立，解密正確性得證。",
      "【步驟三：群論性質與唯一反元素分析】代數結構 $(\\mathbb{Z}_{10}, +)$ 構成一個 10 階有限阿貝爾群（Finite Abelian Group）。根據群之公理，群中任意元素 $m \\in \\mathbb{Z}_{10}$ 必存在唯一的加法反元素（Additive Inverse），記為 $-m \\equiv (10 - m) \\pmod{10}$。",
      "【步驟四：同餘方程式之唯一金鑰解】對任意給定的明文 $m \\in \\mathbb{Z}_{10}$ 與密文 $c \\in \\mathbb{Z}_{10}$，考慮密文生成方程式：$(K + m) \\bmod 10 = c \\iff K + m \\equiv c \\pmod{10}$。在同餘方程兩端同時加上加法反元素 $-m$：$K + m + (-m) \\equiv c + (-m) \\pmod{10} \\iff K \\equiv (c - m) \\pmod{10}$。由於反元素唯一，該同餘方程在金鑰空間 $\\mathcal{K} = \\{0, \\dots, 9\\}$ 中存在且僅存在唯一整數解：$k^* = (c - m) \\bmod 10$。",
      "【步驟五：條件機率均勻性證明】設金鑰 $K$ 均勻隨機選自 $\\{0, \\dots, 9\\}$，則對任意 $k \\in \\mathcal{K}$，$\\Pr[K = k] = \\frac{1}{10}$。因此對任意固定明文 $m$ 與密文 $c$：$\\Pr[C = c \\mid M = m] = \\Pr[K = (c - m) \\bmod 10] = \\Pr[K = k^*] = \\frac{1}{10}$。條件機率對所有明文 $m$ 恆為常數 $1/10$，與明文完全獨立。由夏農充分必要條件，該方案達成完善保密性。Q.E.D。"
    ],
    "algorithm": "關鍵代數原理：群 $(\\mathbb{Z}_N, +)$ 的加法位移映射 $x \\mapsto x + k$ 為雙射置換，均勻分佈在群上經雙射位移後其統計分佈恆定保持均勻。",
    "pitfall": "考試扣分點：必須強調在 $\\mathbb{Z}_{10}$ 中反元素唯一性，明確證明「每個密文對應恰好一把有效金鑰」，不可含糊帶過。"
  },
  {
    "id": "proof-5",
    "category": "ch1-2",
    "chapter": "Ch. 1",
    "title": "模 n 乘法 OTP 之質數條件證明",
    "source": "課本 Exercise 1.15 / 練習一 27",
    "technique": "有限環乘法單位群與歐拉函數 $\\phi(n)$",
    "target": "在空間 $\\{1, \\dots, n-1\\}$ 上以模 $n$ 乘法加密 $\\text{Enc}(K, M) = (K \\cdot M) \\bmod n$，該方案達成完善保密性若且唯若 $n$ 為質數。",
    "steps": [
      "【步驟一：充分性（$n$ 為質數）代數結構分析】當模數 $n$ 為質數時，整數集合 $\\{1, 2, \\dots, n-1\\}$ 與有限體 $\\mathbb{F}_n$ 的乘法單位群 $\\mathbb{Z}_n^*$ 完全重合，群的階數為 $|\\mathbb{Z}_n^*| = n - 1$。",
      "【步驟二：乘法反元素存在性與唯一解】對任意固定明文 $m \\in \\{1, \\dots, n-1\\}$，因 $n$ 為質數，$\\gcd(m, n) = 1$。由裴蜀定理（Bézout's Identity）或歐拉定理，乘法逆元素 $m^{-1} \\pmod n$ 存在且在 $\\{1, \\dots, n-1\\}$ 中唯一。同餘方程 $K \\cdot m \\equiv c \\pmod n$ 兩端同乘 $m^{-1}$，得唯一金鑰解：$K \\equiv c \\cdot m^{-1} \\pmod n$。當 $K$ 均勻隨機抽取時，$\\Pr[C = c \\mid M = m] = \\Pr[K = c \\cdot m^{-1} \\bmod n] = \\frac{1}{n-1}$。密文分佈嚴格均勻且與 $m$ 無關，滿足完善保密性。",
      "【步驟三：必要性（$n$ 為合數）零因子反例構造】若 $n$ 為合數，則 $n$ 必定存在非平凡真因數（Proper Factor）$p$，滿足 $1 < p < n$ 且 $p \\mid n$。挑選明文 $M_0 = p$。",
      "【步驟四：密文空間之因子退化性分析】對任意選取的金鑰 $K \\in \\{1, 2, \\dots, n-1\\}$，計算密文 $C = (K \\cdot p) \\bmod n$。由整除性質，存在整數 $q$ 使得 $K \\cdot p = q \\cdot n + C$，因此 $C = K \\cdot p - q \\cdot n$。因 $p \\mid n$，上式右端必能被 $p$ 整除，故 $p \\mid C$ 恆成立！這證明密文 $C$ 只能是 $p$ 的倍數，或在模 $n$ 下等於 0。",
      "【步驟五：導出條件機率為零產生分佈斷裂】因 $p > 1$，密文空間中與 $n$ 互質的元素（例如 $c = 1$，因 $\\gcd(1, n) = 1$ 故不可能為 $p$ 的倍數）絕不可能成為明文 $M_0 = p$ 的密文！因此：$\\Pr[C = 1 \\mid M = p] = 0$。",
      "【步驟六：對比另一明文並證偽完善保密性】若挑選另一明文 $M_1 = 1$，則密文為 $C = (K \\cdot 1) \\bmod n = K$。因金鑰 $K$ 均勻選自 $\\{1, \\dots, n-1\\}$，故：$\\Pr[C = 1 \\mid M = 1] = \\Pr[K = 1] = \\frac{1}{n-1} > 0$。因 $\\Pr[C = 1 \\mid M = p] = 0 \\neq \\frac{1}{n-1} = \\Pr[C = 1 \\mid M = 1]$，密文分佈依賴於明文，完善保密性破壞。故方案安全充要條件為 $n$ 必須為質數。Q.E.D。"
    ],
    "algorithm": "合數區分演算法：提交 $M_0 = p$（$n$ 之因子）與 $M_1 = 1$。取得挑戰密文 $C^*$。若 $\\gcd(C^*, n) > 1$（密文含有因數 $p$）則判定為 $M_0$；否則判定為 $M_1$。區分勝率達 $1$。",
    "pitfall": "考試扣分點：必須涵蓋合數存在零因子（Zero Divisors）導致乘法映射非滿射的代數論證，不可只寫「因為合數無法求逆」。"
  },
  {
    "id": "proof-6",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "模 10 乘法加密不具單次保密性證明",
    "source": "課本 Exercise 2.13 / 練習一 28",
    "technique": "合數環零因子反例法",
    "target": "金鑰與明文取自 $\\{1, \\dots, 9\\}$，加密函數為 $\\text{Enc}(K, M) = (K \\cdot M) \\bmod 10$，該方案不具備單次保密性（IND-OTS 不安全）。",
    "steps": [
      "【步驟一：反例構造與明文挑選】選取兩筆相異明文：$M_0 = 5$（10 之非平凡質因數）與 $M_1 = 1$（單位元素）。金鑰 $K$ 均勻取樣自空間 $\\mathcal{K} = \\{1, 2, \\dots, 9\\}$，即 $\\Pr[K = k] = 1/9$。",
      "【步驟二：明文 M0 = 5 之密文取值全分析】計算所有可能金鑰下 $M_0 = 5$ 的密文輸出 $C = (K \\cdot 5) \\bmod 10$：\n- 當 $K \\in \\{1, 3, 5, 7, 9\\}$（奇數）時，$(K \\cdot 5) \\bmod 10 = 5$。\n- 當 $K \\in \\{2, 4, 6, 8\\}$（偶數）時，$(K \\cdot 5) \\bmod 10 = 0$。\n由此可見，密文只能落在集合 $\\{0, 5\\}$ 中。",
      "【步驟三：條件機率計算】檢驗密文 $c = 1$ 之出現機率：在明文為 $M_0 = 5$ 時，輸出 $C = 1$ 的事件不可能發生，故條件機率為：$\\Pr[C = 1 \\mid M = 5] = 0$。",
      "【步驟四：明文 M1 = 1 之密文取值對比】計算明文 $M_1 = 1$ 時的密文輸出：$C = (K \\cdot 1) \\bmod 10 = K$。當 $K$ 均勻分佈於 $\\{1, \\dots, 9\\}$ 時，密文 $C$ 等於 1 的機率為：$\\Pr[C = 1 \\mid M = 1] = \\Pr[K = 1] = \\frac{1}{9}$。",
      "【步驟五：不相等式證偽單次保密性】比較步驟三與步驟四之條件機率：$\\Pr[C = 1 \\mid M = 5] = 0 \\neq \\frac{1}{9} = \\Pr[C = 1 \\mid M = 1]$。密文輸出分佈明顯依賴明文之選取，違反單次完善保密性定義，方案不安全。Q.E.D。"
    ],
    "algorithm": "區分者演算法 $D$：提交 $M_0 = 5, M_1 = 1$。收到挑戰密文 $C^*$。若 $C^* \\in \\{0, 5\\}$ 輸出猜測 0；若 $C^* \\in \\{1, 2, 3, 4, 6, 7, 8, 9\\}$ 輸出猜測 1。優勢 $\\mathbf{Adv} = 1$。",
    "pitfall": "考試扣分點：切勿僅口語寫「因為 10 是合數」；評分標準要求明確列出兩個特定明文與特定密文（如 $c=1$）的機率不相等式。"
  },
  {
    "id": "proof-7",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "AND 運算型 OTP 正確性與保密性破壞反例",
    "source": "作業一 1(a)",
    "technique": "非單射映射（Non-injective Mapping）證明",
    "target": "加密方案 $\\text{Enc}(K, M) = K \\wedge M$ 既不具備解密正確性，亦不具備完善保密性。",
    "steps": [
      "【步驟一：正確性定義與反例選取】正確性公理要求存在解密演算法 $\\text{Dec}$，使得 $\\forall K, \\forall M$，$\\text{Dec}(K, \\text{Enc}(K, M)) = M$ 恆成立。考慮金鑰 $K = 0$，分別加密明文 $M = 0$ 與 $M = 1$：$\\text{Enc}(0, 0) = 0 \\wedge 0 = 0$；$\\text{Enc}(0, 1) = 0 \\wedge 1 = 0$。",
      "【步驟二：非單射性證明正確性失敗】在金鑰 $K = 0$ 固定下，加密映射 $M \\mapsto 0 \\wedge M$ 將兩個相異明文 $0$ 與 $1$ 同時映射至同一個密文 $0$。解密演算法給定金鑰 $K = 0$ 與密文 $C = 0$ 時，無法判定原明文究竟為 0 或 1。映射非單射（Non-injective），逆函數不存在，故方案不具備解密正確性。",
      "【步驟三：完善保密性破壞之機率模型】設金鑰 $K \\leftarrow \\{0, 1\\}$ 均勻隨機抽取，即 $\\Pr[K = 0] = \\Pr[K = 1] = 1/2$。選取兩筆明文 $M_0 = 0$ 與 $M_1 = 1$。",
      "【步驟四：明文 M0 = 0 之條件分佈】當明文為 $M_0 = 0$ 時，密文 $C = K \\wedge 0 = 0$ 恆成立，因此密文輸出 1 的機率為：$\\Pr[C = 1 \\mid M = 0] = 0$。",
      "【步驟五：明文 M1 = 1 之條件分佈與對比】當明文為 $M_1 = 1$ 時，密文 $C = K \\wedge 1 = K$。密文輸出 1 的機率等於金鑰為 1 的機率：$\\Pr[C = 1 \\mid M = 1] = \\Pr[K = 1] = \\frac{1}{2}$。兩者條件機率不相等：$\\Pr[C = 1 \\mid M = 0] \\neq \\Pr[C = 1 \\mid M = 1]$，完善保密性遭到破壞。Q.E.D。"
    ],
    "algorithm": "資訊洩漏機制：一旦攻擊者攔截到密文 $C = 1$，可百分之百肯定明文必為 1（因為若明文為 0，AND 運算絕不可能輸出 1），機密瞬間瓦解。",
    "pitfall": "考試扣分點：不可僅直覺回答「AND 是單向的不可逆」；必須嚴格展示 $K=0$ 時明文的碰撞，以及條件機率 $0 \\neq 1/2$。"
  },
  {
    "id": "proof-8",
    "category": "ch1-2",
    "chapter": "Ch. 1-2",
    "title": "金鑰減半 Two-Time Pad 差分消除破壞定理",
    "source": "作業一 1(c) / 練習一 16",
    "technique": "線性 XOR 差分消除與區分者建構",
    "target": "若 $\\text{Enc}(K, (M_1, M_2)) = (K \\oplus M_1, K \\oplus M_2)$ 且 $|K| = |M_1| = |M_2| = n$，此方案不具備單次保密性，攻擊者能無條件萃取明文之位元差分。",
    "steps": [
      "【步驟一：密文結構形式化】密文分為兩個等長區塊：$C_1 = K \\oplus M_1$ 與 $C_2 = K \\oplus M_2$，其中金鑰 $K$ 在兩個區塊中被重複使用（Two-Time Pad 模式）。",
      "【步驟二：線性代數差分消除推導】計算兩密文區塊之 XOR 差分：$C_1 \\oplus C_2 = (K \\oplus M_1) \\oplus (K \\oplus M_2)$。利用 XOR 運算之交換律、結合律與自反性（$K \\oplus K = 0^n$）：$C_1 \\oplus C_2 = (K \\oplus K) \\oplus (M_1 \\oplus M_2) = 0^n \\oplus (M_1 \\oplus M_2) = M_1 \\oplus M_2$。密鑰 $K$ 完全被代數消除！",
      "【步驟三：萃取明文資訊分析】\n1. 明文相等性洩漏：若 $M_1 = M_2$，則密文恆有 $C_1 \\oplus C_2 = 0^n \\iff C_1 = C_2$，直接暴露出明文重複。\n2. 已知前綴破譯（Crib Dragging）：若 $M_1$ 為網路協定標準標頭（如 HTTP GET），則 $M_2 = (C_1 \\oplus C_2) \\oplus M_1$ 被完全還原。",
      "【步驟四：形式化區分者博弈設計】構造多項式時間區分者 $D$：\n1. 挑選挑戰明文對：$M^{(0)} = (0^n, 0^n)$ 與 $M^{(1)} = (0^n, 1^n)$。\n2. 收到挑戰密文 $(C_1^*, C_2^*)$。\n3. 計算差分：若 $C_1^* \\oplus C_2^* == 0^n$ 輸出 0；否則輸出 1。",
      "【步驟五：優勢計算】\n- 若 $b = 0$：$M_1 \\oplus M_2 = 0^n \\oplus 0^n = 0^n$，故 $C_1^* \\oplus C_2^* = 0^n$ 機率為 1，$\\Pr[D \\to 0 \\mid b = 0] = 1$。\n- 若 $b = 1$：$M_1 \\oplus M_2 = 0^n \\oplus 1^n = 1^n \\neq 0^n$，故 $C_1^* \\oplus C_2^* = 1^n$ 機率為 1，$\\Pr[D \\to 0 \\mid b = 1] = 0$。\n區分優勢 $\\mathbf{Adv} = |1 - 0| = 1$。保密性徹底破裂。Q.E.D。"
    ],
    "algorithm": "區分者偽代碼：\n1. (C1, C2) = Challenge((0^n, 0^n), (0^n, 1^n))\n2. return (C1 ^ C2 == 0^n) ? 0 : 1",
    "pitfall": "考試扣分點：題目通常要求「明確指出可萃取的資訊」及「具體攻擊演算法」，必須將代數差分公式與區分者優勢一併寫出。"
  },
  {
    "id": "proof-9",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "函式庫等價性 L1 ≡ L2 分支恆等證明",
    "source": "作業一 2(a)",
    "technique": "分支等價性分析（Branch Equivalence）與隨機變數代換",
    "target": "證明 $\\mathcal{L}_1 \\equiv \\mathcal{L}_2$，其中 $\\mathcal{L}_1: \\text{query}(M) \\to K \\oplus M$ ($K$ 隨機)；$\\mathcal{L}_2: \\text{query}(M) \\to [\\text{if } M=R_1 \\text{ return } R_2 \\text{ else return } M \\oplus R_1 \\oplus R_2]$ ($R_1, R_2$ 隨機)。",
    "steps": [
      "【步驟一：分析 L2 之條件分支邊界】檢視 $\\mathcal{L}_2$ 的條件判斷：若輸入 $M = R_1$，執行 `return R2`；若 $M \\neq R_1$，執行 `return M ⊕ R1 ⊕ R2`。",
      "【步驟二：將邊界條件代入 else 分支表達式】假設我們忽略 `if` 判斷，直接對邊界值 $M = R_1$ 計算 `else` 分支的代數表達式：$M \\oplus R_1 \\oplus R_2 = R_1 \\oplus R_1 \\oplus R_2 = (R_1 \\oplus R_1) \\oplus R_2 = 0^n \\oplus R_2 = R_2$。",
      "【步驟三：代數化簡揭示冗餘程式碼】計算結果與 `if` 分支的強制回傳值 $R_2$ 毫釐不差完全恆等！這證明無論輸入明文 $M$ 是否等於隨機數 $R_1$，$\\mathcal{L}_2$ 的輸出皆唯一等於：$\\text{query}(M) = M \\oplus (R_1 \\oplus R_2)$。`if` 判斷式在語義上為純粹冗餘程式碼。",
      "【步驟四：引入隨機變數替換】令新隨機變數 $K' = R_1 \\oplus R_2$。因 $R_1, R_2$ 為獨立且均勻分佈於 $\\{0, 1\\}^n$ 的隨機字串，根據 OTP 隨機性引理，兩個均勻隨機字串的 XOR 依然為嚴格均勻分佈：$K' \\leftarrow \\{0, 1\\}^n$。",
      "【步驟五：得出聯合機率分佈恆等性】因此，$\\mathcal{L}_2$ 的行為等價於在內部維持一個均勻隨機金鑰 $K'$，每次查詢回傳 $M \\oplus K'$。此 I/O 聯合機率分佈與 $\\mathcal{L}_1$（回傳 $M \\oplus K$）完全相同。對任意演算法，兩函式庫不可區分：$\\mathcal{L}_1 \\equiv \\mathcal{L}_2$。Q.E.D。"
    ],
    "algorithm": "結論：兩函式庫在所有多項式時間程式下的回傳分佈恆等，無任何區分者能以大於 0 之優勢區分它們。",
    "pitfall": "考試扣分點：切勿耗費時間嘗試構造區分者；需先證明分支在代數上的恆等性，再引用隨機變數 XOR 的均勻分佈保持性。"
  },
  {
    "id": "proof-10",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "加解密狀態一致性約束區分者建構",
    "source": "作業一 2(b)",
    "technique": "密碼系統跨查詢狀態一致性檢驗",
    "target": "證明 $\\mathcal{L}_C \\not\\equiv \\mathcal{L}_D$，其中 $\\mathcal{L}_C$ 為共用金鑰之真實加解密庫，$\\mathcal{L}_D$ 為獨立隨機回傳之加解密庫。",
    "steps": [
      "【步驟一：分析兩函式庫之行為差異】\n- 在真實加解密庫 $\\mathcal{L}_C$ 中，$\\text{enc}(M)$ 產生 $C = K \\oplus M$；當呼叫 $\\text{dec}(C)$ 時，解密計算 $K \\oplus C = K \\oplus (K \\oplus M) = M$ 恆成立（維持內部狀態一致性）。\n- 在獨立隨機庫 $\\mathcal{L}_D$ 中，每次呼叫 $\\text{enc}(M)$ 獨立均勻抽取 $C \\leftarrow \\{0, 1\\}^n$ 回傳；每次呼叫 $\\text{dec}(C)$ 亦獨立均勻抽取 $M' \\leftarrow \\{0, 1\\}^n$ 回傳，加解密之間毫無狀態關聯。",
      "【步驟二：構造利用解密正確性之區分者 D】構造多項式時間區分者演算法 $D$：\n1. 呼叫加密介面：$C^* := \\text{enc}(0^n)$。\n2. 將獲得之密文 $C^*$ 送入解密介面：$M' := \\text{dec}(C^*)$。\n3. 比對結果：若 $M' == 0^n$ 輸出 1（判定為真實密碼庫 $\\mathcal{L}_C$）；否則輸出 0（判定為獨立隨機庫 $\\mathcal{L}_D$）。",
      "【步驟三：在真實庫 LC 下之條件機率】在 $\\mathcal{L}_C$ 下，解密演算法保證完全還原輸入：$M' = \\text{dec}(C^*) = K \\oplus (K \\oplus 0^n) = 0^n$。此等式以機率 1 恆成立：$\\Pr[D \\to 1 \\mid \\mathcal{L}_C] = 1$。",
      "【步驟四：在獨立隨機庫 LD 下之條件機率】在 $\\mathcal{L}_D$ 下，$M'$ 為獨立均勻選取的隨機字串，其取值恰好等於 $0^n$ 的機率為：$\\Pr[D \\to 1 \\mid \\mathcal{L}_D] = \\Pr[M' = 0^n] = 2^{-n}$。",
      "【步驟五：優勢計算】區分優勢為：$\\mathbf{Adv} = |\\Pr[D \\to 1 \\mid \\mathcal{L}_C] - \\Pr[D \\to 1 \\mid \\mathcal{L}_D]| = |1 - 2^{-n}| = 1 - 2^{-n} \\approx 1$。優勢不可忽略，兩函式庫可被區分：$\\mathcal{L}_C \\not\\equiv \\mathcal{L}_D$。Q.E.D。"
    ],
    "algorithm": "區分者代碼：\n1. C = enc(0^n)\n2. M = dec(C)\n3. return (M == 0^n) ? 1 : 0",
    "pitfall": "考試扣分點：如果攻擊者只單獨呼叫 enc 或只呼叫 dec，兩者單獨看都是均勻亂數無法區分；關鍵在於「串聯呼叫 enc 後 dec」測試解密正確性約束。"
  },
  {
    "id": "proof-11",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "無用隨機變數庫邊際分佈不變性證明",
    "source": "練習一 17",
    "technique": "邊際機率分佈求和（Marginal Distribution Summation）",
    "target": "證明 $\\mathcal{L}_A \\equiv \\mathcal{L}_B$，其中 $\\mathcal{L}_A: y \\leftarrow \\{0,1\\}^n; \\text{return } y$；$\\mathcal{L}_B: y \\leftarrow \\{0,1\\}^n; z \\leftarrow \\{0,1\\}^n; \\text{return } y$。",
    "steps": [
      "【步驟一：分析兩函式庫之隨機空間】\n- $\\mathcal{L}_A$ 內部隨機變數為 $Y$，抽樣空間為 $\\{0, 1\\}^n$。\n- $\\mathcal{L}_B$ 內部隨機變數為有序對 $(Y, Z)$，抽樣空間為 $\\{0, 1\\}^n \\times \\{0, 1\\}^n$。",
      "【步驟二：計算 LA 之輸出機率分佈】在 $\\mathcal{L}_A$ 中，變數 $Y$ 均勻隨機抽取，對任意固定向量 $y \\in \\{0, 1\\}^n$：$\\Pr_{\\mathcal{L}_A}[Y = y] = 2^{-n}$。",
      "【步驟三：計算 LB 內部之聯合機率分佈】在 $\\mathcal{L}_B$ 中，$Y$ 與 $Z$ 獨立均勻抽取，聯合機率分佈為：$\\Pr[Y = y, Z = z] = \\Pr[Y = y] \\cdot \\Pr[Z = z] = 2^{-n} \\cdot 2^{-n} = 2^{-2n}$。",
      "【步驟四：對未觀測變數 Z 進行邊際化（求和）】函式庫 $\\mathcal{L}_B$ 的外部介面僅回傳 $Y$，內部變數 $Z$ 未曾洩漏。根據全機率公式，對所有可能的 $z \\in \\{0, 1\\}^n$ 進行邊際求和：$\\Pr_{\\mathcal{L}_B}[Y = y] = \\sum_{z \\in \\{0, 1\\}^n} \\Pr[Y = y, Z = z] = \\sum_{z \\in \\{0, 1\\}^n} 2^{-2n} = 2^n \\cdot 2^{-2n} = 2^{-n}$。",
      "【步驟五：結論閉環】對所有可能的輸出 $y \\in \\{0, 1\\}^n$，兩函式庫的邊際輸出分佈完全相等：$\\Pr_{\\mathcal{L}_A}[Y = y] = \\Pr_{\\mathcal{L}_B}[Y = y] = 2^{-n}$。因此兩函式庫等價不可區分：$\\mathcal{L}_A \\equiv \\mathcal{L}_B$。Q.E.D。"
    ],
    "algorithm": "密碼學基本公理：任何未經介面洩漏、且與回傳值相互獨立的內部隨機抽樣，對攻擊者的視角不產生任何統計影響。",
    "pitfall": "考試扣分點：不可因為「多抽樣了變數 $z$ 的運算時間」而判定可區分；在可證明安全模型中，介面輸出之機率分佈等價性為唯一衡量標準。"
  },
  {
    "id": "proof-12",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "混合論證技術（Hybrid Proof）嚴格形式證明",
    "source": "練習一 19",
    "technique": "中間混合庫（Hybrid Library）與雙射變換",
    "target": "利用 Hybrid Proof 證明 $\\mathcal{L}_1 \\equiv \\mathcal{L}_2$，其中 $\\mathcal{L}_1: X \\leftarrow \\{0,1\\}^n; \\text{return } (X, X \\oplus 1^n)$；$\\mathcal{L}_2: Y \\leftarrow \\{0,1\\}^n; \\text{return } (Y \\oplus 1^n, Y)$。",
    "steps": [
      "【步驟一：目標設定與混合庫定義】欲證兩隨機有序對函式庫等價。引入中間混合庫（Hybrid Library）$\\mathcal{L}_{\\text{hyb}}$：\n$\\mathcal{L}_{\\text{hyb}}()$: 抽樣 $Y \\leftarrow \\{0, 1\\}^n$；計算 $X' := Y \\oplus 1^n$；回傳有序對 $(X', X' \\oplus 1^n)$。",
      "【步驟二：證明第一跳 L1 ≡ L_hyb】分析 $\\mathcal{L}_{\\text{hyb}}$ 中 $X'$ 的分佈。映射 $f(Y) = Y \\oplus 1^n$ 是集合 $\\{0, 1\\}^n$ 到自身的一對一雙射置換（Bijective Permutation）。當輸入 $Y$ 均勻分佈時，其雙射映射值 $X' = Y \\oplus 1^n$ 亦嚴格均勻分佈於 $\\{0, 1\\}^n$。因此，$(X', X' \\oplus 1^n)$ 的聯合分佈與 $\\mathcal{L}_1$ 中的 $(X, X \\oplus 1^n)$ 完全相同，故 $\\mathcal{L}_1 \\equiv \\mathcal{L}_{\\text{hyb}}$。",
      "【步驟三：證明第二跳 L_hyb ≡ L2】在 $\\mathcal{L}_{\\text{hyb}}$ 中，檢視回傳有序對的第二個分量：$X' \\oplus 1^n = (Y \\oplus 1^n) \\oplus 1^n = Y \\oplus (1^n \\oplus 1^n) = Y \\oplus 0^n = Y$。將化簡結果代入，$\\mathcal{L}_{\\text{hyb}}$ 實際回傳的有序對為 $(Y \\oplus 1^n, Y)$，這與 $\\mathcal{L}_2$ 的程式碼定義完全一致，故 $\\mathcal{L}_{\\text{hyb}} \\equiv \\mathcal{L}_2$。",
      "【步驟四：不可區分性之傳遞性閉環】根據不可區分等價關係之傳遞性（Transitivity）：$\\mathcal{L}_1 \\equiv \\mathcal{L}_{\\text{hyb}}$ 且 $\\mathcal{L}_{\\text{hyb}} \\equiv \\mathcal{L}_2$，直接導出：$\\mathcal{L}_1 \\equiv \\mathcal{L}_2$。證明完畢。Q.E.D。"
    ],
    "algorithm": "混合論證規範：每一跳（Hop）必須明確陳述代數等價性或引理支撐，確保兩端鏈結閉環。",
    "pitfall": "考試扣分點：必須具體寫出中間庫 $\\mathcal{L}_{\\text{hyb}}$ 的虛擬代碼，切勿直接跳步宣稱等價。"
  },
  {
    "id": "proof-13",
    "category": "ch1-2",
    "chapter": "Ch. 2",
    "title": "修改型 OTP 方案 Σ' 單次保密性證明",
    "source": "作業一 3",
    "technique": "決定性派生密文（Deterministic Derivation）分佈分析",
    "target": "構造方案 $\\text{Enc}'(K, M) = (C_1, C_2) = (K \\oplus M, K \\oplus M \\oplus 1^n)$，證明 $\\Sigma'$ 在單次加密下依然具備完善保密性。",
    "steps": [
      "【步驟一：挑戰博弈設定】攻擊者提交兩筆等長相異明文 $M^{(0)}, M^{(1)} \\in \\{0, 1\\}^n$。挑戰者選取 $b \\leftarrow \\{0, 1\\}$ 與均勻隨機金鑰 $K \\leftarrow \\{0, 1\\}^n$。",
      "【步驟二：密文分量展開】挑戰密文有序對為：$(C_1^*, C_2^*) = (K \\oplus M^{(b)}, K \\oplus M^{(b)} \\oplus 1^n)$。注意到第二分量完全由第一分量決定性導出：$C_2^* = C_1^* \\oplus 1^n$。",
      "【步驟三：第一分量邊際機率分佈】由標準 OTP 完善保密性，對任意固定明文 $m \\in \\{M^{(0)}, M^{(1)}\\}$，第一分量 $C_1^* = K \\oplus m$ 在 $\\{0, 1\\}^n$ 上嚴格均勻分佈：$\\Pr[C_1^* = c_1 \\mid M^{(b)} = m] = \\Pr[K = c_1 \\oplus m] = 2^{-n}$。",
      "【步驟四：密文有序對聯合條件機率分析】對任意候選密文對 $(c_1, c_2) \\in \\{0, 1\\}^n \\times \\{0, 1\\}^n$：\n- 若 $c_2 \\neq c_1 \\oplus 1^n$：該密文對不可能由演算法生成，機率為 0：$\\Pr[(C_1^*, C_2^*) = (c_1, c_2) \\mid M^{(b)} = m] = 0$。\n- 若 $c_2 = c_1 \\oplus 1^n$：事件等價於 $C_1^* = c_1$，機率為：$\\Pr[(C_1^*, C_2^*) = (c_1, c_2) \\mid M^{(b)} = m] = \\Pr[C_1^* = c_1 \\mid M = m] = 2^{-n}$。",
      "【步驟五：獨立性與優勢計算】聯合機率公式寫為：$\\Pr[(C_1^*, C_2^*) = (c_1, c_2) \\mid M^{(b)} = m] = 2^{-n} \\cdot \\mathbb{I}_{\\{c_2 = c_1 \\oplus 1^n\\}}$。此式完全不包含明文 $m$！對 $m = M^{(0)}$ 與 $m = M^{(1)}$ 數值恆等。攻擊者區分優勢嚴格為 0：$\\mathbf{Adv} = 0$，單次保密性成立。Q.E.D。"
    ],
    "algorithm": "本質剖析：雖然密文長度膨脹為兩倍，但第二部分僅是第一部分的公開位元反轉，並未引入獨立金鑰，亦未洩漏明文之內容。",
    "pitfall": "考試扣分點：需特別標明該安全性僅限於「單次加密（IND-OTS）」；若在多筆查詢（CPA）下則因確定性而立即崩潰。"
  },
  {
    "id": "proof-14",
    "category": "ch4-5",
    "chapter": "Ch. 4",
    "title": "生日悖論雜湊碰撞樣本數數學推導",
    "source": "課本 Ch. 4 / 練習一 21",
    "technique": "Taylor 級數近似 $1 - x \\approx e^{-x}$ 與機率積分",
    "target": "在大小為 $N = 2^n$ 的均勻隨機空間中，取樣 $k$ 個元素產生碰撞之機率達到 50% 時，樣本數滿足 $k \\approx \\sqrt{2 \\ln 2} \\cdot 2^{n/2} \\approx 1.177 \\times 2^{n/2}$。",
    "steps": [
      "【步驟一：無碰撞機率之連乘展開】從大小為 $N$ 的集合中獨立均勻抽取 $k$ 個元素。計算「所有 $k$ 個樣本皆互不相同（無碰撞）」之機率 $q$：\n第 1 個樣本無限制；第 2 個不可與第 1 個重複，機率為 $1 - 1/N$；第 $i$ 個不可與前 $i-1$ 個重複，機率為 $1 - (i-1)/N$。\n$q = \\prod_{i=1}^{k-1} \\left(1 - \\frac{i}{N}\\right) = \\left(1 - \\frac{1}{N}\\right)\\left(1 - \\frac{2}{N}\\right) \\cdots \\left(1 - \\frac{k-1}{N}\\right)$。",
      "【步驟二：應用 Taylor 級數指數逼近】利用 Taylor 展開不等式：當 $x \\ll 1$ 時，$1 - x \\approx e^{-x}$（或嚴格上界 $1 - x \\le e^{-x}$）。將每一項替換：$q \\approx \\prod_{i=1}^{k-1} e^{-i/N} = \\exp\\left( - \\sum_{i=1}^{k-1} \\frac{i}{N} \\right) = \\exp\\left( - \\frac{1}{N} \\sum_{i=1}^{k-1} i \\right)$。",
      "【步驟三：等差級數求和】代入等差數列求和公式 $\\sum_{i=1}^{k-1} i = \\frac{k(k-1)}{2}$，得：$q \\approx \\exp\\left( - \\frac{k(k-1)}{2N} \\right) \\approx \\exp\\left( - \\frac{k^2}{2N} \\right)$（當 $k \\gg 1$ 時 $k(k-1) \\approx k^2$）。",
      "【步驟四：建立碰撞機率方程式】至少發生一次碰撞的機率為 $p = 1 - q \\approx 1 - \\exp\\left( - \\frac{k^2}{2N} \\right)$。令碰撞機率達到 50%（$p = 1/2$）：$1 - \\exp\\left( - \\frac{k^2}{2N} \\right) = \\frac{1}{2} \\iff \\exp\\left( - \\frac{k^2}{2N} \\right) = \\frac{1}{2}$。",
      "【步驟五：對數化簡與解出樣本數 k】兩端取自然對數：$-\\frac{k^2}{2N} = \\ln\\left(\\frac{1}{2}\\right) = -\\ln 2 \\iff \\frac{k^2}{2N} = \\ln 2$。解出 $k^2$：$k^2 = 2N \\ln 2$。兩端開平方根：$k = \\sqrt{2 \\ln 2} \\cdot \\sqrt{N}$。代入 $N = 2^n$ 與常數 $\\sqrt{2 \\ln 2} \\approx \\sqrt{2 \\times 0.69315} \\approx \\sqrt{1.3863} \\approx 1.1774$：$k \\approx 1.1774 \\cdot 2^{n/2}$。Q.E.D。"
    ],
    "algorithm": "安全長度結論：欲抵禦 $2^{128}$ 次運算之生日攻擊，雜湊函數輸出位元數必須達到 $n \\ge 2 \\times 128 = 256$ 位元（如 SHA-256）。",
    "pitfall": "考試扣分點：推導中必須寫出連乘積展開式以及 $1 - x \\approx e^{-x}$ 的關鍵近似步驟，切勿直接跳到根號。"
  },
  {
    "id": "proof-15",
    "category": "ch4-5",
    "chapter": "Ch. 5",
    "title": "種子洩漏型 PRG H(S) 區分者建構與優勢計算",
    "source": "作業一 4(a)",
    "technique": "多項式時間區分者演算法與偽隨機測試",
    "target": "若 $G: \\{0,1\\}^\\lambda \\to \\{0,1\\}^{2\\lambda}$ 為安全 PRG，構造 $H(S) = A\\|B\\|C\\|D$ 其中 $A\\|B = G(S)$ 且 $C\\|D = G(B)$。證明 $H$ 不是安全 PRG。",
    "steps": [
      "【步驟一：缺陷識別與安全定義對照】PRG 的安全定義要求輸出與真隨機字串計算不可區分。構造 $H$ 之輸出為 4 個區塊 $A \\| B \\| C \\| D$（總長 $4\\lambda$）。觀察到第二區塊 $B$（長度 $\\lambda$）直接作為第二級 PRG 運算的種子輸入，且 $B$ 與其計算輸出 $C \\| D = G(B)$ 同時公開於輸出中！",
      "【步驟二：構造多項式時間區分者 D】構造區分者演算法 $D(W)$，輸入候選字串 $W \\in \\{0, 1\\}^{4\\lambda}$：\n1. 將 $W$ 解析為 4 個等長子區塊：$W = w_1 \\| w_2 \\| w_3 \\| w_4$，每塊長度 $\\lambda$。\n2. 取出第二區塊 $w_2$，本地執行 PRG 演算法：$Y := G(w_2) \\in \\{0, 1\\}^{2\\lambda}$。\n3. 檢驗關聯性：若 $Y == (w_3 \\| w_4)$ 輸出 1（判定為真實 PRG $H$）；否則輸出 0（判定為均勻隨機字串）。演算法 $D$ 僅呼叫一次 $G$，顯著為多項式時間演算法。",
      "【步驟三：在真實 PRG 分佈下之勝率分析】當 $W = H(S)$ 且 $S \\leftarrow \\{0, 1\\}^\\lambda$ 時：由構造定義，$w_2 = B$ 且 $w_3 \\| w_4 = C \\| D = G(B)$。因此 $G(w_2) = G(B) == w_3 \\| w_4$ 以機率 1 恆成立！$\\Pr_{S \\leftarrow \\{0,1\\}^\\lambda}[D(H(S)) = 1] = 1$。",
      "【步驟四：在真隨機字串分佈下之勝率分析】當 $W \\leftarrow \\{0, 1\\}^{4\\lambda}$ 為均勻隨機字串時：子區塊 $w_2$ 與 $w_3 \\| w_4$ 為相互獨立的均勻隨機字串。固定 $w_2$ 後，$G(w_2)$ 為長度 $2\\lambda$ 的固定字串。隨機字串 $w_3 \\| w_4$ 恰好命中該固定值的機率為：$\\Pr_{W \\leftarrow \\{0,1\\}^{4\\lambda}}[D(W) = 1] = \\Pr[w_3 \\| w_4 = G(w_2)] = 2^{-2\\lambda}$。",
      "【步驟五：優勢計算與證偽安全性】計算區分優勢：$\\mathbf{Adv}_H(D) = |\\Pr[D(H(S))=1] - \\Pr[D(W)=1]| = |1 - 2^{-2\\lambda}| = 1 - 2^{-2\\lambda}$。因 $1 - 2^{-2\\lambda}$ 為不可忽略的顯著數值（對 $\\lambda=128$，接近 1），區分者能以壓倒性機率破解，證明 $H$ 絕非安全 PRG。Q.E.D。"
    ],
    "algorithm": "區分者偽代碼：\n1. parse W as w1 || w2 || w3 || w4 (each lambda bits)\n2. Y = G(w2)\n3. return (Y == w3 || w4) ? 1 : 0",
    "pitfall": "考試扣分點：不可僅指出「因為 $B$ 洩漏了」；必須完整寫出區分者演算法 $D$ 的步驟並精確計算優勢差值。"
  },
  {
    "id": "proof-16",
    "category": "ch4-5",
    "chapter": "Ch. 5",
    "title": "PRG 串接反饋構造安全性分類證明",
    "source": "課本 Exercise 5.21 / 練習一 30",
    "technique": "狀態隱藏混淆論證（Hybrid Argument on Hidden State）",
    "target": "分析由倍長 PRG $G$ 構建之反饋型構造：若中間狀態保持私密則安全；若狀態公開洩漏則不安全。",
    "steps": [
      "【步驟一：構造模型界定】設 $G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{2\\lambda}$ 為安全 PRG。考慮迭代反饋構造：初始化狀態 $s_0 = S$；第 $i$ 輪計算 $s_i \\| t_i = G(s_{i-1})$，其中 $s_i$ 為新狀態，$t_i$ 為輸出塊。",
      "【步驟二：構造 A（狀態私密，標準串流展開）安全性證明】若方案輸出僅為 $t_1 \\| t_2 \\| \\dots \\| t_n$，且所有中間狀態 $s_i$ 皆嚴格保密。\n構造 Hybrid 遊戲序列 $H_0, H_1, \\dots, H_n$：在 $H_i$ 中，前 $i$ 輪之 $(s_j, t_j)$ 皆由真隨機字串替換。\n由 $G$ 之 PRG 安全性，相鄰遊戲之區分優勢滿足 $|\\Pr[D(H_{i-1})=1] - \\Pr[D(H_i)=1]| \\le \\mathbf{Adv}_G(\\mathcal{B}_i)$。\n根據三角不等式，總區分優勢為：$\\mathbf{Adv}_A \\le \\sum_{i=1}^n \\mathbf{Adv}_G(\\mathcal{B}_i) \\le n \\cdot \\mathbf{Adv}_G$。因 $n$ 為多項式大小，優勢依然為可忽略函數，判定構造 A 為安全 PRG。",
      "【步驟三：構造 B（狀態洩漏）缺陷分析】若構造在輸出中暴露中間狀態，例如輸出序列為 $s_1 \\| t_1 \\| s_2 \\| t_2$。\n攻擊者直接取得相鄰兩輪的公開值：第一輪狀態 $s_1$ 與第二輪輸出 $s_2 \\| t_2$。",
      "【步驟四：構造 B 之區分者設計與優勢】構造區分者 $D(W)$：計算 $G(s_1)$ 並比對是否等於 $s_2 \\| t_2$。\n在真實構造下，等式以機率 1 成立；在真隨機字串下，成立機率僅為 $2^{-2\\lambda}$。\n區分優勢為 $\\mathbf{Adv}_B = 1 - 2^{-2\\lambda} \\approx 1$。判定構造 B 不安全。Q.E.D。"
    ],
    "algorithm": "核心準則：密碼學 PRG 迭代之黃金鐵律在於「內部狀態轉移必須絕對黑箱保密，僅能公開非線性萃取之輸出位元」。",
    "pitfall": "考試扣分點：答題時須先明確指出題目所提構造究竟有無隱藏中間狀態，分情況討論證明或給出攻擊。"
  },
  {
    "id": "proof-17",
    "category": "ch6-7",
    "chapter": "Ch. 6",
    "title": "線性構造 PRF 差分破壞與區分優勢計算",
    "source": "作業一 4(b)",
    "technique": "線性差分不變量（Linear Differential Invariant）破譯",
    "target": "設 $G$ 為安全 PRG。構造 $F(K, X) = G(K) \\oplus X$。證明 $F$ 絕非安全 PRF。",
    "steps": [
      "【步驟一：線性差分不變量識別】分析候選 PRF $F: \\{0, 1\\}^n \\times \\{0, 1\\}^n \\to \\{0, 1\\}^n$。任選兩筆相異輸入 $X_1, X_2$，計算兩輸出之 XOR 差分：\n$F(K, X_1) \\oplus F(K, X_2) = (G(K) \\oplus X_1) \\oplus (G(K) \\oplus X_2) = (G(K) \\oplus G(K)) \\oplus (X_1 \\oplus X_2) = 0^n \\oplus (X_1 \\oplus X_2) = X_1 \\oplus X_2$。\n密鑰項 $G(K)$ 完全消除！輸出差分恆等於輸入差分，具有確定性不變量。",
      "【步驟二：構造多項式時間區分者演算法 D】區分者 $D$ 能向黑箱預言機 $\\mathcal{O}$ 進行查詢：\n1. 查詢 Oracle 輸入 $X_1 = 0^n$，獲取輸出 $Y_1 := \\mathcal{O}(0^n)$。\n2. 查詢 Oracle 輸入 $X_2 = 1^n$，獲取輸出 $Y_2 := \\mathcal{O}(1^n)$。\n3. 比對輸出差分：若 $Y_1 \\oplus Y_2 == 1^n$ 輸出 1（判定為真實 PRF $F$）；否則輸出 0（判定為真隨機函數 $\\mathcal{R}$）。",
      "【步驟三：在真實 PRF 下之條件機率】若預言機為真實 PRF（$\\mathcal{O} = F_K$）：$Y_1 \\oplus Y_2 = F(K, 0^n) \\oplus F(K, 1^n) = 0^n \\oplus 1^n = 1^n$ 恆成立。因此：$\\Pr[D^{F_K} = 1] = 1$。",
      "【步驟四：在真隨機函數下之條件機率】若預言機為真隨機函數（$\\mathcal{O} = \\mathcal{R}$）：因輸入 $0^n \\neq 1^n$，其輸出 $Y_1 = \\mathcal{R}(0^n)$ 與 $Y_2 = \\mathcal{R}(1^n)$ 為獨立均勻選取的隨機字串。兩獨立隨機字串之 XOR 等於固定值 $1^n$ 的機率為：$\\Pr[D^{\\mathcal{R}} = 1] = \\Pr[Y_1 \\oplus Y_2 = 1^n] = 2^{-n}$。",
      "【步驟五：優勢計算與結論】區分優勢為：$\\mathbf{Adv}_F^{\\text{prf}}(D) = |\\Pr[D^{F_K} = 1] - \\Pr[D^{\\mathcal{R}} = 1]| = |1 - 2^{-n}| = 1 - 2^{-n} \\approx 1$。優勢不可忽略，證明 $F$ 不是安全 PRF。Q.E.D。"
    ],
    "algorithm": "區分者代碼：\n1. Y1 = Oracle(0^n)\n2. Y2 = Oracle(1^n)\n3. return (Y1 ^ Y2 == 1^n) ? 1 : 0",
    "pitfall": "考試扣分點：切勿誤認「因為 $G(K)$ 是隨機字串，所以加了 $X$ 依然隨機」。PRF 考核的是多次查詢之間的函數映射結構，而非單次輸出的隨機性。"
  },
  {
    "id": "proof-18",
    "category": "ch6-7",
    "chapter": "Ch. 6",
    "title": "歸零輸入破壞 PRF 偽隨機性證明",
    "source": "課本 Exercise 6.9 / 練習一 31",
    "technique": "單查詢零點漏洞（Single-query Zero Defect）",
    "target": "設 $F$ 為安全 PRF。構造 $H(K, X) = F(K, X) \\oplus F(K, 0^n)$。證明 $H$ 不是安全 PRF。",
    "steps": [
      "【步驟一：零點結構退化分析】檢視輸入為全零字串 $X = 0^n$ 時函數 $H$ 之輸出：$H(K, 0^n) = F(K, 0^n) \\oplus F(K, 0^n) = 0^m$。無論金鑰 $K$ 取值為何，全零輸入之輸出恆為全零字串，完全失去隨機性。",
      "【步驟二：構造單次查詢區分者 D】構造區分者 $D^{\\mathcal{O}}$：\n1. 僅需向預言機發起 1 次查詢：查詢 $X = 0^n$，取得輸出 $Y := \\mathcal{O}(0^n)$。\n2. 檢驗：若 $Y == 0^m$ 輸出 1；否則輸出 0。",
      "【步驟三：在真實構造 H 下之勝率】當 $\\mathcal{O} = H_K$ 時：$Y = H(K, 0^n) = 0^m$ 恆成立，故 $\\Pr[D^{H_K} = 1] = 1$。",
      "【步驟四：在真隨機函數 R 下之勝率】當 $\\mathcal{O} = \\mathcal{R}$ 為真隨機函數時：$\\mathcal{R}(0^n)$ 均勻分佈於 $\\{0, 1\\}^m$，輸出剛好為 $0^m$ 的機率為 $2^{-m}$：$\\Pr[D^{\\mathcal{R}} = 1] = 2^{-m}$。",
      "【步驟五：優勢計算】區分優勢為：$\\mathbf{Adv}_H^{\\text{prf}}(D) = |1 - 2^{-m}| = 1 - 2^{-m} \\approx 1$。單次查詢即可徹底攻破。Q.E.D。"
    ],
    "algorithm": "區分者偽代碼：\n1. Y = Oracle(0^n)\n2. return (Y == 0^m) ? 1 : 0",
    "pitfall": "考試扣分點：只需 1 次查詢即可打破，優勢計算為 $1 - 2^{-m}$。"
  },
  {
    "id": "proof-19",
    "category": "ch6-7",
    "chapter": "Ch. 6-7",
    "title": "PRF 與 PRP 切換引理（Switching Lemma）推導",
    "source": "課本 Lemma 7.7 / 練習一 23",
    "technique": "差異引理（Difference Lemma）與生日碰撞界限",
    "target": "對於向 Oracle 進行 $q$ 次查詢的任意多項式時間區分者 $D$，真隨機置換（PRP）與真隨機函數（PRF）之間的區分優勢受限於生日碰撞機率：$|\\Pr[D^{\\text{Perm}}=1] - \\Pr[D^{\\text{Func}}=1]| \\le \\frac{q(q-1)}{2 \\cdot 2^n} \\le \\frac{q^2}{2^{n+1}}$。",
    "steps": [
      "【步驟一：定義隨機置換與隨機函數模型】\n- $\\text{Func}: \\{0, 1\\}^n \\to \\{0, 1\\}^n$ 為全體函數中均勻選取之真隨機函數（有放回抽樣）。\n- $\\text{Perm}: \\{0, 1\\}^n \\to \\{0, 1\\}^n$ 為全體雙射置換中均勻選取之真隨機置換（無放回抽樣）。",
      "【步驟二：引入碰撞壞事件 Coll】區分者發起 $q$ 次兩兩相異的查詢 $X_1, X_2, \\dots, X_q$。定義事件 $\\text{Coll}$：在對 $\\text{Func}$ 的查詢中，輸出出現碰撞，即 $\\exists 1 \\le i < j \\le q$ 使得 $\\text{Func}(X_i) = \\text{Func}(X_j)$。",
      "【步驟三：應用差異引理（Difference Lemma）】若事件 $\\text{Coll}$ 未發生（$\\neg\\text{Coll}$），則 $\\text{Func}$ 對 $q$ 次相異輸入產生了 $q$ 個兩兩相異的均勻隨機輸出。這與無放回抽樣的真隨機置換 $\\text{Perm}$ 在這 $q$ 個點上的條件聯合機率分佈完全恆等！根據差異引理：$|\\Pr[D^{\\text{Perm}}=1] - \\Pr[D^{\\text{Func}}=1]| \\le \\Pr[\\text{Coll}]$。",
      "【步驟四：計算生日碰撞機率上限（Union Bound）】總共有 $\\binom{q}{2} = \\frac{q(q-1)}{2}$ 個查詢對。對任一對 $i < j$，因 $\\text{Func}$ 均勻獨立，$\\Pr[\\text{Func}(X_i) = \\text{Func}(X_j)] = 2^{-n}$。應用聯集上界（Union Bound）：$\\Pr[\\text{Coll}] \\le \\sum_{1 \\le i < j \\le q} \\Pr[\\text{Func}(X_i) = \\text{Func}(X_j)] = \\frac{q(q-1)}{2} \\cdot \\frac{1}{2^n} = \\frac{q(q-1)}{2 \\cdot 2^n} < \\frac{q^2}{2^{n+1}}$。",
      "【步驟五：得出結論】兩函式庫之區分優勢上限為：$\\mathbf{Adv} \\le \\frac{q^2}{2^{n+1}}$。當 $q \\ll 2^{n/2}$ 時，置換與函數無法區分。Q.E.D。"
    ],
    "algorithm": "結論：當查詢次數 $q \\ll 2^{n/2}$ 時，任何置換（如 AES）皆可安全地被視為真隨機函數（PRF）。",
    "pitfall": "考試扣分點：必須點出在「碰撞未發生前，兩者輸出完全不可區分」這一關鍵前提。"
  },
  {
    "id": "proof-20",
    "category": "ch6-7",
    "chapter": "Ch. 7",
    "title": "Feistel 網路結構可逆性代數推導",
    "source": "課本 Ch. 7 / 練習一 8",
    "technique": "對稱代數結構與逆輪變換推導",
    "target": "證明不論輪函數 $F$ 是否可逆，Feistel 網路之每輪變換皆為可逆雙射，且解密演算法與加密演算法結構完全對稱。",
    "steps": [
      "【步驟一：正向加密輪函數定義】第 $i$ 輪輸入為 $(L_{i-1}, R_{i-1})$，輸出為 $(L_i, R_i)$。正向公式：\n$L_i = R_{i-1}$\n$R_i = L_{i-1} \\oplus F(K_i, R_{i-1})$。",
      "【步驟二：逆向解密目標設定】解密端已知第 $i$ 輪輸出 $(L_i, R_i)$ 與子金鑰 $K_i$，目標為唯一還原上一輪之輸入 $(L_{i-1}, R_{i-1})$。",
      "【步驟三：還原上一輪右半部 R_{i-1}】由正向公式第 1 式直接可得：$R_{i-1} = L_i$。解密端直接取當前左半部作為前一輪右半部，完全無需任何計算。",
      "【步驟四：還原上一輪左半部 L_{i-1}】已知 $R_{i-1} = L_i$，將其輸入輪函數計算 $F(K_i, L_i) = F(K_i, R_{i-1})$。將此值與當前右半部 $R_i$ 進行 XOR 運算：\n$R_i \\oplus F(K_i, L_i) = (L_{i-1} \\oplus F(K_i, R_{i-1})) \\oplus F(K_i, R_{i-1})$。\n利用 XOR 運算之自反性（$A \\oplus B \\oplus B = A$）：\n$R_i \\oplus F(K_i, L_i) = L_{i-1} \\oplus (F(K_i, R_{i-1}) \\oplus F(K_i, R_{i-1})) = L_{i-1} \\oplus 0 = L_{i-1}$。左半部精確還原！",
      "【步驟五：輪函數不可逆之獨立性結論】整個求逆推導完全依賴 XOR 運算自我抵消，從未對輪函數 $F$ 進行任何求逆運算。因此，無論輪函數 $F$ 為不可逆函數、多對一函數或單向雜湊函數，Feistel 網絡之每輪變換皆嚴格可逆。解密演算法僅需將金鑰以反向順序代入相同電路。Q.E.D。"
    ],
    "algorithm": "架構優勢：允許密碼設計者在輪函數 $F$ 中任意使用單向不可逆組件（如 S-Box、Hash、非對稱壓縮映射）。",
    "pitfall": "考試扣分點：切勿回答「因為輪函數 $F$ 可逆」；Feistel 的核心精髓恰恰在於輪函數不需可逆。"
  },
  {
    "id": "proof-21",
    "category": "ch6-7",
    "chapter": "Ch. 7",
    "title": "2 輪 Feistel 差分不變量破壞法形式證明",
    "source": "課本 Exercise 7.3 / 練習一 9",
    "technique": "差分消除不變量（Differential Invariant）破壞",
    "target": "證明 2 輪 Feistel 網路無法抵抗選擇明文攻擊，可在常數次查詢內被完全區分（非安全 PRP）。",
    "steps": [
      "【步驟一：推導 2 輪 Feistel 之輸出公式】輸入明文為 $P = (L_0, R_0)$。\n第 1 輪輸出：$L_1 = R_0$, $R_1 = L_0 \\oplus F(K_1, R_0)$。\n第 2 輪輸出：$L_2 = R_1 = L_0 \\oplus F(K_1, R_0)$；$R_2 = L_1 \\oplus F(K_2, R_1) = R_0 \\oplus F(K_2, L_2)$。",
      "【步驟二：挑選共享右半部之相異明文對】選取兩筆相異明文 $P = (L_0, R_0)$ 與 $P' = (L'_0, R_0)$，滿足右半部相同（$R_0 = R'_0$）而左半部相異（$L_0 \\neq L'_0$）。",
      "【步驟三：計算密文左半部差分】將兩明文分別代入第 2 輪左半部公式：\n$L_2 = L_0 \\oplus F(K_1, R_0)$\n$L'_2 = L'_0 \\oplus F(K_1, R_0)$。\n計算差分：$L_2 \\oplus L'_2 = (L_0 \\oplus F(K_1, R_0)) \\oplus (L'_0 \\oplus F(K_1, R_0)) = L_0 \\oplus L'_0$。輪函數項 $F(K_1, R_0)$ 徹底抵消！輸出左半部差分嚴格等於輸入左半部差分。",
      "【步驟四：構造區分者 D】\n1. 查詢明文 $P = (0^w, 0^w)$ 得到密文 $(L_2, R_2)$。\n2. 查詢明文 $P' = (1^w, 0^w)$ 得到密文 $(L'_2, R'_2)$。\n3. 比對：若 $L_2 \\oplus L'_2 == 1^w$ 輸出 1；否則輸出 0。",
      "【步驟五：優勢計算】在真實 2 輪 Feistel 下，$L_2 \\oplus L'_2 = 0^w \\oplus 1^w = 1^w$ 恆成立，勝率為 1。在真隨機置換下，輸出兩半部為隨機數，差分等於 $1^w$ 的機率為 $2^{-w}$。區分優勢 $\\mathbf{Adv} = 1 - 2^{-w} \\approx 1$。2 輪 Feistel 被徹底破解。Q.E.D。"
    ],
    "algorithm": "區分者演算法：\n1. 查詢 P = (0, 0) 得 (L2, R2)\n2. 查詢 P' = (1, 0) 得 (L'2, R'2)\n3. 檢驗：若 L2 ^ L'2 == 1 輸出 1 (判定為 2-round Feistel)；否則輸出 0。優勢為 1 - 2^(-w)。",
    "pitfall": "考試扣分點：記住差分關係發生的條件是「輸入明文共享相同的右半部（$R_0 = R'_0$）」。"
  },
  {
    "id": "proof-22",
    "category": "ch6-7",
    "chapter": "Ch. 7",
    "title": "線性輪函數 Feistel 任意輪數必破證明",
    "source": "課本 Exercise 7.4 / 練習一 32",
    "technique": "仿射線性空間差分守恆（Affine Linear Invariant）",
    "target": "若 Feistel 輪函數為線性構造 $F(K_i, X) = K_i \\oplus X$，證明無論迭代多少輪，該密碼皆非安全 PRP。",
    "steps": [
      "【步驟一：線性輪函數代數矩陣化】輪函數 $F(K_i, X) = X \\oplus K_i$ 在向量空間 $\\mathbb{F}_2^w$ 上為仿射線性映射。Feistel 每輪變換可精確表示為矩陣乘法與金鑰向量相加：\n$\\begin{pmatrix} L_i \\\\ R_i \\end{pmatrix} = \\begin{pmatrix} 0 & I \\\\ I & I \\end{pmatrix} \\begin{pmatrix} L_{i-1} \\\\ R_{i-1} \\end{pmatrix} \\oplus \\begin{pmatrix} 0 \\\\ K_i \\end{pmatrix}$。",
      "【步驟二：複合 r 輪依然為仿射線性變換】有限維向量空間上仿射線性變換的複合依然為仿射線性變換。迭代 $r$ 輪後，密文向量可寫為：$\\begin{pmatrix} L_r \\\\ R_r \\end{pmatrix} = \\mathbf{A}_r \\begin{pmatrix} L_0 \\\\ R_0 \\end{pmatrix} \\oplus \\mathbf{B}_r(K_1, \\dots, K_r)$，其中矩陣 $\\mathbf{A}_r$ 僅由常數矩陣連乘決定（公開已知且可逆），$\\mathbf{B}_r$ 為金鑰的線性組合向量。",
      "【步驟三：構造 4 點差分抵消空間】任選 3 筆相異明文 $P_1, P_2, P_3$，定義第 4 筆明文為前三者之 XOR 和：$P_4 = P_1 \\oplus P_2 \\oplus P_3$。由此保證 $P_1 \\oplus P_2 \\oplus P_3 \\oplus P_4 = 0^{2w}$。",
      "【步驟四：計算 4 筆密文之 XOR 總和】將 4 筆明文送入加密獲得密文 $C_1, C_2, C_3, C_4$。計算總和：\n$\\bigoplus_{i=1}^4 C_i = \\bigoplus_{i=1}^4 (\\mathbf{A}_r P_i \\oplus \\mathbf{B}_r) = \\mathbf{A}_r \\left( \\bigoplus_{i=1}^4 P_i \\right) \\oplus (\\mathbf{B}_r \\oplus \\mathbf{B}_r \\oplus \\mathbf{B}_r \\oplus \\mathbf{B}_r) = \\mathbf{A}_r(0^{2w}) \\oplus 0^{2w} = 0^{2w}$。金鑰向量 $\\mathbf{B}_r$ 徹底相消，4 筆密文的 XOR 和恆等於 0！",
      "【步驟五：區分優勢計算】構造區分者：查詢此 4 筆明文，檢驗 $\\bigoplus_{i=1}^4 C_i == 0$。在真實線性 Feistel 下機率為 1；在真隨機置換下，4 個輸出滿足 XOR 為 0 的機率為 $2^{-2w}$。優勢 $\\mathbf{Adv} = 1 - 2^{-2w} \\approx 1$。任意輪數皆不具偽隨機性。Q.E.D。"
    ],
    "algorithm": "4 點差分區分者：選取任意 $P_1, P_2, P_3$，設定 $P_4 = P_1 \\oplus P_2 \\oplus P_3$。查詢 4 筆密文。若 $C_1 \\oplus C_2 \\oplus C_3 \\oplus C_4 == 0$ 輸出 1；否則輸出 0。優勢達 $1 - 2^{-2w} \\approx 1$。",
    "pitfall": "考試扣分點：證明核心在於線性函數之組合依然為線性函數，疊加再多輪亦無法產生任何密碼學非線性度（混淆度 S-Box）。"
  },
  {
    "id": "proof-23",
    "category": "ch8",
    "chapter": "Ch. 8",
    "title": "決定性加密無狀態下必破 IND-CPA 形式反證法",
    "source": "課本 Theorem 8.5 / 投影片 1.5 Section 1 / 練習一 24",
    "technique": "CPA 重複查詢博弈與相等性檢測",
    "target": "任何無狀態（Stateless）且具備解密正確性的確定性加密方案（Deterministic Encryption），絕不可能達成 IND-CPA 安全性。",
    "steps": [
      "【步驟一：確定性與無狀態加密定義】無狀態確定性加密演算法之定義為：對固定金鑰 $K$，演算法為數學函數 $\\text{Enc}: \\mathcal{K} \\times \\mathcal{M} \\to \\mathcal{C}$。對相同明文輸入 $M$，在不同時間呼叫 $\\text{Enc}(K, M)$ 恆輸出完全相同之密文 $C$。",
      "【步驟二：構造 CPA 攻擊者演算法 A】構造攻擊者 $\\mathcal{A}$，利用 CPA 提供之加密預言機 $\\text{Enc}(K, \\cdot)$：\n1. 挑選兩筆相異明文 $M_0, M_1 \\in \\mathcal{M}$（$M_0 \\neq M_1$）。\n2. 呼叫加密預言機查詢明文 $M_0$，獲得密文存為 $C_0 := \\text{Enc}(K, M_0)$。\n3. 向挑戰預言機提交挑戰對 $(M_0, M_1)$，獲得挑戰密文 $C^* = \\text{Enc}(K, M_b)$。\n4. 比對：若 $C^* == C_0$ 輸出 0；否則輸出 1。",
      "【步驟三：挑戰位元 b = 0 之勝率分析】若挑戰位元為 $b = 0$，則挑戰密文為 $C^* = \\text{Enc}(K, M_0)$。由確定性無狀態性質，兩次查詢輸入皆為 $M_0$，密文必定嚴格相等：$C^* = C_0$。因此攻擊者必輸出 0：$\\Pr[\\mathcal{A} \\to 0 \\mid b = 0] = 1$。",
      "【步驟四：挑戰位元 b = 1 之勝率分析】若挑戰位元為 $b = 1$，則挑戰密文為 $C^* = \\text{Enc}(K, M_1)$。由解密正確性公理 $\\text{Dec}(K, \\text{Enc}(K, M)) = M$，若 $C^* = C_0$，則解密將得出 $M_1 = \\text{Dec}(K, C^*) = \\text{Dec}(K, C_0) = M_0$，這與 $M_0 \\neq M_1$ 產生矛盾！因此必定有 $C^* \\neq C_0$。攻擊者必輸出 1：$\\Pr[\\mathcal{A} \\to 0 \\mid b = 1] = 0$。",
      "【步驟五：優勢計算與定理成立】CPA 區分優勢為：$\\mathbf{Adv}_{\\text{cpa}} = |\\Pr[\\mathcal{A} \\to 0 \\mid b = 0] - \\Pr[\\mathcal{A} \\to 0 \\mid b = 1]| = |1 - 0| = 1$。優勢高達 1，證明確定性無狀態加密絕對無法達成 CPA 安全。Q.E.D。"
    ],
    "algorithm": "推論：所有達成 CPA 安全的對稱加密系統必須具備隨機性（如隨機 IV）或內部狀態（如不重複計數器）。",
    "pitfall": "考試扣分點：必須強調攻擊者能在發起挑戰前後任意呼叫加密 Oracle，這是 CPA 相較於 OTS 的本質威力。"
  },
  {
    "id": "proof-24",
    "category": "ch8",
    "chapter": "Ch. 8",
    "title": "|M| = |C| 且具正確性之方案必破 CPA 證明",
    "source": "課本 Exercise 8.11 / 練習一 33",
    "technique": "有限集單射即雙射引理與確定性必然性",
    "target": "若加密方案滿足解密正確性且明文空間大小等於密文空間大小（$|\\mathcal{M}| = |\\mathcal{C}|$），則該方案絕不可能達成 CPA 安全。",
    "steps": [
      "【步驟一：解密正確性要求單射性】由正確性條件：$\\forall K, \\text{Dec}(K, \\text{Enc}(K, M)) = M$。這要求對固定金鑰 $K$，映射 $f_K(M) = \\text{Enc}(K, M)$ 必須為單射（Injective）。否則若存在 $M_1 \\neq M_2$ 使得 $\\text{Enc}(K, M_1) = \\text{Enc}(K, M_2) = C$，解密 $\\text{Dec}(K, C)$ 將無法同時還原 $M_1$ 與 $M_2$，破壞正確性。",
      "【步驟二：有限集單射必為雙射引理】由題目條件，明文空間與密文空間為同等基數之有限集：$|\\mathcal{M}| = |\\mathcal{C}| < \\infty$。根據有限集合論基本定理：有限集到等大有限集的單射映射必定為滿射（Surjective），從而必為雙射（Bijective）。",
      "【步驟三：雙射排斥演算法內部隨機性】因為映射為雙射，每個明文 $M$ 在密文空間中存在且僅存在一個合法的對應密文 $C$。若加密演算法消耗了 $r$ 個隨機位元，則每筆明文將對應至少 $2^r$ 個可能密文，這將導致密文空間大小必須滿足 $|\\mathcal{C}| \\ge 2^r |\\mathcal{M}| > |\\mathcal{M}|$，與前提 $|\\mathcal{M}| = |\\mathcal{C}|$ 矛盾！因此，該方案絕不可能包含隨機性，必定為確定性演算法（Deterministic）。",
      "【步驟四：引用確定性必破 CPA 定理】由步驟三證明方案為確定性無狀態加密，直接引用「決定性加密無狀態下必破 IND-CPA 定理」，攻擊者可透過預先查詢明文 $M_0$ 獲得密文進行比對，取得優勢 $\\mathbf{Adv} = 1$。因此該方案絕不可能達成 CPA 安全。Q.E.D。"
    ],
    "algorithm": "結論：任何 CPA 安全的加密方案密文長度必須嚴格大於明文長度（$|\\mathcal{C}| > |\\mathcal{M}|$），必須攜帶隨機鹽（IV 或 Nonce）。",
    "pitfall": "考試扣分點：核心在於引用「有限集上單射必為雙射」，進而導出演算法無隨機擴展空間的確定性必然性。"
  },
  {
    "id": "proof-25",
    "category": "ch8",
    "chapter": "Ch. 8",
    "title": "隨機化 PRF 加密方案之 IND-CPA 形式證明",
    "source": "課本 Theorem 8.6 / 作業一 5(a)-i",
    "technique": "PRF 歸約（Reduction to PRF）與生日界限差異引理",
    "target": "設 $F$ 為安全 PRF。證明隨機化加密方案 $\\text{Enc}(K, M) = (R, F(K, R) \\oplus M)$（其中 $R \\leftarrow \\{0,1\\}^\\lambda$）達成 IND-CPA 安全性。",
    "steps": [
      "【步驟一：建立 Game 0（真實 CPA 博弈）】在 Game 0 中，挑戰者使用真實 PRF $F(K, \\cdot)$ 回應攻擊者的 $q$ 次加密查詢及 1 次挑戰查詢。攻擊者猜對勝率記為 $\\Pr[\\text{Win}_0]$。",
      "【步驟二：建立 Game 1（理想隨機函數替換）】在 Game 1 中，挑戰者將 PRF $F(K, \\cdot)$ 替換為真正的真隨機函數 $\\mathcal{R}: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^m$。構造歸約演算法 $\\mathcal{B}$：若存在攻擊者能區分 Game 0 與 Game 1，則 $\\mathcal{B}$ 可攻破 PRF $F$。由 PRF 安全性：$|\\Pr[\\text{Win}_0] - \\Pr[\\text{Win}_1]| \\le \\mathbf{Adv}_F^{\\text{prf}}(\\mathcal{B})$。",
      "【步驟三：定義隨機數碰撞壞事件 Coll】在 Game 1 中，每次加密獨立隨機抽取 $R \\leftarrow \\{0, 1\\}^\\lambda$。令總查詢次數為 $q+1$（含挑戰查詢）。定義壞事件 $\\text{Coll}$：在所有查詢中，至少存在兩次查詢抽中了相同的隨機數 $R$。",
      "【步驟四：生日界限計算碰撞機率】在長度為 $\\lambda$ 的空間中抽樣 $q+1$ 次，根據生日界限（Birthday Bound）：$\\Pr[\\text{Coll}] \\le \\frac{(q+1)q}{2 \\cdot 2^\\lambda} \\le \\frac{(q+1)^2}{2^{\\lambda+1}}$。",
      "【步驟五：未碰撞下真隨機函數之 OTP 完善保密性】在事件 $\\neg\\text{Coll}$ 發生時，挑戰查詢所使用的隨機數 $R^*$ 從未在任何其他查詢中出現過。真隨機函數 $\\mathcal{R}$ 在新點 $R^*$ 上的輸出 $\\mathcal{R}(R^*)$ 為嚴格均勻隨機字串，等價於一次性密碼本（OTP）！挑戰密文 $C^* = \\mathcal{R}(R^*) \\oplus M_b$ 具備完善保密性，攻擊者猜對機率嚴格為 $1/2$：$\\Pr[\\text{Win}_1 \\mid \\neg\\text{Coll}] = \\frac{1}{2}$。",
      "【步驟六：應用差異引理得出最終優勢界限】根據差異引理（Difference Lemma）：$|\\Pr[\\text{Win}_1] - 1/2| \\le \\Pr[\\text{Coll}]$。結合步驟二與步驟四：$\\mathbf{Adv}_{\\text{cpa}} = 2 |\\Pr[\\text{Win}_0] - 1/2| \\le 2 \\cdot \\mathbf{Adv}_F^{\\text{prf}}(\\mathcal{B}) + 2\\Pr[\\text{Coll}] \\le 2 \\cdot \\mathbf{Adv}_F^{\\text{prf}}(\\mathcal{B}) + \\frac{(q+1)^2}{2^\\lambda}$。因 PRF 優勢與生日碰撞項皆為可忽略函數，方案達成 IND-CPA 安全。Q.E.D。"
    ],
    "algorithm": "碰撞分析：只要查詢次數 $q \\ll 2^{\\lambda/2}$，方案即可提供堅不可摧的語義安全性。",
    "pitfall": "考試扣分點：證明中切勿忘記考慮隨機數 $R$ 在生日界限下的碰撞機率項 $\\frac{(q+1)^2}{2^\\lambda}$。"
  },
  {
    "id": "proof-26",
    "category": "ch8",
    "chapter": "Ch. 8",
    "title": "外部隨機數消去破壞 CPA 之區分者建構",
    "source": "作業一 5(a)-ii",
    "technique": "線性代數抵消破壞隨機化",
    "target": "若 $\\text{Enc}(K, M) = (R, F(K, M) \\oplus R)$，其中 $R \\leftarrow \\{0,1\\}^\\lambda$ 均勻隨機且 $F$ 為安全 PRF。證明此方案無法達成 CPA 安全。",
    "steps": [
      "【步驟一：密文結構破綻分析】密文包含兩分量 $(C_1, C_2) = (R, F(K, M) \\oplus R)$。隨機數 $R$ 雖然是均勻隨機抽取，但其並未傳入 PRF 內部作為非線性種子，而是直接外加在最外層與 PRF 評估值進行 XOR。",
      "【步驟二：線性差分消除隨機數】計算兩密文分量之 XOR 和：$C_1 \\oplus C_2 = R \\oplus (F(K, M) \\oplus R) = (R \\oplus R) \\oplus F(K, M) = 0^\\lambda \\oplus F(K, M) = F(K, M)$。隨機數 $R$ 被完全抵消！密文對直接洩漏了決定性的 PRF 評估值 $F(K, M)$。",
      "【步驟三：構造 CPA 攻擊者 A】構造攻擊者演算法 $\\mathcal{A}$：\n1. 挑選挑戰明文對：$M_0 = 0^n, M_1 = 1^n$，送入挑戰預言機，獲得挑戰密文 $(C_1^*, C_2^*)$。\n2. 計算挑戰特徵值：$V^* = C_1^* \\oplus C_2^* = F(K, M_b)$。\n3. 向加密預言機查詢明文 $M_0$，獲得密文 $(C_1', C_2')$。\n4. 計算查詢特徵值：$V' = C_1' \\oplus C_2' = F(K, M_0)$。\n5. 比對判定：若 $V^* == V'$ 輸出 0；否則輸出 1。",
      "【步驟四：勝率與優勢計算】\n- 若 $b = 0$：$V^* = F(K, M_0) = V'$ 恆成立，$\\Pr[\\mathcal{A} \\to 0 \\mid b = 0] = 1$。\n- 若 $b = 1$：$V^* = F(K, M_1)$ 與 $V' = F(K, M_0)$。由 PRF 安全性，$F$ 在兩相異點上碰撞的機率為可忽略函數 $2^{-\\lambda}$，故 $\\Pr[\\mathcal{A} \\to 0 \\mid b = 1] = 2^{-\\lambda}$。\n區分優勢 $\\mathbf{Adv} = |1 - 2^{-\\lambda}| \\approx 1$。方案在 CPA 下徹底崩潰。Q.E.D。"
    ],
    "algorithm": "區分者代碼：\n1. (C1*, C2*) = Challenge(M0, M1)\n2. (C1', C2') = Encrypt(M0)\n3. return ((C1* ^ C2*) == (C1' ^ C2')) ? 0 : 1",
    "pitfall": "考試扣分點：隨機數 $R$ 必須作為 PRF 的輸入引數（如 $F(K, R) \\oplus M$），若置於 PRF 外部會被線性差分直接抹除。"
  },
  {
    "id": "proof-27",
    "category": "ch8",
    "chapter": "Ch. 8",
    "title": "CBC 模式可預測 IV 之 BEAST 攻擊形式證明",
    "source": "投影片 1.5 Section 1 / 考點變化題 5",
    "technique": "已知差分預補償（Difference Pre-compensation）破壞 IND-CPA",
    "target": "若 CBC 模式採用可預測的 IV（例如計數器或下一輪已知 IV），則該 CBC 模式無法達成 IND-CPA 安全性。",
    "steps": [
      "【步驟一：CBC 模式加密方程分析】標準 CBC 模式加密單區塊之公式為：$C_1 = \\text{AES}_K(IV \\oplus M)$。方案要求 IV 必須均勻且在明文確定前不可預測，以扮演隨機遮罩的角色。",
      "【步驟二：可預測 IV 漏洞模型】假設實作缺陷：攻擊者在發起下一次加密查詢前，能預先獲知下一次加密將採用的初始向量，記為 $IV_{\\text{next}}$（例如前一筆密文的最後一塊，或自增計數器）。",
      "【步驟三：構造 BEAST 選擇明文攻擊演算法】\n1. 攻擊者挑選兩筆挑戰明文 $M_0, M_1 \\in \\{0, 1\\}^{128}$ 提交給挑戰預言機，獲得挑戰密文 $(IV^*, C_1^*)$，其中 $C_1^* = \\text{AES}_K(IV^* \\oplus M_b)$。\n2. 攻擊者預測下一次加密之向量 $IV_{\\text{next}}$。\n3. 構造特定差分預補償明文：$M_{\\text{query}} = IV_{\\text{next}} \\oplus IV^* \\oplus M_0$。\n4. 將 $M_{\\text{query}}$ 提交給加密預言機。系統使用 $IV_{\\text{next}}$ 進行加密，計算第一塊密文：\n   $C_{\\text{query}} = \\text{AES}_K(IV_{\\text{next}} \\oplus M_{\\text{query}}) = \\text{AES}_K(IV_{\\text{next}} \\oplus (IV_{\\text{next}} \\oplus IV^* \\oplus M_0)) = \\text{AES}_K(0^{128} \\oplus IV^* \\oplus M_0) = \\text{AES}_K(IV^* \\oplus M_0)$！\n5. 比對密文：若 $C_{\\text{query}} == C_1^*$ 輸出 0（判定 $b=0$）；否則輸出 1（判定 $b=1$）。",
      "【步驟四：優勢計算】\n- 若 $b = 0$：$C_1^* = \\text{AES}_K(IV^* \\oplus M_0) = C_{\\text{query}}$ 恆成立，$\\Pr[\\mathcal{A} \\to 0 \\mid b = 0] = 1$。\n- 若 $b = 1$：$C_1^* = \\text{AES}_K(IV^* \\oplus M_1)$。因 AES 為置換，$C_1^* = C_{\\text{query}} \\iff IV^* \\oplus M_1 = IV^* \\oplus M_0 \\iff M_1 = M_0$。因 $M_0 \\neq M_1$，碰撞機率嚴格為 0：$\\Pr[\\mathcal{A} \\to 0 \\mid b = 1] = 0$。\n區分優勢 $\\mathbf{Adv} = |1 - 0| = 1$。CBC 模式被徹底攻破。Q.E.D。"
    ],
    "algorithm": "歷史警示：此機制即為歷史上攻破 TLS 1.0 的著名 BEAST（Browser Exploit Against SSL/TLS）攻擊原型，迫使產業全面淘汰可預測 IV。",
    "pitfall": "考試扣分點：CBC 模式之 IV 不僅要保證不重複，而且在明文確定前必須保持不可預測（Unpredictable）。"
  }
];
