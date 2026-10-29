// Cryptography Course Review Data (Filtered strictly up to Slides 1.5 Section 1)
const MODULES_DATA = [
  {
    "id": "mod-0",
    "number": "模組 00",
    "title": "古典密碼學、密碼分析與離散數學基石",
    "subtitle": "Historical Ciphers, Cryptanalysis & Discrete Math Foundations",
    "sources": [
      "Introduction to Modern Cryptography - Historical Ciphers (Katz & Lindell Ch. 1)",
      "Cyrptography.pdf (The Joy of Cryptography, Ch. 0: Review of Concepts & Notation, p. 1 - 9)"
    ],
    "summary": "融合古典密碼學分析與離散數學基石：柯克霍夫原則（Kerckhoffs's Principle）、凱撒密碼、單字母替換、維吉尼亞多表密碼、頻率分析、卡西斯基檢驗法、重合指數（IC）；指數禁忌、模除運算子（非負餘數定義）、同餘關係、歐幾里得 GCD 演算法、二進位字串 XOR 四大代數性質、函數分類（單射/映成/雙射）與聯集上界機率論。",
    "sections": [
      {
        "title": "柯克霍夫原則與密碼學假設邊界",
        "content": [
          "**Kerckhoffs's Principle（柯克霍夫原則）**：加密系統的安全性絕不能依賴演算法的保密（Security through Obscurity），而必須完全建立在金鑰（Secret Key）的保密之上。演算法公開能接受全世界密碼專家檢驗；金鑰外洩時僅需重新生成金鑰即可恢復安全性。",
          "**密碼學防範與不防範之範疇**：密碼學防範在開放/惡意中間人通道下的竊聽與竄改；無法防範終端惡意軟體鍵擊記錄、側信道實體攻擊或使用者社交工程。"
        ]
      },
      {
        "title": "三大古典密碼機制與破譯推導",
        "content": [
          "**1. 凱撒移位密碼（Shift Cipher / Caesar Cipher）**：定義於 $\\mathbb{Z}_{26}$，金鑰 $k \\in \\{0, \\dots, 25\\}$。加密 $c = (m + k) \\pmod{26}$，解密 $m = (c - k) \\pmod{26}$。金鑰空間只有 26，暴力窮舉可在瞬間破譯。",
          "**2. 單字母替換密碼（Monoalphabetic Substitution Cipher）**：金鑰為 26 字母之置換排列，金鑰空間 $|\\mathcal{K}| = 26! \\approx 4 \\times 10^{26}$。雖然金鑰空間極大無法窮舉，但因字母保持一對一映射，完全保留自然語言的單字母與雙字母統計頻率特徵（如英文 E 約 12.7%，T 約 9.1%），透過頻率分析即可輕易手動破譯！",
          "**3. 維吉尼亞多表密碼（Vigenère Cipher）**：以長度 $t$ 之字串 $k = (k_1, \\dots, k_t)$ 進行循環移位。卡西斯基檢驗法（Kasiski Examination）透過重複字串間距的最大公因數（GCD）推導金鑰週期 $t$；重合指數（Index of Coincidence, IC）隨機抽取兩字母相同的機率：純隨機約 $0.038$，英語文本約 $0.065$，分組週期正確時子密文 IC 必然躍升至約 $0.065$。"
        ]
      },
      {
        "title": "密碼學必備離散數學基石（Joy of Cryptography Ch. 0）",
        "content": [
          "**指數運算重大禁忌**：$(x^a)(x^b) = x^{a+b}$、$(x^a)^b = x^{ab}$。嚴禁寫出 $(x^a)(x^b) = x^{ab}$，底數相同時冪次是相加而非相乘。",
          "**模除運算子（% Operator）之非負性**：$a \\% n$ 定義為唯一的餘數 $r \\in \\{0, \\dots, n-1\\}$ 滿足 $n \\mid (a - r)$。**關鍵特性：無論 $a$ 為正或負，$a \\% n$ 恆非負**！例如 $20 \\% 7 = 6$、$-20 \\% 7 = 1$（$-20 = -3 \\times 7 + 1$）、$-1 \\% 7 = 6$。",
          "**同餘 $\\equiv_n$ 與整數相等之嚴格差異**：$a \\equiv_n b$ 兩邊可為任意整數；而 $a = b \\% n$ 要求 $a \\in \\{0, \\dots, n-1\\}$。例如 $99 \\equiv_{10} 19$ 為真，但 $99 = 19 \\% 10$ 為假（$19 \\% 10 = 9 \\ne 99$）。",
          "**歐幾里得 GCD 演算法**：$\\gcd(x, y) = \\gcd(y, x \\% y)$。模乘法運算時應隨時化簡中間數值，避免大數溢位。",
          "**XOR 四大代數基石**：交換律、結合律、單位元（$x \\oplus 0 = x$）、自相反身性（$x \\oplus x = 0$ 且 $(x \\oplus y) \\oplus y = x$）。自相反身性是對稱密碼加解密能使用同一電路的核心依據。",
          "**函數映射與置換**：單射（$|X| \\le |Y|$）、映成（$|X| \\ge |Y|$）、雙射（$|X|=|Y|$ 且具備反函數 $f^{-1}$）。有限集合上的雙射即為置換（Permutation），為分組密碼之數學本質。",
          "**聯集上界（Union Bound）**：對任意 $k$ 個事件（無論是否獨立），恆有 $P[\\bigcup_{i=1}^k E_i] \\le \\sum_{i=1}^k P[E_i]$。"
        ]
      }
    ]
  },
  {
    "id": "mod-1",
    "number": "模組 01",
    "title": "完美保密性、單次密鑰與金鑰極限",
    "subtitle": "Perfect Secrecy, One-Time Pad & Shannon's Impossibility Theorem",
    "sources": [
      "Introduction to Modern Cryptography - Perfectly Secret Encryption (Katz & Lindell Ch. 2)",
      "1.2 The Provable Security Mindset.pdf (p. 4 - 32)",
      "Cyrptography.pdf (The Joy of Cryptography, Ch. 1)"
    ],
    "summary": "深入 Shannon 資訊理論完美保密性定義、One-Time Pad（OTP）加解密與完美性數學證明、Shannon 不可能定理（|K| >= |M|）、Two-Time Pad 致命金鑰重用攻擊、ASCII 空白鍵翻轉特徵與 Crib Dragging，以及位元翻轉延展性攻擊。",
    "sections": [
      {
        "title": "Shannon 完美保密性之嚴格定義（Perfect Secrecy）",
        "content": [
          "**直覺觀念**：觀察到密文不應提供任何有關明文的新資訊。",
          "**形式化定義**：對於明文上的任意先驗機率分佈、任意明文 $m \\in \\mathcal{M}$ 與任意密文 $c \\in \\mathcal{C}$（滿足 $P[C=c] > 0$），恆有：",
          "$$P[M = m \\mid C = c] = P[M = m]$$",
          "即明文的**後驗機率嚴格等於先驗機率**。",
          "**等價不可區分性定義**：對任意兩明文 $m_0, m_1 \\in \\mathcal{M}$ 與任意密文 $c$，$P[\\mathrm{Enc}_K(m_0) = c] = P[\\mathrm{Enc}_K(m_1) = c]$。"
        ]
      },
      {
        "title": "單次密鑰（One-Time Pad, OTP）規格與完美性推導",
        "content": [
          "明文、密文與金鑰均為長度 $\\ell$ 的二進位字串：$\\mathcal{M} = \\mathcal{C} = \\mathcal{K} = \\{0, 1\\}^\\ell$。",
          "- 金鑰生成：$K \\leftarrow \\{0, 1\\}^\\ell$ 均勻隨機抽取，每個金鑰出現機率均為 $2^{-\\ell}$。",
          "- 加密：$C = M \\oplus K$；解密：$M = C \\oplus K$。",
          "**完美安全性推導**：",
          "任取固定明文 $m$ 與密文 $c$，使 $\\mathrm{Enc}_k(m) = c$ 成立的充要條件為 $k = m \\oplus c$。因此：",
          "$$P[C = c \\mid M = m] = P[K = m \\oplus c] = \\frac{1}{2^\\ell}$$",
          "該機率對任意明文 $m$ 恆為常數 $2^{-\\ell}$，與明文完全獨立。故 OTP 具備嚴格的完美保密性！"
        ]
      },
      {
        "title": "Shannon 不可能定理與金鑰分發難題",
        "content": [
          "**Shannon 不可能定理**：任何滿足完美保密性的加密系統，其金鑰空間必須大於或等於明文空間：$|\\mathcal{K}| \\ge |\\mathcal{M}|$。二進位字串下，金鑰長度必須至少與明文一樣長（$\\ell_K \\ge \\ell_M$）。",
          "**反證法推導**：若 $|\\mathcal{K}| < |\\mathcal{M}|$，給定密文 $c$，可能解密出的明文集合大小最多僅 $|\\mathcal{K}|$ 個，必定存在某個明文 $m^*$ 永遠無法由 $c$ 解出（$P[M = m^* \\mid C = c] = 0 \\ne P[M = m^*]$），產生矛盾！故 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 必然成立。",
          "**金鑰分發難題（Key Distribution Problem）**：要加密 1 TB 資料必須預先安全傳輸 1 TB 隨機金鑰，且金鑰嚴禁重複使用，使得 OTP 在大規模實務傳輸中極度受限。"
        ]
      },
      {
        "title": "實務致命漏洞：Two-Time Pad 攻擊與延展性",
        "content": [
          "**1. Two-Time Pad 攻擊（重用金鑰的災難）**：",
          "- 若以同一金鑰 $k$ 加密兩條訊息 $m_1, m_2$：$c_1 = m_1 \\oplus k, \\; c_2 = m_2 \\oplus k$。",
          "- 密文相異或：$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$。金鑰完全抵消！",
          "- **ASCII 特徵破譯**：ASCII 英文字母高 3 位為 `010` 或 `011`，空白鍵為 `0x20`（`00100000`）。字母與空白鍵 XOR 會翻轉大小寫，非空白鍵互斥或會產生小於 `0x40` 的值。攻擊者利用 Crib Dragging 技術可迅速全數還原明文！",
          "**2. 延展性（Malleability / Bit-flipping Attack）**：",
          "- 中間人修改密文為 $c' = c \\oplus \\Delta$，解密明文為 $m' = c' \\oplus k = (c \\oplus k) \\oplus \\Delta = m \\oplus \\Delta$。攻擊者可在不知道金鑰與明文下精準操縱明文特定位元翻轉。**OTP 僅保護機密性，完全不具備完整性！**"
        ]
      }
    ]
  },
  {
    "id": "mod-2",
    "number": "模組 02",
    "title": "可證明安全性思維與計算密碼學",
    "subtitle": "The Provable Security Mindset, Concrete/Asymptotic Security & Hybrid Proofs",
    "sources": [
      "1.2 The Provable Security Mindset.pdf (劉子源教授講義全部 62 頁)",
      "Cyrptography.pdf (The Joy of Cryptography, Ch. 2 & Ch. 4)"
    ],
    "summary": "地毯式涵蓋講義 1.2 全文：秘密性的思考（Thinking about Secrecy）、對稱密鑰加密之正確性（Correctness）與單次保密性（One-Time Secrecy）形式化定義、計算密碼學之具體方法（Concrete Approach）與漸近方法（Asymptotic Approach）、巨大運算的金錢成本（Monetary Cost of Computations）與比特幣挖礦算力規模對比、PPT、可忽略函數（Negligible Function）、安全遊戲範式、示範不安全性三步驟、混合證明技術（The Hybrid Technique）以及生日定理（Birthday Bound）。",
    "sections": [
      {
        "title": "對稱加密的形式化定義：正確性與單次保密性",
        "content": [
          "對稱加密方案（SKE）由三個演算法組成：$(\\mathrm{Gen}, \\mathrm{Enc}, \\mathrm{Dec})$。",
          "**正確性條件（Correctness）**：對任意安全參數 $\\lambda$、任意由 $\\mathrm{Gen}(1^\\lambda)$ 生成的金鑰 $k$ 以及任意明文 $m \\in \\mathcal{M}$，恆滿足：",
          "$$\\mathrm{Dec}(k, \\mathrm{Enc}(k, m)) = m$$",
          "**單次保密性（One-Time Secrecy）與區分器程式**：攻擊者程式 $\\mathcal{A}$ 提交等長明文對 $(m_0, m_1)$，在 Game 0 收到 $\\mathrm{Enc}(k, m_0)$，在 Game 1 收到 $\\mathrm{Enc}(k, m_1)$。若任何多項式時間區分器輸出 1 的機率差（優勢度 Advantage）皆小於可忽略函數，則滿足單次保密性。"
        ]
      },
      {
        "title": "計算密碼學兩大取徑：具體方法 vs 漸近方法",
        "content": [
          "為突破 Shannon 定理限制，現代密碼學建立在計算安全性之上：",
          "**1. 具體方法（The Concrete Approach，投影片 p.50-55）**：",
          "- 量化攻擊者所需的實質運算資源（時間 $t$）與成功優勢（$\\epsilon$），稱方案為 $(t, \\epsilon)$-安全。",
          "- **巨大運算的金錢成本（Monetary Cost of Huge Computations）**：暴力破解一個 128 位元金鑰需要 $2^{128} \\approx 3.4 \\times 10^{38}$ 次操作。即使動用全球所有超級電腦耗盡地球總能源運轉數十億年，也無法完成！",
          "- **比特幣挖礦算力對比（Bitcoin Mining Computational Scale）**：全球比特幣網絡每秒算力約 $6 \\times 10^{20}$ 次雜湊，即使讓全網比特幣礦機全部轉向暴力破解 AES-128，破解單一金鑰依然需要數百萬兆年！",
          "**2. 漸近方法（The Asymptotic Approach，投影片 p.56-61）**：",
          "- 所有演算法複雜度皆表示為安全參數 $n$ 的函數。攻擊者限制為機率多項式時間（PPT），成功機率限制為可忽略函數（$\\mathrm{negl}(n) < 1/n^c$）。"
        ]
      },
      {
        "title": "安全遊戲、示範不安全性與混合證明技術",
        "content": [
          "**兩大安全遊戲風格**：Left-vs-Right 風格（加密回傳 $m_0$ 還是 $m_1$）與 Real-vs-Random 風格（真實密文還是純隨機字串）。",
          "**示範不安全性的攻擊三步驟**：(1) 寫出具體 PPT 攻擊演算法 $\\mathcal{A}$；(2) 精確計算 $\\mathcal{A}$ 在兩遊戲中輸出 1 的機率；(3) 計算差值絕對值，展示 $\\mathbf{Adv}(\\mathcal{A})$ 為顯著非可忽略常數（如 1 或 0.5）。",
          "**核心證明武器：混合證明技術（The Hybrid Technique）**：在真實遊戲 $G_0$ 與目標隨機遊戲 $G_k$ 之間構造多項式個中間遊戲 $G_0, G_1, \\dots, G_k$，每步僅微調單一元件。由三角不等式：$|P[G_0] - P[G_k]| \\le \\sum |P[G_i] - P[G_{i+1}]|$，將整體安全性嚴格歸約到底層難題！"
        ]
      },
      {
        "title": "生日問題機率與抽樣邊界（Birthday Bound）",
        "content": [
          "從大小為 $N$ 的集合中進行 $q$ 次隨機抽樣，發生碰撞的機率近似為 $P[\\text{Collision}] \\approx q^2 / (2N)$。",
          "**臨界值 $q \\approx \\sqrt{N}$**：64 位元區塊密碼（$N=2^{64}$）在加密約 $2^{32} \\approx 40$ 億個區塊（約 32 GB）時即有 50% 機率發生碰撞，瓦解 CBC 安全性（Sweet32 攻擊）；現代 AES 採用 128 位元區塊（碰撞門檻高達 $2^{64}$ 區塊）確保安全。"
        ]
      }
    ]
  },
  {
    "id": "mod-3",
    "number": "模組 03",
    "title": "偽隨機性、分組密碼與 Feistel 網路",
    "subtitle": "Pseudorandomness: PRG, PRF, PRP, Feistel Networks & DES/AES",
    "sources": [
      "1.4 Pseudorandomness.pdf (劉子源教授講義全部 60 頁)",
      "Cyrptography.pdf (The Joy of Cryptography, Ch. 5 & Ch. 6)"
    ],
    "summary": "地毯式涵蓋講義 1.4 全文：PRG/PRF/PRP 互相建構關係、Pseudo-OTP 構造與 Hybrid 證明、RC4 串流密碼運作演算法與弱點、不安全 PRF 反例構造剖析、PRF 黃金法則、惰性字典 vs 惰性置換、PRP/PRF 切換引理、Feistel 網路運作、攻破 2 輪 Feistel 網路的具體攻擊演算法推導、Luby-Rackoff 定理、DES 實務與 EFF Deep Crack 歷史實例，以及 AES-128 結構。",
    "sections": [
      {
        "title": "PRG、PRF、PRP 三大原語與互相轉換架構",
        "content": [
          "**三大原語定義**：",
          "- **PRG（偽隨機生成器）**：$G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + \\ell}$，將短種子伸展為長字串，對 PPT 區分器不可區分。",
          "- **PRF（偽隨機函數）**：金鑰化函數族 $F_k$，黑盒子查詢模型下與真正的隨機函數 RF 不可區分。",
          "- **PRP（偽隨機置換 / 分組密碼）**：雙射（一對一且映成）置換族 $P_k$，正向與反向皆為多項式時間可計算。",
          "**相互轉換架構（投影片 p.2）**：",
          "- **PRG $\\to$ PRF**：GGM 樹狀建構法（以輸入位元尋訪二元樹路徑）。",
          "- **PRF $\\to$ PRG**：CTR 模式計數器串接（$G(k) = F_k(0) \\parallel F_k(1) \\dots$）。",
          "- **PRF $\\to$ PRP**：Feistel 網路結構。",
          "**Pseudo-OTP**：$c = m \\oplus G(k)$，透過 Hybrid 證明將 $G(k)$ 替換為真隨機字串，以短金鑰實現計算安全性。"
        ]
      },
      {
        "title": "串流密碼實例：RC4 演算法與 PRG 弱點",
        "content": [
          "**RC4 串流密碼（投影片 p.18-19）**：包含兩大演算法：",
          "1. **金鑰排程演算法（KSA）**：初始化 256 位元組狀態表 $S = [0, 1, \\dots, 255]$，依金鑰 $k$ 進行打亂洗牌。",
          "2. **偽隨機生成演算法（PRGA）**：指針 $i, j$ 循環前進，交換 $S[i], S[j]$，輸出位元組 $K = S[(S[i] + S[j]) \\% 256]$。",
          "**重大弱點**：RC4 初期輸出的位元組存在嚴重的統計偏差（Key-derivation bias，如第 2 個位元組出現 0 的機率顯著偏高），導致 WEP 等早期協議被輕易破譯，現代已被全面淘汰！"
        ]
      },
      {
        "title": "不安全 PRF 的反例構造與 PRF 黃金法則",
        "content": [
          "**不安全 PRF 反例分析（投影片 p.25-28）**：",
          "- 反例 A：$F_k(x) = k \\oplus x$。攻擊者查詢 $x_1$ 得 $y_1 = k \\oplus x_1$，查詢 $x_2$ 得 $y_2 = k \\oplus x_2$。計算 $y_1 \\oplus y_2 = x_1 \\oplus x_2$，該等式永遠成立；但在真正隨機函數中發生機率僅 $2^{-n}$！攻擊者優勢度接近 1，該構造被完全攻破！",
          "- 反例 B：$F_k(x) = k \\cdot x \\pmod p$。利用線性關係亦可瞬間被區分器識破。",
          "**The Golden Rule of PRFs（PRF 黃金法則，投影片 p.29）**：**絕不可在 PRF 內部保留輸入與輸出之間的任何代數線性關係或結構特徵！**"
        ]
      },
      {
        "title": "惰性字典 vs 惰性置換與 PRP/PRF 切換引理",
        "content": [
          "**惰性字典（Lazy Dictionaries）vs 惰性置換（Lazy Permutations，投影片 p.38-39）**：形式化證明中模擬 RF（隨機函數）與 RP（隨機置換）的技術。RF 允許碰撞；RP 嚴格禁止碰撞，若隨機抽到已存在的輸出必須重新取樣。",
          "**PRP/PRF 切換引理（Switching Lemma，投影片 p.41）**：",
          "$$\\big| \\mathbf{Adv}_{\\mathrm{prp}}(\\mathcal{D}) - \\mathbf{Adv}_{\\mathrm{prf}}(\\mathcal{D}) \\big| \\le \\frac{q(q-1)}{2 \\cdot 2^n} \\le \\frac{q^2}{2^{n+1}}$$",
          "只要查詢次數 $q \\ll 2^{n/2}$，分組密碼即可直接當作理想 PRF 使用。"
        ]
      },
      {
        "title": "Feistel 網路、攻破 2 輪 Feistel 演算法與 Luby-Rackoff 定理",
        "content": [
          "**Feistel 網路運作**：$L_{i+1} = R_i, \\; R_{i+1} = L_i \\oplus F_{k_i}(R_i)$。輪函數 $F$ 本身不需要可逆，整體架構天然對稱解密。",
          "**攻破 2 輪 Feistel 網路的具體演算法推導（投影片 p.49-51）**：",
          "- 2 輪 Feistel 輸出為：$L_2 = R_0 \\oplus F_1(L_0), \\; R_2 = L_0 \\oplus F_2(L_2)$。",
          "- 攻擊者選取兩組明文 $(L_0, R_0)$ 與 $(L_0, R'_0)$，其左半部相同，右半部不同：$\\Delta R = R_0 \\oplus R'_0$。",
          "- 觀察兩次加密輸出的左半部：$L_2 = R_0 \\oplus F_1(L_0)$，$L'_2 = R'_0 \\oplus F_1(L_0)$。",
          "- 攻擊者計算 $L_2 \\oplus L'_2 = R_0 \\oplus R'_0 = \\Delta R$！",
          "- 密文左半部的 XOR 恆等於明文右半部的 XOR！而在真正的隨機置換中，該等式成立機率僅 $2^{-n/2}$。攻擊者以 100% 優勢攻破 2 輪 Feistel！",
          "**Luby-Rackoff 定理（投影片 p.52-53）**：",
          "- 3 輪 Feistel 達成抗選擇明文攻擊的 PRP。",
          "- **必須達到 4 輪 Feistel**，才能抵抗正向與反向雙向預言機攻擊，達成強偽隨機置換（Strong PRP）！"
        ]
      },
      {
        "title": "DES 實務、EFF Deep Crack 歷史與 AES-128 結構",
        "content": [
          "**DES 實務與 EFF Deep Crack（投影片 p.54-56）**：DES 為 16 輪 Feistel 結構，但金鑰僅有 56 位元（金鑰空間 $2^{56} \\approx 7.2 \\times 10^{16}$）。1998 年電子前哨基金會（EFF）耗資 25 萬美元建造專用硬體「Deep Crack」，僅耗時 56 小時便暴力窮舉破譯 DES 金鑰，徹底終結 DES，促成 AES 的誕生！",
          "**AES-128 結構（投影片 p.57-59）**：非 Feistel 網路，採用 SPN（Substitution-Permutation Network）結構，具備 10 輪運算（SubBytes, ShiftRows, MixColumns, AddRoundKey），以 128 位元金鑰徹底封殺暴力破解。"
        ]
      }
    ]
  },
  {
    "id": "mod-4",
    "number": "模組 04",
    "title": "選擇明文攻擊（CPA）與加密模式深入",
    "subtitle": "Chosen-Plaintext Attacks & Block Cipher Modes of Operation",
    "sources": [
      "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Section 1, p. 2 - 14)",
      "Cyrptography.pdf (The Joy of Cryptography, Ch. 7: Security Against CPA)"
    ],
    "summary": "地毯式涵蓋講義 1.5 Section 1 全文：CPA 安全性重要性、明文長度考量、確定性加密被 100% 攻破證明、AES 單獨運作之確定性、分組密碼操作模式深入剖析（CBC 模式與 CTR 模式深入檢視）、基於 PRF 之隨機化 CPA 安全方案構造與 Hybrid 證明、狀態化 vs 隨機化工程取捨，以及偽隨機密文（Pseudorandom Ciphertexts）。",
    "sections": [
      {
        "title": "CPA 安全性與確定性加密的結構性死穴",
        "content": [
          "**為什麼 CPA 安全性至關重要？（投影片 p.4）** 在真實網路通訊中，攻擊者可藉由向受害者發送特定封包（如誘騙其加密特製的電子郵件或網路請求）來觀察密文，因此必須假設攻擊者擁有加密預言機 $\\mathcal{O}_{\\mathrm{Enc}}(\\cdot)$。",
          "**AES 本身是確定性的（AES by itself is deterministic，投影片 p.9）**：分組密碼 AES 只是固定區塊的一對一映射，若直接使用（ECB 模式），相同明文永遠產生相同密文，著名的「ECB 企鵝圖」直觀展示了明文紋理與結構的完全外洩！",
          "**確定性加密在 CPA 下的 100% 破譯證明（投影片 p.6）**：",
          "- 攻擊者向預言機查詢 $m_0$ 取得密文 $c_0 = \\mathrm{Enc}(k, m_0)$。",
          "- 挑戰階段送出 $(m_0, m_1)$，接收挑戰密文 $c^*$。",
          "- 若 $c^* == c_0$ 則猜 $b=0$，否則猜 $b=1$。勝率 100%，優勢度恆為 1！**任何確定性加密演算法絕對無法達成 IND-CPA 安全！**"
        ]
      },
      {
        "title": "分組密碼操作模式深入剖析：CBC 與 CTR 模式",
        "content": [
          "**1. CBC 模式深入檢視（CBC mode: a closer look，投影片 p.11-12）**：",
          "- 加密：$C_0 = \\mathrm{IV}$（必須均勻隨機選取）；$C_i = E_k(P_i \\oplus C_{i-1})$。",
          "- 解密：$P_i = D_k(C_i) \\oplus C_{i-1}$。",
          "- 特性：解密可完全平行化，但加密必須序列依序執行；若 IV 可被攻擊者預測（如固定或遞增 IV），會遭到 BEAST 攻擊攻破 CPA 安全！",
          "**2. CTR 計數器模式深入檢視（CTR mode: a closer look，投影片 p.13-14）**：",
          "- 加密：計算金鑰串流遮罩 $S_i = E_k(\\mathrm{IV} \\parallel i)$，密文為 $C_i = P_i \\oplus S_i$。",
          "- 解密：$P_i = C_i \\oplus E_k(\\mathrm{IV} \\parallel i)$。**注意：解密完全不需要分組密碼的逆運算 $D_k$，只使用正向加密 $E_k$！**",
          "- 特性：加密與解密皆可完全高度硬體平行化，支援隨機讀取；但 IV 與計數器嚴禁重用！"
        ]
      },
      {
        "title": "基於 PRF 之隨機化 CPA 安全加密構造與證明",
        "content": [
          "設 $F$ 為安全 PRF，金鑰為 $k$：",
          "- 加密明文 $m$：均勻隨機挑選初始化向量 $r \\leftarrow \\{0, 1\\}^\\mathrm{in}$，輸出密文對：$c = \\langle r, \\; F(k, r) \\oplus m \\rangle$。",
          "- 解密：$m = c_1 \\oplus F(k, r)$。",
          "**安全性推導（The Hybrid Technique 應用）**：",
          "1. Game 0：真實 CPA 遊戲，遮罩為 $F(k, r)$。",
          "2. Game 1：將 PRF 替換為真正隨機函數 RF。兩者之差受限於 $\\mathbf{Adv}_{\\mathrm{prf}}$。",
          "3. Game 2：在隨機函數下，只要隨機選取的 $r$ 無碰撞，每個 $F(k, r)$ 皆為全新的一致一次性金鑰。由生日界可知 $q$ 次查詢碰撞機率小於 $q^2 / (2 \\cdot 2^\\mathrm{in})$。",
          "4. 在無碰撞情況下，密文等價於 OTP，優勢度嚴格為 0！故方案具備可證明 CPA 安全性！"
        ]
      },
      {
        "title": "狀態化（Stateful）vs 隨機化（Randomized）與偽隨機密文",
        "content": [
          "**隨機化（Randomized）**：每次抽取隨機 IV $r$。無需持久化狀態，但存在生日碰撞風險（$2^{n/2}$ 區塊後可能碰撞）。",
          "**狀態化（Stateful / Counter）**：雙方維護嚴格單調遞增計數器 Nonce（$r = 0, 1, 2, \\dots$）。保證 Nonce 絕不重複，徹底消除生日碰撞；缺點為若系統斷電重置導致計數器回退，將引發金鑰重用災難。",
          "**偽隨機密文（Pseudorandom Ciphertexts）**：密文外觀與純隨機二進位雜訊不可區分，能徹底掩蓋長度特徵與協議元數據。"
        ]
      }
    ]
  }
];

