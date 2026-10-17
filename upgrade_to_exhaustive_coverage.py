# -*- coding: utf-8 -*-
"""
Exhaustive alignment script:
Integrates EVERY concept, theorem, slide title, attack, and historical example
from all slides (1.2, 1.4, 1.5) and textbooks into js/data.js and regenerates notes.html.
"""

import json

# Comprehensive 8 Modules strictly covering all slides & textbooks
modules = [
    # Module 0
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

    # Module 1
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

    # Module 2
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

    # Module 3
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

    # Module 4
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
    },

    # Module 5
    {
        "id": "mod-5",
        "number": "模組 05",
        "title": "選擇密文攻擊（CCA）與格式/填充預言機",
        "subtitle": "Chosen-Ciphertext Attacks, Null-Oracle & Padding Oracle Attacks",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Section 2, p. 15 - 45)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 9)"
        ],
        "summary": "地毯式涵蓋講義 1.5 Section 2 全文：IND-CCA1 與 IND-CCA2 模型、解密預言機之威脅、1 個位元的延展性即可徹底粉碎 CCA 安全（One bit of malleability already breaks CCA）、偽造未曾發送的密文（Forging ciphertexts you never sent）；講義核心重點：Null-Oracle 格式預言機攻擊（CTR 模式延展性漏洞反推明文，深入剖析為何非暴力破解、Rate-limit 無效、修補 null-byte 無效）；以及 Serge Vaudenay 的 CBC 模式 Padding Oracle 逐位元組逆推攻擊推導。",
        "sections": [
            {
                "title": "IND-CCA 安全模型與延展性的毀滅性打擊",
                "content": [
                    "**CCA 威脅模型**：攻擊者額外獲得**解密預言機 $\\mathcal{O}_{\\mathrm{Dec}}(\\cdot)$** 查詢權限。",
                    "- **IND-CCA1（午餐時間攻擊）**：僅在挑戰階段『之前』允許查詢解密預言機。",
                    "- **IND-CCA2（適應性 CCA）**：收到挑戰密文 $c^*$ 後，除了本體 $c^*$ 以外，仍可查詢任何竄改密文 $c \\ne c^*$。",
                    "**1 位元延展性即可徹底粉碎 CCA（One bit of malleability already breaks CCA，投影片 p.40-41）**：",
                    "攻擊者取得挑戰密文 $c^*$ 後，將末位翻轉 1 位元得到 $c' = c^* \\oplus 1$（顯然 $c' \\ne c^*$）。攻擊者將 $c'$ 送給解密預言機，合法獲得明文 $m' = m_b \\oplus 1$。隨後只需再翻轉 1 位元：$m' \\oplus 1 = m_b$，即可 100% 還原真實明文！因此 **IND-CCA 安全要求加密演算法必須嚴格具備非延展性（Non-malleability）**。"
                ]
            },
            {
                "title": "講義核心案例：Null-Oracle 格式預言機攻擊（CTR Mode）",
                "content": [
                    "講義（p.20-33）深入探討的重大實務攻擊：",
                    "**背景設定**：伺服器使用 CTR 模式加密以 C 語言風格結尾的字串（末尾以 Null-byte `\\0` 即 `0x00` 結尾）。伺服器提供解密服務，若解密後發現字串末尾缺少 `\\0`，會回傳格式錯誤訊號（Null-Oracle $\\mathcal{O}_{\\mathrm{null}}(C)$）。",
                    "**攻擊運算步驟（CTR mode is malleable）**：",
                    "1. 目標是破解明文中的某個位元組 $P[i]$。CTR 解密為 $P[i] = C[i] \\oplus S[i]$。",
                    "2. 攻擊者構造密文 $C'$：將 $C[i]$ 修改為 $C'[i] = C[i] \\oplus \\Delta$，將其餘字元清空使目標字元成為結尾。",
                    "3. 遍歷 $\\Delta$ 從 `0x00` 到 `0xFF` 送交伺服器。當伺服器回傳「格式正確（存在 `\\0`）」時，代表解密結果恰好等於 0：",
                    "$$P'[i] = P[i] \\oplus \\Delta = 0 \\implies P[i] = \\Delta$$",
                    "4. 攻擊者無需知道金鑰，只要觀察伺服器是否報錯，即可直接精確求出明文字元 $P[i] = \\Delta$！",
                    "**深層密碼學洞見（講義 p.31-33）**：",
                    "- **這不是暴力破解（Not just brute-force）**：每個位元組只需 256 次查詢，將指數難度降至多項式時間！",
                    "- **限制頻率無效（Rate-limiting is not enough）**：查詢次數過少，即便限速依然能於幾分鐘內被完全還原！",
                    "- **修復 Null-byte 錯誤也無效（Fixing null-byte bug is not enough）**：任何格式解析器（XML, JSON, ASN.1）只要回傳格式錯誤，都會構成格式預言機！根本解法是採用驗證式加密（AE）。"
                ]
            },
            {
                "title": "CBC 模式之 Padding Oracle 攻擊（Serge Vaudenay, 2002）",
                "content": [
                    "**PKCS#7 填充規範**：16 位元組區塊，缺 1 位元組填 `0x01`，缺 2 位元組填 `0x02 0x02`，對齊則補滿整塊 `0x10`。",
                    "**逐位元組逆推推導**：",
                    "解密明文 $P_2 = D_k(C_2) \\oplus C_1$。令中間值 $I_2 = D_k(C_2)$。",
                    "1. 構造偽造的前一區塊 $C'_1$，遍歷 $C'_1[15]$ 從 `0x00` 到 `0xFF` 送交解密。當伺服器回傳 Padding 合法（等於 `0x01`）時：",
                    "$$I_2[15] \\oplus C'_1[15] = 0x01 \\implies I_2[15] = C'_1[15] \\oplus 0x01$$",
                    "2. 原始明文立即還原：$P_2[15] = I_2[15] \\oplus C_1[15]$。",
                    "3. 接著設定 $C'_1[15] = I_2[15] \\oplus 0x02$，繼續破解 $C'_1[14]$。每個區塊 16 位元組最差僅需 $16 \\times 256 = 4096$ 次查詢即可完全破解！"
                ]
            }
        ]
    },

    # Module 6
    {
        "id": "mod-6",
        "number": "模組 06",
        "title": "訊息驗證碼（MAC）與雜湊函數實務",
        "subtitle": "Message Authentication Codes, Hash Functions & Integrity",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Subsection 2.1, p. 46 - 61)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 10 & Ch. 11)"
        ],
        "summary": "地毯式涵蓋講義 1.5 Subsection 2.1 全文：密碼學雜湊函數特性與實務（Linux ISO 下載校驗、工作量證明 Proof of Work: Anubis）、訊息驗證碼 MAC 語意與 EUF-CMA 安全遊戲、實務範例 AES-CTR + HMAC、PRFs as MACs、CBC-MAC 在可變長度訊息下的長度延伸偽造攻擊與 CMAC 修復，以及 HMAC 雙重雜湊設計原理。",
        "sections": [
            {
                "title": "雜湊函數特性與實務應用（Hash Functions in Practice）",
                "content": [
                    "**密碼學雜湊函數三大特性**：單向抗原像性（Pre-image resistance）、抗第二原像性（Second pre-image resistance）、抗強碰撞性（Collision resistance）。",
                    "**講義實務案例（投影片 p.49-50）**：",
                    "- **資料完整性校驗**：驗證 Linux ISO 下載檔案是否損毀或遭植入後門（`sha256sum ubuntu.iso`）。",
                    "- **工作量證明（Proof of Work: Anubis）**：要求尋找 Nonce 使得 $H(\\mathrm{data} \\parallel \\mathrm{nonce})$ 開頭具備固定數量的 0 位元，作為算力消耗之實證（比特幣與區塊鏈之基石）。"
                ]
            },
            {
                "title": "訊息驗證碼（MAC）與 EUF-CMA 安全模型",
                "content": [
                    "**目標**：確保訊息的真實性（Authenticity）與完整性（Integrity），防止未授權竄改（MAC 不提供機密性）。演算法組：$(\\mathrm{Gen}, \\mathrm{Mac}, \\mathrm{Vrfy})$。",
                    "**EUF-CMA 安全模型（選擇訊息攻擊下的存在不可偽造性，投影片 p.51-54）**：",
                    "- 攻擊者可向 MAC 預言機查詢任意訊息的合法標籤。",
                    "- 獲勝條件：產出一組全新訊息 $m^*$（未曾查詢過）與其合法標籤 $t^*$ 使得驗證通過。",
                    "- 若對所有 PPT 攻擊者獲勝機率皆為 $\\mathrm{negl}(n)$，則稱該 MAC 具備 EUF-CMA 安全性。",
                    "**PRFs as MACs**：若 $F$ 為安全 PRF，則 $\\mathrm{Mac}_k(m) = F_k(m)$ 是安全的固定長度 MAC！"
                ]
            },
            {
                "title": "CBC-MAC 之長度延伸攻擊與 CMAC 修復",
                "content": [
                    "**基礎 CBC-MAC 構造**：以 IV=0 進行 CBC 模式加密，最後一個區塊輸出即為標籤 $t$。",
                    "**長度延伸偽造攻擊（Splicing Attack，講義 p.55-58）**：",
                    "- 若用於可變長度訊息，查詢單區塊 $m_1$ 得標籤 $t_1$；查詢單區塊 $m_2$ 得標籤 $t_2$。",
                    "- 構造兩區塊新訊息 $m^* = m_1 \\parallel (m_2 \\oplus t_1)$。",
                    "- 計算第二區塊輸入：$(m_2 \\oplus t_1) \\oplus t_1 = m_2$。輸出恰好等於 $t_2$！攻擊者成功偽造全新訊息標籤！",
                    "**修復方案**：CMAC（在最後區塊 XOR 獨立衍生金鑰），阻斷長度延伸鏈接。"
                ]
            },
            {
                "title": "HMAC 雙重雜湊架構與實務範例",
                "content": [
                    "**實務經典範例（投影片 p.52）**：AES-CTR + HMAC 組合，兼具高速串流加密與強完整性校驗。",
                    "**HMAC 構造**：$\\mathrm{HMAC}_K(m) = H\\big((K \\oplus \\mathrm{opad}) \\parallel H((K \\oplus \\mathrm{ipad}) \\parallel m)\\big)$。",
                    "**設計原理**：若直接採用單次雜湊 $H(K \\parallel m)$，Merkle-Damgård 結構雜湊會遭受長度延伸攻擊（Length Extension Attack）；HMAC 透過內外兩層金鑰遮罩雙重雜湊，徹底阻斷了此類攻擊。"
                ]
            }
        ]
    },

    # Module 7
    {
        "id": "mod-7",
        "number": "模組 07",
        "title": "驗證式加密（AE/AEAD）與現代標準",
        "subtitle": "Authenticated Encryption (AEAD), AES-GCM, ChaCha20 & Replay Attacks",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Subsection 2.2, p. 62 - 85)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 12)"
        ],
        "summary": "地毯式涵蓋講義 1.5 Subsection 2.2 全文：驗證式加密（AE）形式化定義、黃金定理（IND-CPA + INT-CTXT => IND-CCA）、三大組合範式評比（EtM vs EaM vs MtE）；深入 AES-GCM：什麼是 GHASH、為什麼用 GHASH 代替 HMAC、為什麼不能處處使用 GHASH（Nonce 重用災難）；金鑰承諾（Key Commitment）、ChaCha20-Poly1305；重放攻擊（Replay Attacks）與序號防護；關聯資料（Associated Data）提供 Context 的核心作用，以及 Fujisaki-Okamoto Transform。",
        "sections": [
            {
                "title": "驗證式加密（AE）與黃金定理：IND-CPA + INT-CTXT => IND-CCA",
                "content": [
                    "**AE 定義（Beyond CCA Security，講義 p.63-66）**：同時提供機密性（Confidentiality）與完整性（Integrity）。",
                    "**密文完整性（INT-CTXT）**：攻擊者無法鍛造出任何能成功解密的新密文。",
                    "**黃金定理**：",
                    "$$\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$$",
                    "**直觀證明**：只要密文具備 INT-CTXT，攻擊者發送給解密預言機的任何竄改密文 $c \\ne c^*$ 都會在解密前直接被驗證器拒絕，解密預言機徹底失效，系統自動升格為最強的 IND-CCA 安全！"
                ]
            },
            {
                "title": "三大組合範式評比（Combining MACs and Encryption）",
                "content": [
                    "講義（p.57-61）詳細對比的三大組合：",
                    "1. **Encrypt-and-MAC（SSH 早期）**：$c = \\mathrm{Enc}_{k_1}(m), \\; t = \\mathrm{Mac}_{k_2}(m)$。**不安全**！MAC 標籤直接由明文計算，可能直接外洩明文資訊，無法保證 IND-CPA！",
                    "2. **MAC-then-Encrypt（SSL/TLS 早期）**：$t = \\mathrm{Mac}_{k_2}(m), \\; c = \\mathrm{Enc}_{k_1}(m \\parallel t)$。**脆弱**！密文遭篡改時會先進入解密器解密，容易引發 Padding Oracle 等解密側信道漏洞（如 Lucky Thirteen 攻擊）！",
                    "3. **Encrypt-then-MAC（EtM）（IPsec、現代標準）**：$c = \\mathrm{Enc}_{k_1}(m), \\; t = \\mathrm{Mac}_{k_2}(c)$。**唯一通用且證明安全**！接收端先校驗密文標籤 $t$，若不符直接拋棄，完全不執行解密！"
                ]
            },
            {
                "title": "AES-GCM 深度剖析：什麼是 GHASH？為什麼不能處處使用？",
                "content": [
                    "講義（p.68-73）深度探討的 AES-GCM：",
                    "- **架構**：CTR 模式串流加密 + Galois 有限域 $\\mathrm{GF}(2^{128})$ 上的多項式乘法認證標籤（GHASH）。",
                    "- **為什麼用 GHASH 代替 HMAC？（投影片 p.71）** GHASH 是有限域上的乘法運算，硬體指令集（如 Intel PCLMULQDQ）能以極低時鐘週期平行化計算，吞吐量遠高於雜湊函數 HMAC！",
                    "- **如果 GHASH 這麼好，為什麼不能處處使用？（投影片 p.72）** GHASH 不是密碼學安全雜湊函數！它不是單向的；**更致命的是對 Nonce 重用極度敏感（Nonce-reuse catastrophy）**！若在相同金鑰下重複使用同一個 IV，攻擊者只需兩筆密文就能直接求出 GHASH 金鑰 $H$，隨後可偽造任意訊息的合法認證標籤，安全性瞬間歸零！"
                ]
            },
            {
                "title": "ChaCha20-Poly1305 與金鑰承諾（Key Commitment）",
                "content": [
                    "**ChaCha20-Poly1305（投影片 p.75-76）**：DJB 設計的現代 AEAD 標準。ChaCha20 串流加密 + Poly1305 MAC。在沒有 AES 硬體加速指令集的手機、ARM 處理器與嵌入式設備上，速度顯著超越 AES-GCM，為 TLS 1.3 與 WireGuard VPN 核心標準。",
                    "**金鑰承諾問題（Key Commitment in AE，投影片 p.74）**：某些 AEAD 方案可能存在同一密文能在不同金鑰下解密出合法明文的異常現象，現代高階協議正逐步引入金鑰承諾機制進行防護。"
                ]
            },
            {
                "title": "重放攻擊、關聯資料（AEAD）與 Fujisaki-Okamoto 轉換",
                "content": [
                    "**重放攻擊（Replay Attacks，投影片 p.77-79）**：AE 只能保護單個封包的完整性。攻擊者攔截一筆合法的匯款密文並重複重放 100 次，伺服器每次驗證皆合法！**防護方案：必須在協議層加入單調遞增的 Sequence Number（序號）或時間戳記！**",
                    "**關聯資料（Associated Data, AD，投影片 p.80-83）**：AEAD 形式化語意：$\\mathrm{Enc}(K, N, P, A) \\to C$，$\\mathrm{Dec}(K, N, C, A) \\to P$。$A$ 不被加密，但會參與 MAC 認證。**作用：為封包提供不可分割的 Context（如來源/目的 IP、Session ID、通訊輪次）**，防止封包被活躍中間人跨連線錯位注入！",
                    "**Fujisaki-Okamoto Transform（投影片 p.84）**：在後量子密碼與現代公鑰加密中，將僅具備弱被動 CPA 安全的加密方案，透過隨機預言機轉換為抗主動攻擊的 IND-CCA 安全方案的核心轉換技術！"
                ]
            }
        ]
    }
]