const QUIZ_DATA = [
  {
    "id": "q-all-0-1",
    "moduleId": "mod-0",
    "category": "概念辨析",
    "question": "根據柯克霍夫原則（Kerckhoffs's Principle），一個密碼系統的安全性應該建立在何種前提之上？",
    "options": [
      "加密演算法細節必須被嚴格保密，防止外界得知運算邏輯",
      "即使加密演算法被完全公開，只要金鑰（Secret Key）保密，系統就必須維持安全",
      "金鑰空間大小必須大於等於 $2^{256}$ 才能保證絕對不被攻破",
      "只要更換為多表替換密碼即可保證數學安全性"
    ],
    "answer": 1,
    "explanation": "柯克霍夫原則是現代密碼學的核心基石：安全絕不能依賴演算法的隱蔽（Security through Obscurity）。公開演算法能接受大眾檢驗，金鑰外洩時僅需更換金鑰即可恢復安全性。",
    "pitfalls": "將『演算法保密』視為更安全，忽視了演算法一旦逆向工程外洩將導致系統全面毀滅。",
    "reference": "Introduction to Modern Cryptography, Katz & Lindell Ch. 1, p. 6 & Joy of Cryptography Ch. 1"
  },
  {
    "id": "q-all-0-2",
    "moduleId": "mod-0",
    "category": "數學運算",
    "question": "在密碼學離散數學定義中，計算負數模除 $-20 \\% 7$ 的正確數值為何？",
    "options": [
      "-6",
      "1",
      "-1",
      "6"
    ],
    "answer": 1,
    "explanation": "在密碼學與整數論中，餘數 $r = a \\% n$ 必須是非負數且滿足 $r \\in \\{0, \\dots, n-1\\}$。因為 $-20 = (-3) \\times 7 + 1$，餘數為 1。$-20$ 比 7 的倍數（$-21$）大 1。",
    "pitfalls": "部分程式語言定義負數餘數為 -6，這在密碼學運算中是嚴格錯誤的，密碼學餘數必須為非負數。",
    "reference": "The Joy of Cryptography, Ch. 0.2, Definition 0.2, p. 2"
  },
  {
    "id": "q-all-0-3",
    "moduleId": "mod-0",
    "category": "密碼分析",
    "question": "單字母替換密碼的金鑰空間大小 $|\\mathcal{K}| = 26! \\approx 4 \\times 10^{26}$。為何此密碼系統在實務上依舊能被輕易攻破？",
    "options": [
      "因為金鑰空間雖然龐大，但現代電腦可在數分鐘內窮舉全部 $26!$ 種組合",
      "因為加密過程未將字母轉換為二進位位元組進行 XOR 運算",
      "因為每個字母始終保持一對一固定映射，完全保留了自然語言的統計頻率特徵（如英文 E 約佔 12.7%）",
      "因為卡西斯基檢驗法可以直接算出單字母替換密碼的金鑰長度"
    ],
    "answer": 2,
    "explanation": "單字母替換密碼雖然無法使用暴力窮舉破解，但因對應關係固定，密文中出現頻率最高的字母極可能對應明文中的 'E'，透過單字母頻率分析即可在無需窮舉下輕易還原明文。",
    "pitfalls": "誤以為『金鑰空間大就等於不可破解』，忽略了統計特徵外洩完全繞過了金鑰窮舉。",
    "reference": "Introduction to Modern Cryptography, Katz & Lindell Ch. 1, p. 9"
  },
  {
    "id": "q-all-0-4",
    "moduleId": "mod-0",
    "category": "統計推導",
    "question": "在使用重合指數（Index of Coincidence, IC）檢驗維吉尼亞密碼之金鑰週期時，若猜測的週期 $t$ 正確，子密文的 IC 理論數值應接近何者？",
    "options": [
      "純隨機字串的 $0.038$",
      "自然英文文本的約 $0.065$",
      "0",
      "1.0"
    ],
    "answer": 1,
    "explanation": "隨機均勻字串抽取兩相同字母的機率約 $1/26 \\approx 0.038$；在英語文本中因字母分佈不均勻，IC 躍升至約 $0.065$。若分組週期猜測正確，子密文保留了英語特性，IC 值會趨近 $0.065$。",
    "pitfalls": "混淆隨機文字（0.038）與英語文本（0.065）的 IC 理論基準值。",
    "reference": "Introduction to Modern Cryptography, Katz & Lindell Ch. 1"
  },
  {
    "id": "q-all-1-1",
    "moduleId": "mod-1",
    "category": "概念辨析",
    "question": "下列哪一個數學方程式最精準表達了 Shannon 的「完美保密性（Perfect Secrecy）」？",
    "options": [
      "$P[M = m \\mid C = c] = 0$",
      "$P[M = m \\mid C = c] = P[M = m]$",
      "$P[C = c \\mid M = m] = 1$",
      "$P[K = k \\mid C = c] = P[K = k]$"
    ],
    "answer": 1,
    "explanation": "Shannon 定義完美保密性為：在觀察到特定密文 $C=c$ 後，明文為 $m$ 的後驗機率 $P[M=m \\mid C=c]$，與未看到密文前的先驗機率 $P[M=m]$ 嚴格相等，密文不透露明文的任何資訊。",
    "pitfalls": "誤選 $P[M=m \\mid C=c] = 0$，完美保密不是機率為 0，而是後驗等於先驗。",
    "reference": "Introduction to Modern Cryptography, Katz & Lindell Ch. 2, p. 25 & Joy Ch. 1"
  },
  {
    "id": "q-all-1-2",
    "moduleId": "mod-1",
    "category": "數學證明",
    "question": "在 One-Time Pad（OTP）中，對於長度為 $\\ell$ 的任意固定明文 $m$ 與密文 $c$，$P[C=c \\mid M=m]$ 的精確數值為何？",
    "options": [
      "0",
      "$2^{-\\ell}$",
      "$1/\\ell$",
      "取決於明文中 0 與 1 的分佈比例"
    ],
    "answer": 1,
    "explanation": "因為 $C = M \\oplus K$，給定 $M=m$ 時，產生密文 $c$ 的充要條件為 $K = m \\oplus c$。金鑰從長度 $\\ell$ 的字串中均勻隨機抽取，機率恆為 $1/2^\\ell = 2^{-\\ell}$，證明了 OTP 的完美安全性。",
    "pitfalls": "誤以為機率會受到明文長度 $\\ell$ 的倍數或文字意義影響。",
    "reference": "Introduction to Modern Cryptography, Katz & Lindell Ch. 2, p. 28 & Joy Ch. 1"
  },
  {
    "id": "q-all-1-3",
    "moduleId": "mod-1",
    "category": "攻擊推導",
    "question": "發送方使用相同 OTP 金鑰加密兩條明文 $m_1, m_2$，攻擊者取得 $c_1, c_2$ 並計算 $c_1 \\oplus c_2$，其結果為何？",
    "options": [
      "純隨機字串，完全無法分析",
      "得到 $m_1 \\oplus m_2$，金鑰被完全抵消，可透過 ASCII 空白鍵（0x20）大小寫翻轉特徵與 Crib Dragging 破譯明文",
      "金鑰平方數值",
      "明文長度的總和"
    ],
    "answer": 1,
    "explanation": "$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$。金鑰完全被消去，攻擊者直接掌握兩篇明文的互斥或，此即為著名的 Two-Time Pad 致命漏洞。",
    "pitfalls": "誤以為金鑰依然留在密文 XOR 結果中保護資料。",
    "reference": "Introduction to Modern Cryptography Ch. 2 & Joy of Cryptography Ch. 1, p. 16"
  },
  {
    "id": "q-all-1-4",
    "moduleId": "mod-1",
    "category": "理論極限",
    "question": "根據 Shannon 不可能定理，任何達到完美保密性的加密系統，其金鑰空間 $|\\mathcal{K}|$ 與明文空間 $|\\mathcal{M}|$ 必須滿足何種關係？",
    "options": [
      "$|\\mathcal{K}| \\le |\\mathcal{M}|$",
      "$|\\mathcal{K}| \\ge |\\mathcal{M}|$",
      "$|\\mathcal{K}| = \\log_2 |\\mathcal{M}|$",
      "$|\\mathcal{K}| = \\sqrt{|\\mathcal{M}|}$"
    ],
    "answer": 1,
    "explanation": "Shannon 定理證明：若 $|\\mathcal{K}| < |\\mathcal{M}|$，必定存在某些明文在觀察到特定密文後解密機率為 0，破壞完美保密。因此金鑰空間必須至少與明文空間一樣大（$|\\mathcal{K}| \\ge |\\mathcal{M}|$）。",
    "pitfalls": "誤記為 $|\\mathcal{K}| \\le |\\mathcal{M}|$ 或對數關係。",
    "reference": "Introduction to Modern Cryptography Ch. 2, p. 33 & Joy Ch. 1, p. 18"
  },
  {
    "id": "q-all-2-1",
    "moduleId": "mod-2",
    "category": "概念辨析",
    "question": "在可證明安全性定義中，Left-vs-Right（$\\mathcal{L}_{\\mathrm{ots\\text{-}L}}$ vs $\\mathcal{L}_{\\mathrm{ots\\text{-}R}}$）風格的核心定義為何？",
    "options": [
      "挑戰者回傳金鑰的左半部或右半部給攻擊者",
      "攻擊者提交等長明文對 $(m_0, m_1)$，挑戰者在 Game 0 加密 $m_0$，在 Game 1 加密 $m_1$",
      "攻擊者必須在左側伺服器與右側伺服器之間進行分散式運算",
      "演算法使用向左移位或向右移位"
    ],
    "answer": 1,
    "explanation": "Left-vs-Right 風格要求攻擊者提交兩個明文 $m_0$（Left）與 $m_1$（Right），挑戰者隨機決定加密回傳哪一個，測試攻擊者是否有能力區分密文來自左側還是右側。",
    "pitfalls": "誤以為與金鑰切片或移位運算有關。",
    "reference": "1.2 The Provable Security Mindset.pdf & Joy of Cryptography Ch. 2.2, p. 26"
  },
  {
    "id": "q-all-2-2",
    "moduleId": "mod-2",
    "category": "證明技術",
    "question": "混合證明技術（The Hybrid Technique）在可證明安全性中的核心運作思路為何？",
    "options": [
      "混合使用對稱密碼與非對稱密碼來提升運算速度",
      "在真實遊戲 $G_0$ 與目標遊戲 $G_k$ 之間插入一系列相鄰僅有微小單步差異的中間遊戲，透過三角不等式將總優勢度限制在各步驟優勢度之和",
      "將密文與雜湊值混合進行多次加密",
      "將攻擊者的程式碼轉換為硬體電路進行混合模擬"
    ],
    "answer": 1,
    "explanation": "Hybrid Technique 是現代密碼學證明骨架。當兩遊戲差距太大無法直接歸約時，構造 $G_0, G_1, \\dots, G_k$，每步只替換一個元件，利用三角不等式將不可區分性歸約到底層元件的安全假設。",
    "pitfalls": "將證明技術中的 Hybrid 與混合加密（Hybrid Encryption）混為一談。",
    "reference": "The Joy of Cryptography, Ch. 2.4, p. 33"
  },
  {
    "id": "q-all-2-3",
    "moduleId": "mod-2",
    "category": "生日問題",
    "question": "根據生日定理（Birthday Bound），從大小為 $N = 2^{64}$ 的集合中進行 $q$ 次隨機抽樣，欲使發生至少一次碰撞的機率達到約 50%，抽樣次數 $q$ 約為多少？",
    "options": [
      "$2^{63}$ 次",
      "$\\approx \\sqrt{N} = 2^{32}$ 次（約 40 億次）",
      "$2^{64}$ 次",
      "64 次"
    ],
    "answer": 1,
    "explanation": "生日碰撞臨界值發生在 $q \\approx \\sqrt{N}$。當 $N = 2^{64}$ 時，$\\sqrt{2^{64}} = 2^{32} \\approx 4.29 \\times 10^9$ 次。這也是 64 位元區塊密碼在加密數十 GB 資料時即會面臨 Sweet32 碰撞攻擊的原因！",
    "pitfalls": "誤以為需要抽樣一半（$2^{63}$）才會碰撞，生日悖論展示了碰撞機率增長遠比直覺快速得多。",
    "reference": "The Joy of Cryptography, Ch. 4.4, p. 76 - 78 & Slides 1.2"
  },
  {
    "id": "q-all-2-4",
    "moduleId": "mod-2",
    "category": "複雜度理論",
    "question": "下列哪一個數學函數 $\\mu(n)$ 符合現代密碼學中「可忽略函數（Negligible Function）」的定義？",
    "options": [
      "$\\mu(n) = \\frac{1}{n^5}$",
      "$\\mu(n) = \\frac{1}{\\log_2 n}$",
      "$\\mu(n) = 2^{-n}$",
      "$\\mu(n) = \\frac{1}{1000n}$"
    ],
    "answer": 2,
    "explanation": "可忽略函數必須對任意正整數 $c$，最終滿足 $\\mu(n) < 1/n^c$。指數衰減函數 $2^{-n}$ 比任何多項式倒數 $1/n^c$ 衰減得更快，屬於可忽略函數；而 $1/n^5$、$1/\\log n$ 和 $1/(1000n)$ 都是多項式或次多項式等級，非可忽略函數。",
    "pitfalls": "誤認為分母有 $n^5$ 很大就是可忽略，忽略了定義要求對『任意 $c$』皆須成立。",
    "reference": "1.2 The Provable Security Mindset.pdf, p. 55 & Joy Ch. 4.2"
  },
  {
    "id": "q-all-3-1",
    "moduleId": "mod-3",
    "category": "原語建構",
    "question": "GGM 建構法（Goldreich-Goldwasser-Micali）展示了密碼學中哪兩種基本原語的等價轉換？",
    "options": [
      "如何利用偽隨機生成器（PRG）建構出偽隨機函數（PRF）",
      "如何利用公鑰加密建構出數位簽章",
      "如何利用雜湊函數建構出非對稱密碼",
      "如何利用串流密碼建構出一次性密碼"
    ],
    "answer": 0,
    "explanation": "GGM 建構法利用將種子擴展為兩倍長的 PRG，以輸入位元作為樹狀尋訪路徑，遞迴構建出偽隨機函數 PRF，證明了 PRG 可建構出 PRF。",
    "pitfalls": "混淆 CTR 模式（PRF 轉 PRG）與 GGM（PRG 轉 PRF）。",
    "reference": "1.4 Pseudorandomness.pdf, p. 25-28 & Joy Ch. 6.2"
  },
  {
    "id": "q-all-3-2",
    "moduleId": "mod-3",
    "category": "理論推導",
    "question": "根據著名的 Luby-Rackoff 定理，使用獨立隨機輪函數建構的 Feistel 網路，至少需要幾輪（Rounds）才能在理論上保證達到強偽隨機置換（Strong PRP）？",
    "options": [
      "1 輪",
      "2 輪",
      "3 輪",
      "4 輪"
    ],
    "answer": 3,
    "explanation": "Luby-Rackoff 定理指出：(1) 1 輪與 2 輪不安全；(2) 3 輪可達到抗選擇明文攻擊的 PRP；(3) 4 輪則可抵抗同時具有正向加密與反向解密預言機查詢的攻擊者，達成強偽隨機置換（Strong PRP）。",
    "pitfalls": "誤選 3 輪。注意 3 輪只滿足 PRP，要達到 Strong PRP 必須為 4 輪。",
    "reference": "1.4 Pseudorandomness.pdf, p. 45-50 & Joy Ch. 6.6"
  },
  {
    "id": "q-all-3-3",
    "moduleId": "mod-3",
    "category": "引理推導",
    "question": "根據 PRP/PRF 切換引理（Switching Lemma），將分組密碼（PRP）視為偽隨機函數（PRF）使用時，產生的優勢度差距受限於何種邊界？",
    "options": [
      "$\\mathbf{Adv}$ 差距為 0，兩者完全相同",
      "$\\big| \\mathbf{Adv}_{\\mathrm{prp}} - \\mathbf{Adv}_{\\mathrm{prf}} \\big| \\le \\frac{q^2}{2^{n+1}}$（受生日碰撞機率上界限制）",
      "差距是指數級的 $2^n$",
      "差距只取決於金鑰長度與輪數"
    ],
    "answer": 1,
    "explanation": "分組密碼是置換（不允許碰撞），而真隨機函數允許碰撞。區分兩者的唯一機會就是觀察到輸出碰撞，根據生日定理，在 $q$ 次查詢下碰撞機率不超過 $q^2 / 2^{n+1}$。",
    "pitfalls": "誤以為 PRP 與 PRF 沒有任何統計差異，置換無碰撞的特性是其唯一的區分依據。",
    "reference": "The Joy of Cryptography, Ch. 6.4, p. 121 & Slides 1.4"
  },
  {
    "id": "q-all-3-4",
    "moduleId": "mod-3",
    "category": "實務應用",
    "question": "在即時通訊協議（如 Signal）的對稱棘輪（Symmetric Ratchet）機制中，如何達成「前向保密（Forward Secrecy）」？",
    "options": [
      "將所有通訊紀錄上傳至區塊鏈儲存",
      "利用 PRG 單向演進金鑰狀態：$(k_{\\mathrm{next}}, k_{\\mathrm{enc}}) \\leftarrow G(k_{\\mathrm{curr}})$，並立即徹底銷毀 $k_{\\mathrm{curr}}$，使攻擊者即使入侵裝置也無法逆推歷史金鑰",
      "每分鐘向金鑰伺服器下載全新 RSA 私鑰",
      "將密文以明文廣播"
    ],
    "answer": 1,
    "explanation": "對稱棘輪利用 PRG 的單向不可逆性。每次傳訊後狀態推進並銷毀舊狀態，即使當前狀態金鑰遭竊，攻擊者在計算上無法逆推先前的金鑰，保障過往通訊不被解密。",
    "pitfalls": "誤以為前向保密必須隨時向中心伺服器連線更換金鑰。",
    "reference": "The Joy of Cryptography, Ch. 5.5, p. 98"
  },
  {
    "id": "q-all-4-1",
    "moduleId": "mod-4",
    "category": "概念辨析",
    "question": "在選擇明文攻擊（CPA）安全模型下，為何任何確定性加密演算法（Deterministic Encryption）絕對無法達到 IND-CPA 安全？",
    "options": [
      "因為確定性加密的運算速度太慢，無法在多項式時間內完成",
      "因為攻擊者可向加密預言機查詢 $m_0$ 得到 $c_0$，隨後在挑戰階段若收到相同的 $c^*$，即可 100% 斷定 $c^* = \\mathrm{Enc}(m_0)$",
      "因為確定性加密無法加密超過 128 位元的訊息",
      "因為確定性加密會被 Shor 演算法在多項式時間內分解金鑰"
    ],
    "answer": 1,
    "explanation": "在 IND-CPA 遊戲中攻擊者擁有加密預言機。若演算法為確定性，同一明文每次產生的密文必然相同。攻擊者只要預先查詢 $m_0$ 得 $c_0$，若挑戰密文 $c^* = c_0$ 則猜 $b=0$，否則猜 $b=1$，獲勝機率恆為 1，優勢度為 1。因此 IND-CPA 安全加密必須引入隨機性或狀態。",
    "pitfalls": "誤以為是算力不足或金鑰長度問題，這純粹是確定性映射導致的結構性安全缺陷。",
    "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 5-7 & Joy Ch. 7.1"
  },
  {
    "id": "q-all-4-2",
    "moduleId": "mod-4",
    "category": "架構推導",
    "question": "基於 PRF $F$ 建構的 CPA 安全加密方案，密文形式為 $c = \\langle r, F(k, r) \\oplus m \\rangle$。初始化向量 $r$ 的生成方式為何？",
    "options": [
      "固定為全 0 字串",
      "每次加密時獨立均勻隨機抽取（$r \\leftarrow \\{0, 1\\}^\\mathrm{in}$）",
      "將明文 $m$ 進行 SHA-256 雜湊後的結果",
      "直接使用金鑰 $k$"
    ],
    "answer": 1,
    "explanation": "$r$ 必須是隨機均勻抽取的隨機數（IV）。如此一來每次產生的遮罩 $F(k, r)$ 都如同一把全新的一次性金鑰，除非 $r$ 發生碰撞（機率受生日界限制），否則達到可證明 CPA 安全。",
    "pitfalls": "若 $r$ 固定為常數，方案立即退化為確定性加密而瓦解。",
    "reference": "1.5 Chosen-Plaintext Attacks.pdf & Joy Ch. 7.3, p. 135"
  },
  {
    "id": "q-all-4-3",
    "moduleId": "mod-4",
    "category": "方案比較",
    "question": "在對抗 CPA 攻擊時，「隨機化（Randomized）加密」與「狀態化（Stateful / Counter）加密」相比，狀態化加密的最大優勢為何？",
    "options": [
      "狀態化加密不需要金鑰",
      "計數器嚴格單調遞增（$r = 0, 1, 2, \\dots$），保證 Nonce 絕不重複，徹底消除了隨機化方案的生日碰撞風險",
      "狀態化加密可以抵禦量子電腦攻擊",
      "密文長度為 0"
    ],
    "answer": 1,
    "explanation": "隨機化方案在 $q \\approx 2^{n/2}$ 次時會因生日悖論發生 IV 碰撞；而狀態化計數器嚴格遞增，保證在 $2^n$ 次查詢前絕對不會重複，徹底杜絕了碰撞風險。",
    "pitfalls": "誤以為隨機比計數器更好，狀態化在無碰撞上更強，但代價是需安全保存狀態。",
    "reference": "The Joy of Cryptography, Ch. 7.3, p. 138"
  },
  {
    "id": "q-all-4-4",
    "moduleId": "mod-4",
    "category": "概念辨析",
    "question": "「偽隨機密文（Pseudorandom Ciphertexts）」相較於一般的「明文不可區分性（IND-CPA）」具備何種更強的特性？",
    "options": [
      "密文不僅無法辨別明文，且對不知道金鑰的觀察者而言，密文本身與均勻隨機字串在計算上無法區分",
      "密文可以不需要金鑰就能解密",
      "密文永遠具備抗量子特性",
      "密文可以抵禦 Padding Oracle 攻擊"
    ],
    "answer": 0,
    "explanation": "偽隨機密文要求密文外觀與真正的隨機雜訊無法區分，這隱藏了訊息長度特徵、封包格式與協議元數據，提供更高層級的隱匿防護。",
    "pitfalls": "偽隨機密文不等於抗 CCA 攻擊，它依然需要搭配 MAC 才能防範篡改。",
    "reference": "The Joy of Cryptography, Ch. 7.2, p. 133"
  }
];