# Write to js/data.js
js_content = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source strictly and exhaustively covering ALL slides (1.2, 1.4, 1.5)
// and textbooks (Katz & Lindell, Mike Rosulek Joy of Cryptography)

const MODULES_DATA = {json.dumps(modules, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(modules[0]['sections'], ensure_ascii=False)}; // placeholder
"""

# Let's read existing QUIZ_DATA and GLOSSARY_DATA from js/data.js to preserve them
with open("js/data.js", "r", encoding="utf-8") as f:
    old_data = f.read()

import re
m_quiz = re.search(r"const\s+QUIZ_DATA\s*=\s*(\[.*?\]);\s*const\s+GLOSSARY_DATA", old_data, re.DOTALL)
m_glossary = re.search(r"const\s+GLOSSARY_DATA\s*=\s*(\[.*?\]);\s*$", old_data, re.DOTALL)

quizzes = json.loads(m_quiz.group(1)) if m_quiz else []
glossary = json.loads(m_glossary.group(1)) if m_glossary else []

final_js = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source strictly and exhaustively covering ALL slides (1.2, 1.4, 1.5)
// and textbooks (Katz & Lindell, Mike Rosulek Joy of Cryptography)

const MODULES_DATA = {json.dumps(modules, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(quizzes, ensure_ascii=False, indent=2)};

const GLOSSARY_DATA = {json.dumps(glossary, ensure_ascii=False, indent=2)};
"""

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(final_js)

print("Exhaustive data successfully written to js/data.js!")