const GLOSSARY_DATA = [
  {
    "term": "Kerckhoffs's Principle",
    "chinese": "柯克霍夫原則",
    "category": "古典與基礎 (Katz Ch 1 / Joy Ch 1)",
    "definition": "加密演算法必須假設完全公開，系統的安全性必須完全建立在金鑰的保密性之上。",
    "pitfall": "切勿實施『隱蔽式安全（Security through Obscurity）』，私有演算法往往暗藏致命設計漏洞。"
  },
  {
    "term": "Perfect Secrecy",
    "chinese": "完美保密性 / 資訊理論安全",
    "category": "資訊理論 (Katz Ch 2 / Joy Ch 1)",
    "definition": "觀察到密文前後，明文的後驗機率嚴格等於先驗機率：$P[M=m|C=c] = P[M=m]$。即使攻擊者擁有無限算力亦不可破譯。",
    "pitfall": "達成完美保密性必須付出 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 的代價，在實務大規模傳輸中無法實現。"
  },
  {
    "term": "One-Time Pad (OTP)",
    "chinese": "單次密鑰",
    "category": "資訊理論 (Katz Ch 2 / Joy Ch 1)",
    "definition": "Vernam 發明的經典密碼。金鑰長度與明文相同，加密 $c = m \\oplus k$，具備完美保密性，但金鑰嚴禁重複使用。",
    "pitfall": "若金鑰重複使用兩次，$c_1 \\oplus c_2 = m_1 \\oplus m_2$ 會直接消除金鑰並外洩明文。"
  },
  {
    "term": "PPT (Probabilistic Polynomial Time)",
    "chinese": "機率多項式時間",
    "category": "計算複雜度 (Slides 1.2 / Joy Ch 4)",
    "definition": "現實可行攻擊者的運算模型。演算法步數受安全參數多項式限制，可投擲隨機硬幣決定分支。",
    "pitfall": "PPT 排除非現實的指數窮舉（如遍歷 $2^{128}$ 金鑰）。"
  },
  {
    "term": "Negligible Function (negl)",
    "chinese": "可忽略函數",
    "category": "計算複雜度 (Slides 1.2 / Joy Ch 4)",
    "definition": "衰減速度超越任何多項式倒數的函數：對任意 $c>0$，存在 $n_0$ 使得 $n>n_0$ 時 $\\mu(n) < 1/n^c$。",
    "pitfall": "$1/n^{10}$ 衰減很慢不是可忽略函數；$2^{-n}$ 與 $2^{-\\sqrt{n}}$ 才是可忽略函數。"
  },
  {
    "term": "The Hybrid Technique",
    "chinese": "混合證明技術",
    "category": "證明方法 (Joy Ch 2 / Slides 1.2)",
    "definition": "在真實遊戲與目標隨機遊戲間插入序列中間遊戲 $G_0, G_1, \\dots, G_k$，每步僅微調單一元件，透過三角不等式將總優勢度限制在各步驟差異之和。",
    "pitfall": "中間遊戲的總數量 $k$ 必須為多項式大小，否則累積優勢度無法保證可忽略性。"
  },
  {
    "term": "Birthday Bound",
    "chinese": "生日界 / 生日問題機率",
    "category": "機率推導 (Joy Ch 4)",
    "definition": "從大小 $N$ 集合中隨機抽樣 $q$ 次，碰撞機率約為 $q^2 / (2N)$。當 $q \\approx \\sqrt{N}$ 時碰撞機率達約 50%。",
    "pitfall": "64 位元區塊密碼在加密 $2^{32}$ 區塊時即面臨生日碰撞（Sweet32 攻擊），現代應使用 128 位元 AES。"
  },
  {
    "term": "PRG (Pseudorandom Generator)",
    "chinese": "偽隨機生成器",
    "category": "核心原語 (Slides 1.4 / Joy Ch 5)",
    "definition": "確定性演算法，將短種子 $s \\in \\{0, 1\\}^\\lambda$ 擴展為長偽隨機場 $G(s)$，且對任意 PPT 區分器與真隨機不可區分。",
    "pitfall": "PRG 是確定性的，並非真正隨機，但能以短金鑰實現 Pseudo-OTP 加密。"
  },
  {
    "term": "Symmetric Ratchet",
    "chinese": "對稱棘輪",
    "category": "通訊應用 (Joy Ch 5)",
    "definition": "利用 PRG 單向演進狀態金鑰並立即銷毀舊金鑰的機制，實現前向保密（Forward Secrecy）。",
    "pitfall": "只要舊狀態徹底從記憶體抹除，即使當前狀態遭竊，過往通訊紀錄依然無法逆推。"
  },
  {
    "term": "PRF (Pseudorandom Function)",
    "chinese": "偽隨機函數",
    "category": "核心原語 (Slides 1.4 / Joy Ch 6)",
    "definition": "帶金鑰函數族 $F_k$，任何 PPT 攻擊者透過黑盒子預言機查詢時，無法將其與真正均勻隨機的函數區分。",
    "pitfall": "PRF 通常不具備可逆性，輸出允許碰撞。"
  },
  {
    "term": "PRP (Pseudorandom Permutation)",
    "chinese": "偽隨機置換 / 分組密碼",
    "category": "核心原語 (Slides 1.4 / Joy Ch 6)",
    "definition": "雙射（一對一且映成）的函數族 $P_k$，正向與反向皆為多項式時間可計算。為分組密碼（如 AES）的理論抽象。",
    "pitfall": "PRP 不允許碰撞，與 PRF 的差異受限於生日碰撞界（Switching Lemma）。"
  },
  {
    "term": "Strong PRP",
    "chinese": "強偽隨機置換",
    "category": "核心原語 (Slides 1.4 / Joy Ch 6)",
    "definition": "面對能同時查詢正向加密預言機與反向解密預言機的攻擊者，依然無法與隨機置換區分的 PRP。",
    "pitfall": "由 Luby-Rackoff 定理：3 輪 Feistel 僅為 PRP，必須達到 4 輪才可保證 Strong PRP。"
  },
  {
    "term": "IND-CPA",
    "chinese": "選擇明文攻擊不可區分性",
    "category": "安全模型 (Slides 1.5 / Joy Ch 7)",
    "definition": "攻擊者擁有加密預言機查詢權限，給定明文對 $(m_0, m_1)$，無法以顯著優勢猜中挑戰密文由何者加密而成。",
    "pitfall": "任何確定性加密演算法絕對無法達到 IND-CPA 安全，必須引入隨機 IV 或 Nonce 狀態。"
  }
];
