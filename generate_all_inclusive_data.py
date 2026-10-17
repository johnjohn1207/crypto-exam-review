# -*- coding: utf-8 -*-
"""
Generate comprehensive data for Cryptography Learning Platform
Integrating ALL 6 PDFs present in the directory:
1. Introduction to Modern Cryptography - Historical Ciphers and Their Cryptanalysis (1).pdf
2. Introduction to Modern Cryptography - Perfectly Secret Encryption (1).pdf
3. 1.2 The Provable Security Mindset.pdf
4. 1.4 Pseudorandomness.pdf
5. 1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf
6. Cyrptography.pdf (The Joy of Cryptography by Mike Rosulek: Ch 0, 1, 2, 4, 5, 6, 7)
"""

import json

all_modules = [
    # Module 0
    {
        "id": "mod-all-0",
        "number": "模組 00",
        "title": "古典密碼學、密碼分析與離散數學基石",
        "subtitle": "Historical Ciphers, Cryptanalysis & Discrete Math Foundations",
        "sources": [
            "Introduction to Modern Cryptography - Historical Ciphers and Their Cryptanalysis (1).pdf (Katz & Lindell, Ch. 1)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 0: Review of Concepts & Notation, p. 1 - 9)"
        ],
        "summary": "融合 Katz & Lindell 的古典替換/移位密碼分析與 Mike Rosulek 的離散數學基石：柯克霍夫原則（Kerckhoffs's Principle）、凱撒密碼、單字母替換、維吉尼亞多表密碼、頻率分析、卡西斯基檢驗法、重合指數（IC），以及模運算（負數模除與化簡技巧）、二進位 XOR 四大性質、函數分類（單射/映成/雙射）與聯集上界機率論。",
        "sections": [
            {
                "title": "柯克霍夫原則與密碼學假設邊界",
                "content": [
                    "**Kerckhoffs's Principle（柯克霍夫原則）**：加密系統的安全性絕不能依賴演算法的保密（Security through Obscurity），而必須完全建立在金鑰（Secret Key）的保密之上。這也是現代密碼學「開放演算法、嚴守金鑰」的鐵律。",
                    "**密碼學防範與不防範之範疇**：密碼學保護在開放或惡意中間人（Eve）竊聽/竄改通道下的傳輸安全；密碼學無法防範終端惡意軟體側信道鍵擊記錄、使用者社交工程或實體伺服器被盜。"
                ]
            },
            {
                "title": "三大古典密碼機制與破譯推導",
                "content": [
                    "**1. 凱撒移位密碼（Shift Cipher / Caesar Cipher）**：",
                    "- 定義於 $\\mathbb{Z}_{26}$，金鑰 $k \\in \\{0, \\dots, 25\\}$。加密 $c = (m + k) \\pmod{26}$，解密 $m = (c - k) \\pmod{26}$。",
                    "- 漏洞：金鑰空間 $|\\mathcal{K}| = 26$，只需嘗試 26 次暴力窮舉即可瞬間破解。",
                    "**2. 單字母替換密碼（Monoalphabetic Substitution Cipher）**：",
                    "- 金鑰為 26 個字母之置換排列，金鑰空間 $|\\mathcal{K}| = 26! \\approx 4 \\times 10^{26}$（大於 88 位元，無法暴力窮舉）。",
                    "- 漏洞：明文字母與密文字母維持固定一對一映射，完全保留了自然語言的統計頻率分佈（例如英文中 'E' 出現率約 12.7%，'T' 約 9.1%），透過單字母頻率分析可在數分鐘內手動解密！",
                    "**3. 維吉尼亞多表密碼（Vigenère Cipher）**：",
                    "- 金鑰為長度 $t$ 之字串 $k = (k_1, \\dots, k_t)$，依序對明文進行循環移位：$c_i = (m_i + k_{(i \\% t)}) \\pmod{26}$。",
                    "- **卡西斯基檢驗法（Kasiski Examination）**：尋找長度 $\\ge 3$ 之重複密文字串，計算其出現位置之間距，所有間距之最大公因數（GCD）高機率即為金鑰週期長度 $t$。",
                    "- **重合指數（Index of Coincidence, IC）**：隨機抽取兩字母相同的機率：$\\mathrm{IC} = \\sum \\frac{f_i(f_i-1)}{N(N-1)}$。隨機均勻文字 $\\mathrm{IC} \\approx 0.038$，英語文本 $\\mathrm{IC} \\approx 0.065$。若分組週期猜測正確，子密文保留英語特性，其 IC 必然飆升至約 $0.065$。"
                ]
            },
            {
                "title": "密碼學必備離散數學基石（Joy of Cryptography Ch. 0）",
                "content": [
                    "**指數與對數禁忌**：$(x^a)(x^b) = x^{a+b}$、$(x^a)^b = x^{ab}$。嚴禁寫出 $(x^a)(x^b) = x^{ab}$，底數相同時冪次是相加而非相乘。",
                    "**模除運算子（% Operator）之非負性**：$a \\% n$ 定義為唯一的餘數 $r \\in \\{0, \\dots, n-1\\}$ 滿足 $n \\mid (a - r)$。**關鍵：無論 $a$ 為正或負，$a \\% n$ 恆非負**！例如 $20 \\% 7 = 6$、$-20 \\% 7 = 1$（因為 $-20 = -3 \\times 7 + 1$）、$-1 \\% 7 = 6$。",
                    "**同餘 $\\equiv_n$ 與整數相等之嚴格差異**：$a \\equiv_n b$ 兩邊可為任意大小與符號的整數；而 $a = b \\% n$ 是整數相等，右側必在 $\\{0, \\dots, n-1\\}$。例如 $99 \\equiv_{10} 19$ 為真，但 $99 = 19 \\% 10$ 為假（$19 \\% 10 = 9 \\ne 99$）。",
                    "**歐幾里得最大公因數演算法（GCD）**：$\\gcd(x, y) = \\gcd(y, x \\% y)$。若 $\\gcd(x, y) = 1$ 則兩者互質。",
                    "**字串與 XOR 四大代數基石**：交換律、結合律、單位元（$x \\oplus 0 = x$）、自相反身性（$x \\oplus x = 0$ 且 $(x \\oplus y) \\oplus y = x$）。自相反身性是對稱密碼能夠使用相同電路加解密的核心依據。",
                    "**函數映射與置換**：單射（$|X| \\le |Y|$）、映成（$|X| \\ge |Y|$）、雙射（$|X|=|Y|$ 且存在反函數 $f^{-1}$）。有限集合上的雙射即為置換（Permutation），為分組密碼之數學本質。",
                    "**機率與聯集上界（Union Bound）**：均勻隨機抽取 $\\leftarrow$、條件機率 $P[A \\mid B]$。對任意 $k$ 個事件（無論彼此是否獨立），恆有 $P[\\bigcup_{i=1}^k E_i] \\le \\sum_{i=1}^k P[E_i]$。"
                ]
            }
        ]
    },

    # Module 1
    {
        "id": "mod-all-1",
        "number": "模組 01",
        "title": "完美保密性、單次密鑰與金鑰極限",
        "subtitle": "Perfect Secrecy, One-Time Pad & Shannon's Theorem",
        "sources": [
            "Introduction to Modern Cryptography - Perfectly Secret Encryption (1).pdf (Katz & Lindell, Ch. 2)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 1: One-Time Pad & Kerckhoffs' Principle, p. 10 - 20)"
        ],
        "summary": "探討 Shannon 提出之資訊理論完美保密性（後驗等於先驗機率）、Vernam 單次密鑰（One-Time Pad）的數學證明、Shannon 不可能定理（|K| >= |M|），以及金鑰重複使用時的 Two-Time Pad 致命漏洞與延展性位元翻轉攻擊。",
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
                "title": "Shannon 不可能定理（Shannon's Impossibility Theorem）",
                "content": [
                    "**定理內容**：任何滿足完美保密性的加密系統，其金鑰空間必須大於或等於明文空間：",
                    "$$|\\mathcal{K}| \\ge |\\mathcal{M}|$$",
                    "對於二進位字串，金鑰長度必須至少與明文一樣長（$\\ell_K \\ge \\ell_M$）。",
                    "**反證法推導**：若 $|\\mathcal{K}| < |\\mathcal{M}|$，給定密文 $c$，由 $c$ 可能解密出的明文集合 $\\mathcal{M}(c) = \\{\\mathrm{Dec}_k(c) \\mid k \\in \\mathcal{K}\\}$ 大小最多僅 $|\\mathcal{K}|$ 個，必定存在某個明文 $m^* \\in \\mathcal{M}$ 永遠無法由 $c$ 解出（$P[M = m^* \\mid C = c] = 0 \\ne P[M = m^*]$），矛盾！故 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 必然成立。",
                    "**實務代價**：要加密 1 TB 資料必須預先安全傳輸 1 TB 隨機金鑰，且金鑰嚴禁重複使用，使得 OTP 在大規模實務傳輸中極度受限。"
                ]
            },
            {
                "title": "實務致命漏洞：Two-Time Pad 攻擊與延展性",
                "content": [
                    "**1. Two-Time Pad 攻擊（金鑰重用的災難）**：",
                    "- 若以同一金鑰 $k$ 加密兩條訊息 $m_1, m_2$：$c_1 = m_1 \\oplus k, \\; c_2 = m_2 \\oplus k$。",
                    "- 密文相異或：$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$。金鑰完全抵消！",
                    "- **ASCII 特徵破譯**：ASCII 英文字母前 3 位為 `010` 或 `011`，空白鍵為 `0x20`（`00100000`）。字母與空白鍵 XOR 會翻轉大小寫，非空白鍵互斥或會產生小於 `0x40` 的值。攻擊者利用 Crib Dragging 技術可迅速全數還原明文！",
                    "**2. 延展性（Malleability / Bit-flipping Attack）**：",
                    "- 中間人修改密文為 $c' = c \\oplus \\Delta$，解密明文為 $m' = c' \\oplus k = (c \\oplus k) \\oplus \\Delta = m \\oplus \\Delta$。攻擊者可在不知道金鑰與明文下精準操縱明文特定位元翻轉。**OTP 僅保護機密性，完全不具備完整性！**"
                ]
            }
        ]
    },

    # Module 2
    {
        "id": "mod-all-2",
        "number": "模組 02",
        "title": "可證明安全性思維與計算密碼學基礎",
        "subtitle": "The Provable Security Mindset, Computational Foundations & Hybrid Technique",
        "sources": [
            "1.2 The Provable Security Mindset.pdf (劉子源教授講義, 62 頁)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 2: Basics of Provable Security & Ch. 4: Intractable Computations)"
        ],
        "summary": "融合講義 1.2 與 Joy of Cryptography Ch. 2/4：計算安全性的兩大放寬（PPT 算力限制與 Negligible 函數）、安全遊戲範式（Left-vs-Right 與 Real-vs-Random 風格）、優勢度（Advantage）定義、示範不安全性的標準攻擊步驟、核心證明武器：混合證明技術（The Hybrid Technique），以及生日問題機率（Birthday Bound）與計算不可區分性。",
        "sections": [
            {
                "title": "計算安全性的兩大鬆綁與數學定義",
                "content": [
                    "為突破 Shannon 定理 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 的限制，計算密碼學做出兩大務實假設：",
                    "1. **運算資源限制（PPT 模型）**：攻擊者算力受限於安全參數 $n$ 的機率多項式時間（Probabilistic Polynomial Time, PPT），排除非現實的指數窮舉（如遍歷 $2^{128}$ 金鑰）。",
                    "2. **成功機率容許（Negligible 函數）**：允許攻擊者以可忽略函數 $\\mathrm{negl}(n)$ 的微小機率成功。",
                    "**可忽略函數嚴格定義**：對任意多項式次方 $c > 0$，皆存在臨界值 $n_0$，使得當 $n > n_0$ 時均有 $\\mu(n) < 1/n^c$。例如 $2^{-n}$、$2^{-\\sqrt{n}}$ 為可忽略函數；而 $n^{-10}$、$1/\\log n$ 則非可忽略函數。"
                ]
            },
            {
                "title": "安全遊戲範式與不可區分性（Security Games）",
                "content": [
                    "安全定義由挑戰者（Challenger）與攻擊者 $\\mathcal{A}$ 進行形式化互動遊戲：",
                    "**兩大主流風格**：",
                    "1. **Left-vs-Right 風格**：攻擊者提交 $(m_0, m_1)$，Challenger 擲硬幣 $b \\leftarrow \\{0, 1\\}$ 加密回傳 $m_b$。攻擊者輸出 $b'$。",
                    "2. **Real-vs-Random 風格**：攻擊者提交 $m$，Challenger 在 Real 遊戲中回傳真實密文 $\\mathrm{Enc}(k, m)$，在 Random 遊戲中回傳長度相同的純隨機字串 $r \\leftarrow \\{0, 1\\}^\\ell$。",
                    "**優勢度（Advantage）數學定義**：",
                    "$$\\mathbf{Adv}(\\mathcal{A}) = \\big| P[\\mathcal{A} \\text{ outputs 1 in Game 0}] - P[\\mathcal{A} \\text{ outputs 1 in Game 1}] \\big|$$",
                    "若對所有 PPT 攻擊者均有 $\\mathbf{Adv}(\\mathcal{A}) \\le \\mathrm{negl}(n)$，則稱該方案在該模型下可證明安全。"
                ]
            },
            {
                "title": "示範不安全性的攻擊三步驟（Demonstrating Insecurity）",
                "content": [
                    "若要嚴謹證明某機制不安全，必須提出攻擊實例：",
                    "1. 寫出具體的多項式時間攻擊者演算法 $\\mathcal{A}$ 之虛擬碼。",
                    "2. 分別推導並計算 $\\mathcal{A}$ 在 Game 0 與 Game 1 中輸出 1 的精確機率數值。",
                    "3. 計算優勢度絕對值，展示 $\\mathbf{Adv}(\\mathcal{A})$ 為顯著非可忽略數值（如 1 或 0.5）。"
                ]
            },
            {
                "title": "核心證明武器：混合證明技術（The Hybrid Technique）",
                "content": [
                    "**運作機制**：當真實遊戲 $G_0$ 與目標隨機遊戲 $G_k$ 差異過大時，構造中間遊戲序列 $G_0, G_1, \\dots, G_k$。每相鄰兩遊戲 $G_i$ 與 $G_{i+1}$ 之間只有單一微小步驟差異（如替換一個金鑰或一個隨機數）。",
                    "**三角不等式上界推導**：",
                    "$$\\big| P[G_0] - P[G_k] \\big| \\le \\sum_{i=0}^{k-1} \\big| P[G_i] - P[G_{i+1}] \\big|$$",
                    "只要中間步驟數量 $k$ 為多項式大小，且每步之不可區分性皆能歸約到底層難題，則總優勢度必然為可忽略數值！"
                ]
            },
            {
                "title": "生日問題機率與抽樣邊界（Birthday Bound）",
                "content": [
                    "從大小為 $N$ 的集合中進行 $q$ 次隨機抽樣，發生碰撞的機率近似為 $P[\\text{Collision}] \\approx q^2 / (2N)$。",
                    "**臨界值 $q \\approx \\sqrt{N}$**：64 位元區塊密碼在加密約 $2^{32} \\approx 40$ 億個區塊（約 32 GB）時即有 50% 機率發生碰撞，瓦解 CBC 安全性（Sweet32 攻擊）；現代 AES 採用 128 位元區塊（碰撞門檻高達 $2^{64}$ 區塊）確保安全。"
                ]
            }
        ]
    },

    # Module 3
    {
        "id": "mod-all-3",
        "number": "模組 03",
        "title": "偽隨機性與原語建構理論",
        "subtitle": "Pseudorandomness: PRG, PRF, PRP & Block Ciphers",
        "sources": [
            "1.4 Pseudorandomness.pdf (劉子源教授講義, 60 頁)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 5: PRG & Ch. 6: PRF and Block Ciphers)"
        ],
        "summary": "融合講義 1.4 與 Joy of Cryptography Ch. 5/6：深入偽隨機生成器（PRG）、偽隨機函數（PRF）與偽隨機置換（PRP/分組密碼）三大核心原語。剖析 Pseudo-OTP 構造、Blum-Micali 伸展定理、對稱棘輪（Symmetric Ratchet）前向保密、GGM 樹狀建構（PRG -> PRF）、CTR 模式（PRF -> PRG）、PRP/PRF 切換引理，以及 Feistel 網路與 Luby-Rackoff 定理（3 輪達 PRP，4 輪達 Strong PRP）。",
        "sections": [
            {
                "title": "三大核心原語定義與安全性",
                "content": [
                    "**1. 偽隨機生成器（PRG）**：確定性演算法 $G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + \\ell}$（$\\ell > 0$），將短隨機種子伸展為長字串，對任何 PPT 區分器而言與真隨機不可區分：$\\mathbf{Adv}_{\\mathrm{prg}}(\\mathcal{D}) \\le \\mathrm{negl}(\\lambda)$。",
                    "**2. 偽隨機函數（PRF）**：金鑰化函數族 $F: \\{0, 1\\}^\\lambda \\times \\{0, 1\\}^\\mathrm{in} \\to \\{0, 1\\}^\\mathrm{out}$。攻擊者透過黑盒子查詢，無法區分面對的是 $F(k, \\cdot)$ 還是真正均勻隨機的函數 $\\mathrm{RF}(\\cdot)$。",
                    "**3. 偽隨機置換（PRP / 分組密碼）**：雙射（一對一且映成）的置換族 $P: \\{0, 1\\}^\\lambda \\times \\{0, 1\\}^n \\to \\{0, 1\\}^n$，具備高效率正向與反向運算 $P^{-1}$。為 AES 等現代分組密碼的抽象理論模型。"
                ]
            },
            {
                "title": "PRG 應用：Pseudo-OTP 與對稱棘輪",
                "content": [
                    "**Pseudo-OTP 加密**：$c = m \\oplus G(k)$，金鑰長度僅需種子長度。透過 Hybrid Technique 將 $G(k)$ 替換為真隨機字串，歸約至 OTP，證明其具備計算安全性！",
                    "**Blum-Micali 擴展定理**：輸出多 1 位元的 PRG（$G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + 1}$）即可級聯構造出任意多項式長度之 PRG。",
                    "**對稱棘輪（Symmetric Ratchet）與前向保密（Forward Secrecy）**：",
                    "- 狀態推進：$(k_{\\mathrm{next}}, k_{\\mathrm{enc}}) \\leftarrow G(k_{\\mathrm{curr}})$，並立即銷毀舊狀態。",
                    "- 即使攻擊者在時間點 $T$ 竊取設備當前金鑰，受限於 PRG 單向性，攻擊者**完全無法逆推歷史金鑰**，過往歷史通訊紀錄依然絕對保密（此為 Signal 與現代通訊軟體核心機制）。"
                ]
            },
            {
                "title": "原語相互建構與切換引理（Switching Lemma）",
                "content": [
                    "**CTR 模式（PRF $\\to$ PRG）**：令 $G(k) = F(k, 0) \\parallel F(k, 1) \\parallel F(k, 2) \\dots$，將短金鑰展開為無限隨機串流。",
                    "**GGM 樹狀構造（PRG $\\to$ PRF）**：利用將種子長度加倍的 PRG，以輸入位元尋訪二元樹路徑，葉節點即為 $F_k(x)$，採用 Variable-Hybrid 技術證明安全。",
                    "**PRP/PRF 切換引理（Switching Lemma）**：分組密碼（PRP）是置換（不允許碰撞），而真隨機函數允許碰撞。在進行 $q$ 次查詢時，兩者的優勢度差異受限於生日碰撞機率：",
                    "$$\\big| \\mathbf{Adv}_{\\mathrm{prp}} - \\mathbf{Adv}_{\\mathrm{prf}} \\big| \\le \\frac{q(q-1)}{2 \\cdot 2^n} \\le \\frac{q^2}{2^{n+1}}$$",
                    "只要查詢次數 $q \\ll 2^{n/2}$，分組密碼即可安全地當作理想 PRF 使用！"
                ]
            },
            {
                "title": "Feistel 網路與 Luby-Rackoff 定理",
                "content": [
                    "每輪計算 $L_{i+1} = R_i, \\; R_{i+1} = L_i \\oplus F_{k_i}(R_i)$。即使輪函數 $F$ 不可逆，Feistel 網路解密天然對稱可逆。",
                    "**Luby-Rackoff 定理之輪數里程碑**：",
                    "- **1 輪與 2 輪**：絕不安全，存在顯著多項式區分器。",
                    "- **3 輪 Feistel**：可證明達成抗選擇明文攻擊的偽隨機置換（PRP）。但在面對能查詢反向預言機 $P^{-1}$ 的攻擊者時會被攻破！",
                    "- **4 輪 Feistel**：面對同時具備正向加密與反向解密查詢的攻擊者，依然滿足不可區分性，達成**強偽隨機置換（Strong PRP）**！"
                ]
            }
        ]
    },

    # Module 4
    {
        "id": "mod-all-4",
        "number": "模組 04",
        "title": "選擇明文攻擊（CPA）與加密模式",
        "subtitle": "Chosen-Plaintext Attacks & Modes of Operation",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Section 1)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 7: Security Against CPA)"
        ],
        "summary": "融合講義 1.5 Section 1 與 Joy of Cryptography Ch. 7：深入 IND-CPA 安全遊戲模型，揭示確定性加密（如 ECB 模式）為何被 100% 攻破，剖析基於 PRF 之隨機化加密方案（c = <r, F_k(r) XOR m>）與其安全性證明推導，比較狀態化（Stateful / Counter）與隨機化（Randomized）之工程權衡，並探討偽隨機密文（Pseudorandom Ciphertexts）。",
        "sections": [
            {
                "title": "IND-CPA 遊戲與確定性加密的結構性死穴",
                "content": [
                    "**CPA 威脅模型**：攻擊者手握加密預言機 $\\mathcal{O}_{\\mathrm{Enc}}(\\cdot)$，可任意取得其挑選之明文的對應密文。",
                    "**確定性加密（Deterministic Encryption）的致命缺陷**：",
                    "- 若演算法對相同明文始終產出相同密文：",
                    "- 攻擊者向預言機查詢 $m_0$ 取得密文 $c_0 = \\mathrm{Enc}(k, m_0)$。",
                    "- 在挑戰階段送出 $(m_0, m_1)$，接收挑戰密文 $c^*$。",
                    "- 若 $c^* == c_0$，攻擊者 100% 確定 $b=0$，否則 $b=1$。勝率為 100%（$\\mathbf{Adv} = 1$）！",
                    "- **核心定理：任何確定性加密演算法絕對無法達成 IND-CPA 安全！** IND-CPA 安全加密必須具備隨機性（Randomized）或維護內部狀態（Nonce / IV）。"
                ]
            },
            {
                "title": "基於 PRF 之隨機化 CPA 安全加密構造與證明",
                "content": [
                    "設 $F$ 為安全 PRF，金鑰為 $k$：",
                    "- **加密**：要加密明文 $m$，均勻隨機挑選初始化向量 $r \\leftarrow \\{0, 1\\}^\\mathrm{in}$，輸出密文對：",
                    "$$c = \\langle r, \\; F(k, r) \\oplus m \\rangle$$",
                    "- **解密**：$m = c_1 \\oplus F(k, r)$。",
                    "**安全性推導（The Hybrid Technique 應用）**：",
                    "1. **Game 0**：真實 CPA 遊戲，密文遮罩為 $F(k, r)$。",
                    "2. **Game 1**：將 PRF 替換為真正隨機函數 $\\mathrm{RF}$。兩者之差受限於 $\\mathbf{Adv}_{\\mathrm{prf}}$。",
                    "3. **Game 2**：在隨機函數下，只要隨機選取的 $r$ 沒有發生碰撞，每個 $F(k, r)$ 皆為全新的一次性隨機金鑰。由生日界可知 $q$ 次查詢碰撞機率小於 $q^2 / (2 \\cdot 2^\\mathrm{in})$。",
                    "4. 在無碰撞情況下，密文相當於 One-Time Pad，攻擊者優勢度嚴格為 0！故方案在 $q \\ll 2^{\\mathrm{in}/2}$ 下具備可證明 CPA 安全性！"
                ]
            },
            {
                "title": "狀態化（Stateful / Counter）vs 隨機化（Randomized）",
                "content": [
                    "**隨機化（Randomized）**：每次抽取隨機 IV $r$。優點為無需持久化狀態，缺點為密文變長且存在生日碰撞風險（$2^{n/2}$ 區塊後可能碰撞）。",
                    "**狀態化（Stateful / Counter）**：雙方維護嚴格單調遞增的計數器 Nonce（$r = 0, 1, 2, \\dots$）。優點為保證 Nonce 絕不重複，徹底消除生日碰撞，在 $2^n$ 次查詢前均絕對安全；缺點為若系統斷電重置導致計數器回退，將引發金鑰重用災難。"
                ]
            },
            {
                "title": "偽隨機密文（Pseudorandom Ciphertexts）",
                "content": [
                    "更強的安全屬性：密文在多項式時間內與純隨機二進位雜訊不可區分。",
                    "達成偽隨機密文能夠徹底隱藏封包長度、格式、協議元數據特徵，有效防範流量深度檢測（DPI）與側信道分析。"
                ]
            }
        ]
    },

    # Module 5
    {
        "id": "mod-all-5",
        "number": "模組 05",
        "title": "選擇密文攻擊（CCA）與填充預言機攻擊",
        "subtitle": "Chosen-Ciphertext Attacks & The Padding Oracle Attack",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Section 2)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 9: Chosen Ciphertext Attacks)"
        ],
        "summary": "深入 IND-CCA1（午餐時間攻擊）與 IND-CCA2（適應性選擇密文攻擊）安全模型，剖析解密預言機之威脅與延展性帶來的毀滅性後果，並一步步深度解析 Serge Vaudenay 提出的 CBC 模式 Padding Oracle 逐位元組逆推攻擊推導與運算細節。",
        "sections": [
            {
                "title": "IND-CCA 安全模型與解密預言機（Decryption Oracle）",
                "content": [
                    "**CCA 威脅模型**：攻擊者額外獲得**解密預言機 $\\mathcal{O}_{\\mathrm{Dec}}(\\cdot)$** 查詢權限，能模擬活躍中間人篡改密文並觀察接收端反應。",
                    "**IND-CCA1 vs IND-CCA2**：",
                    "- **IND-CCA1（非適應性 / Lunchtime Attack）**：攻擊者僅能在挑戰階段『之前』查詢解密預言機；收到挑戰密文 $c^*$ 後，解密預言機立即關閉。",
                    "- **IND-CCA2（適應性選擇密文攻擊）**：攻擊者在收到挑戰密文 $c^*$『之後』，依然能向解密預言機查詢任何非本體的密文 $c \\ne c^*$！",
                    "**延展性為何徹底粉碎 CCA 安全**：若加密具備延展性，攻擊者將挑戰密文 $c^*$ 翻轉一位得到 $c' = c^* \\oplus \\Delta$（顯然 $c' \\ne c^*$），送給解密預言機合法解密得 $m' = m_b \\oplus \\Delta$，再計算 $m' \\oplus \\Delta = m_b$，即可 100% 還原明文！因此 **IND-CCA 要求加密演算法必須嚴格具備非延展性（Non-malleability）**。"
                ]
            },
            {
                "title": "CBC 模式之 Padding Oracle 攻擊（Serge Vaudenay, 2002）",
                "content": [
                    "**PKCS#7 填充規範**：分組大小若為 16 位元組，若明文缺 1 位元組則填充 `0x01`；缺 2 位元組填充 `0x02 0x02`；若剛好對齊 16 位元組，則補上一整塊全為 `0x10` 的填充塊。",
                    "**預言機洩漏漏洞**：伺服器若解密後發現 PKCS#7 格式不正確，會回傳 Padding Error（或產生特定時間差）。",
                    "**逐位元組逆推運算推導**：",
                    "設目標密文區塊為 $C_2$，前一區塊為 $C_1$。解密明文為 $P_2 = D_k(C_2) \\oplus C_1$。令中間值 $I_2 = D_k(C_2)$。",
                    "1. 攻擊者構造偽造的前一區塊 $C'_1$。欲破解最後一位元組 $P_2[15]$：",
                    "2. 構造 $C'_1[15]$ 從 `0x00` 到 `0xFF`，送交伺服器。當伺服器回傳「填充正確」時，代表解密末尾等於 `0x01`：",
                    "$$I_2[15] \\oplus C'_1[15] = 0x01 \\implies I_2[15] = C'_1[15] \\oplus 0x01$$",
                    "3. 計算出中間值 $I_2[15]$ 後，真正的原始明文直接出爐：",
                    "$$P_2[15] = I_2[15] \\oplus C_1[15]$$",
                    "4. 接著將 $C'_1[15]$ 固定為 $I_2[15] \\oplus 0x02$，開始搜尋 $C'_1[14]$ 滿足結尾為 `0x02 0x02`。",
                    "5. **複雜度**：一個區塊 16 位元組，每個位元組最多僅需 256 次查詢，整個區塊最多 $16 \\times 256 = 4096$ 次查詢即可在未知金鑰下完全還原！"
                ]
            }
        ]
    },

    # Module 6
    {
        "id": "mod-all-6",
        "number": "模組 06",
        "title": "訊息驗證碼（MAC）與完整性防護",
        "subtitle": "Message Authentication Codes & Integrity",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Subsection 2.1)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 10: Message Authentication Codes)"
        ],
        "summary": "深入資料完整性（Integrity）之核心原語 MAC 與 EUF-CMA 安全遊戲模型，探討 CBC-MAC 在可變長度訊息下的長度延伸偽造攻擊與修復方案，以及 HMAC 雙重雜湊設計原理。",
        "sections": [
            {
                "title": "訊息驗證碼（MAC）與 EUF-CMA 安全模型",
                "content": [
                    "**目標**：確保訊息的真實性（Authenticity）與完整性（Integrity），防止攻擊者未經授權竄改或偽造內容（MAC 不提供機密性）。",
                    "**演算法組**：$(\\mathrm{Gen}, \\mathrm{Mac}, \\mathrm{Vrfy})$。標籤 $t \\leftarrow \\mathrm{Mac}_k(m)$，驗證 $\\mathrm{Vrfy}_k(m, t) \\in \\{1, 0\\}$。",
                    "**EUF-CMA 安全模型（選擇訊息攻擊下的存在不可偽造性）**：",
                    "- 攻擊者可向 MAC 預言機查詢任意訊息的合法標籤。",
                    "- 獲勝條件：產出一組全新訊息 $m^*$（未曾查詢過）與其合法標籤 $t^*$，使得驗證通過。",
                    "- 若對所有 PPT 攻擊者獲勝機率皆為 $\\mathrm{negl}(n)$，則稱該 MAC 為 EUF-CMA 安全。"
                ]
            },
            {
                "title": "CBC-MAC 之長度延伸攻擊與修復",
                "content": [
                    "**基礎 CBC-MAC 構造**：以 IV=0 進行 CBC 模式加密，最後一個區塊輸出即為標籤 $t$。",
                    "**長度延伸攻擊（Extension / Splicing Attack）**：",
                    "- 若直接用於可變長度訊息，攻擊者查詢單區塊 $m_1$ 得標籤 $t_1$；查詢單區塊 $m_2$ 得標籤 $t_2$。",
                    "- 攻擊者構造兩區塊新訊息 $m^* = m_1 \\parallel (m_2 \\oplus t_1)$。",
                    "- 在計算 $m^*$ 的第二區塊時：輸入為 $(m_2 \\oplus t_1) \\oplus t_1 = m_2$。輸出恰好等於 $t_2$！攻擊者成功偽造全新訊息之合法標籤！",
                    "**修復方案**：CMAC 或 ECBC-MAC（在最後一個區塊使用由獨立金鑰衍生的遮罩金鑰異或），阻斷長度延伸延伸鏈接。"
                ]
            },
            {
                "title": "HMAC 雙重雜湊架構",
                "content": [
                    "構造：$\\mathrm{HMAC}_K(m) = H\\big((K \\oplus \\mathrm{opad}) \\parallel H((K \\oplus \\mathrm{ipad}) \\parallel m)\\big)$。",
                    "**設計考量**：若直接採用單次雜湊 $H(K \\parallel m)$，Merkle-Damgård 結構的雜湊函數會遭受長度延伸攻擊（Length Extension Attack）；HMAC 透過內外兩層不同常數（ipad `0x36`, opad `0x5C`）的雙重雜湊結構，徹底阻斷了此類攻擊。"
                ]
            }
        ]
    },

    # Module 7
    {
        "id": "mod-all-7",
        "number": "模組 07",
        "title": "驗證式加密（AE）與現代標準",
        "subtitle": "Authenticated Encryption (AE) & Generic Compositions",
        "sources": [
            "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf (劉子源教授講義, Subsection 2.2)",
            "Cyrptography.pdf (The Joy of Cryptography, Ch. 12: Authenticated Encryption & AEAD)"
        ],
        "summary": "探討同時提供機密性與完整性的驗證式加密（AE）。剖析現代密碼學黃金定理（IND-CPA + INT-CTXT => IND-CCA）、評比三大組合範式（Encrypt-and-MAC, MAC-then-Encrypt, Encrypt-then-MAC），以及現代高吞吐 AEAD 標準 AES-GCM 模式。",
        "sections": [
            {
                "title": "驗證式加密核心定理：IND-CPA + INT-CTXT => IND-CCA",
                "content": [
                    "**安全性層級**：",
                    "- 密文完整性（INT-CTXT）：攻擊者在未掌握金鑰下，無法鍛造出任何能成功解密的新密文。",
                    "**黃金定理**：",
                    "$$\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$$",
                    "**直觀證明**：只要密文具備 INT-CTXT，攻擊者向解密預言機發送的任何竄改密文 $c \\ne c^*$ 都會在解密前直接被驗證器拒絕並拋棄，解密預言機對攻擊者完全無效，系統自動升格為最強的 IND-CCA 安全！"
                ]
            },
            {
                "title": "三大組合範式評比（Generic Compositions）",
                "content": [
                    "1. **Encrypt-and-MAC**（早期 SSH）：$c = \\mathrm{Enc}_{k_1}(m), \\; t = \\mathrm{Mac}_{k_2}(m)$。**不安全**！MAC 標籤直接由明文計算，可能外洩明文資訊，無法保證 IND-CPA。",
                    "2. **MAC-then-Encrypt**（早期 SSL/TLS）：$t = \\mathrm{Mac}_{k_2}(m), \\; c = \\mathrm{Enc}_{k_1}(m \\parallel t)$。**脆弱**！密文遭篡改時會先進入解密器，容易引發 Padding Oracle 側信道攻擊（如 Lucky Thirteen 漏洞）。",
                    "3. **Encrypt-then-MAC（EtM）**（IPsec、現代標準）：$c = \\mathrm{Enc}_{k_1}(m), \\; t = \\mathrm{Mac}_{k_2}(c)$。**唯一通用且可證明安全**！接收端先校驗密文標籤 $t$，若不符直接丟棄，完全不執行解密！"
                ]
            },
            {
                "title": "現代 AEAD 標準：AES-GCM 模式",
                "content": [
                    "**AEAD（Authenticated Encryption with Associated Data）**：除了加密明文外，還能對無需保密的關聯資料（如網路封包 IP 標頭）同時進行完整性認證。",
                    "**AES-GCM（Galois/Counter Mode）**：採用 CTR 模式進行加密，結合有限域 $\\mathrm{GF}(2^{128})$ 上的 GHASH 乘法進行平行化認證，吞吐量極高，為 TLS 1.3、IPsec 與現代 HTTPS 的默認標準。"
                ]
            }
        ]
    }
]

# 32 Comprehensive Quizzes (4 per module across all 8 modules)
all_quizzes = [
    # Mod 0: Historical & Math (Katz Ch 1 + Joy Ch 0)
    {
        "id": "q-all-0-1",
        "moduleId": "mod-all-0",
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
        "moduleId": "mod-all-0",
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
        "moduleId": "mod-all-0",
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
        "moduleId": "mod-all-0",
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

    # Mod 1: Perfect Secrecy (Katz Ch 2 + Joy Ch 1)
    {
        "id": "q-all-1-1",
        "moduleId": "mod-all-1",
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
        "moduleId": "mod-all-1",
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
        "moduleId": "mod-all-1",
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
        "moduleId": "mod-all-1",
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

    # Mod 2: Provable Security Mindset (Slides 1.2 + Joy Ch 2/4)
    {
        "id": "q-all-2-1",
        "moduleId": "mod-all-2",
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
        "moduleId": "mod-all-2",
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
        "moduleId": "mod-all-2",
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
        "moduleId": "mod-all-2",
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

    # Mod 3: Pseudorandomness (Slides 1.4 + Joy Ch 5/6)
    {
        "id": "q-all-3-1",
        "moduleId": "mod-all-3",
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
        "moduleId": "mod-all-3",
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
        "moduleId": "mod-all-3",
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
        "moduleId": "mod-all-3",
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

    # Mod 4: CPA (Slides 1.5 Section 1 + Joy Ch 7)
    {
        "id": "q-all-4-1",
        "moduleId": "mod-all-4",
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
        "moduleId": "mod-all-4",
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
        "moduleId": "mod-all-4",
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
        "moduleId": "mod-all-4",
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
    },

    # Mod 5: CCA & Padding Oracle (Slides 1.5 Section 2 + Joy Ch 9)
    {
        "id": "q-all-5-1",
        "moduleId": "mod-all-5",
        "category": "概念辨析",
        "question": "IND-CCA1 與 IND-CCA2 最核心的威脅模型差異為何？",
        "options": [
            "IND-CCA1 攻擊者不能取得密文，而 IND-CCA2 可以",
            "IND-CCA1（非適應性）僅允許攻擊者在收到挑戰密文 $c^*$『之前』查詢解密預言機；而 IND-CCA2（適應性）在收到 $c^*$『之後』仍可查詢除 $c^*$ 以外的任意密文",
            "IND-CCA1 是針對對稱密碼，而 IND-CCA2 專門針對公鑰密碼",
            "IND-CCA1 採用量子電腦攻擊，IND-CCA2 採用經典電腦攻擊"
        ],
        "answer": 1,
        "explanation": "IND-CCA1（午餐時間攻擊）在挑戰密文產生後立即關閉解密預言機；IND-CCA2 是完全適應性攻擊，攻擊者收到挑戰密文 $c^*$ 後，除了不得直接查詢 $c^*$ 本身外，仍可繼續查詢任何竄改後的密文 $c \\ne c^*$，安全性要求最高。",
        "pitfalls": "混淆前後查詢權限，IND-CCA2 是在挑戰密文產生後仍能持續進行有條件查詢。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 15-18 & Joy Ch. 9"
    },
    {
        "id": "q-all-5-2",
        "moduleId": "mod-all-5",
        "category": "攻擊推導",
        "question": "在 CBC 模式的 Padding Oracle 攻擊中，攻擊者修改前一密文區塊 $C_1$ 得到 $C'_1$ 並送交解密。當伺服器回傳「Padding Valid」且目標填充為單一位元組 `0x01` 時，中間值 $I_2[15]$ 與構造值 $C'_1[15]$ 滿足何種數學關係？",
        "options": [
            "$I_2[15] = C'_1[15] \\oplus 0x01$",
            "$I_2[15] = C'_1[15] + 0x01$",
            "$I_2[15] = C_1[15] \\oplus C'_1[15]$",
            "$I_2[15] = 0x01$"
        ],
        "answer": 0,
        "explanation": "CBC 解密時最後一位元組明文為 $P'_2[15] = I_2[15] \\oplus C'_1[15]$。若伺服器判定填充合法為 `0x01`，則代表 $P'_2[15] = 0x01$。由 $I_2[15] \\oplus C'_1[15] = 0x01$，兩邊同時 $\\oplus 0x01$ 即得 $I_2[15] = C'_1[15] \\oplus 0x01$。",
        "pitfalls": "誤將 XOR 寫為加法，或忘記中間值是由偽造的 $C'_1$ 與填充目標計算得出。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 25-32 & Joy Ch. 9"
    },
    {
        "id": "q-all-5-3",
        "moduleId": "mod-all-5",
        "category": "演算複雜度",
        "question": "使用 Padding Oracle 攻擊還原一個 16 位元組（128-bit）的 CBC 密文區塊時，攻擊者在最差情況下最多需向伺服器發送幾次解密預言機查詢？",
        "options": [
            "$2^{128}$ 次",
            "$16 \\times 256 = 4096$ 次",
            "$16^{16}$ 次",
            "$256^{16}$ 次"
        ],
        "answer": 1,
        "explanation": "該攻擊以位元組為單位獨立逐一破解。一個位元組只有 256 種可能數值（0x00 到 0xFF），因此每個位元組最多需 256 次查詢。整個 16 位元組區塊最差情況下僅需 $16 \\times 256 = 4096$ 次查詢，將指數級的密鑰窮舉降至多項式次數！",
        "pitfalls": "誤認為區塊長度會導致查詢次數呈現指數爆炸（如 $256^{16}$）。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 33 & Joy Ch. 9"
    },
    {
        "id": "q-all-5-4",
        "moduleId": "mod-all-5",
        "category": "防護原則",
        "question": "防範 Padding Oracle 攻擊的根本解決方案為何？",
        "options": [
            "優化 Padding 檢查程式碼使其執行更快",
            "將錯誤訊息全部改為相同的 HTTP 500",
            "採用驗證式加密（Authenticated Encryption，如 Encrypt-then-MAC 或 AES-GCM），在解密前先驗證密文完整性",
            "將金鑰長度擴展為 512 位元"
        ],
        "answer": 2,
        "explanation": "單純修改錯誤訊息往往無效，解密時間差異（Timing Side-channel）依然會造成洩漏。根本解決之道是在解密前先驗證 MAC 標籤，不合法直接丟棄，完全不執行解密！",
        "pitfalls": "誤以為修改回傳字串就能修補漏洞，忽略了時間側信道。",
        "reference": "1.5 Chosen-Ciphertext Attacks.pdf & Joy Ch. 9.2"
    },

    # Mod 6: MAC (Slides 1.5 Subsection 2.1 + Joy Ch 10)
    {
        "id": "q-all-6-1",
        "moduleId": "mod-all-6",
        "category": "概念辨析",
        "question": "在訊息驗證碼（MAC）的 EUF-CMA 安全模型中，攻擊者獲勝的標準是什麼？",
        "options": [
            "計算出發送方的私密金鑰 $k$",
            "成功解密出一篇未曾公開的機密訊息",
            "產出一組未曾在預言機查詢過的全新訊息 $m^*$，並給出合法的標籤 $t^*$ 使其驗證通過",
            "使驗證伺服器的 CPU 使用率達到 100%"
        ],
        "answer": 2,
        "explanation": "EUF-CMA 代表「選擇訊息攻擊下的存在不可偽造性」。攻擊者只要能針對任何一條未曾查詢過的訊息 $m^*$ 鍛造出合法標籤 $t^*$，即使該訊息毫無語意價值，也算完全攻破該 MAC 系統。",
        "pitfalls": "誤以為攻擊者必須還原出金鑰 $k$ 才算獲勝。密碼學安全要求更嚴格：哪怕只偽造一則無意義訊息的標籤就算破解。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 48 & Joy Ch. 10.1"
    },
    {
        "id": "q-all-6-2",
        "moduleId": "mod-all-6",
        "category": "攻擊推導",
        "question": "基礎的 CBC-MAC 若直接應用於「可變長度訊息（Variable-length messages）」，會面臨何種致命攻擊？",
        "options": [
            "金鑰會在傳輸第 3 個區塊時自動洩漏",
            "長度延伸攻擊（Extension / Splicing Attack）：給定單區塊合法對 $(m_1, t_1)$，攻擊者可偽造雙區塊訊息 $m_1 \\parallel (m_2 \\oplus t_1)$ 其標籤恰好等於單區塊 $m_2$ 之標籤 $t_2$",
            "CBC 模式在解密時無法平行化",
            "會導致雜湊函數發生碰撞"
        ],
        "answer": 1,
        "explanation": "CBC-MAC 僅對固定長度訊息保證安全。若長度可變，第二區塊在加密前會與前一區塊密文（標籤 $t_1$）進行 XOR：$(m_2 \\oplus t_1) \\oplus t_1 = m_2$。輸入內容與直接對 $m_2$ 計算完全相同，標籤自然等於 $t_2$，攻擊者可輕易偽造兩區塊訊息！",
        "pitfalls": "誤認為 CBC-MAC 可直接用於任意長度檔案，必須使用 CMAC 或在最後一區塊異或特殊金鑰。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 55-58 & Joy Ch. 10.3"
    },
    {
        "id": "q-all-6-3",
        "moduleId": "mod-all-6",
        "category": "架構原理",
        "question": "HMAC 採用雙重雜湊架構 $H\\big((K \\oplus \\mathrm{opad}) \\parallel H((K \\oplus \\mathrm{ipad}) \\parallel m)\\big)$，其主要設計目的為何？",
        "options": [
            "為了讓運算速度提升兩倍",
            "徹底阻斷 Merkle-Damgård 結構雜湊函數在單次雜湊 $H(K \\parallel m)$ 時面臨的長度延伸攻擊（Length Extension Attack）",
            "為了縮短 MAC 標籤的長度",
            "使 MAC 具備非對稱公鑰加密功能"
        ],
        "answer": 1,
        "explanation": "若直接使用 $H(K \\parallel m)$，攻擊者知道訊息長度後可在末尾追加內容並由舊雜湊值繼續計算新雜湊。HMAC 透過內外兩層金鑰遮罩雙重雜湊，徹底阻斷了長度延伸路徑。",
        "pitfalls": "誤以為直接使用單次雜湊加金鑰就足夠安全。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf & Joy Ch. 11.3"
    },
    {
        "id": "q-all-6-4",
        "moduleId": "mod-all-6",
        "category": "概念辨析",
        "question": "訊息驗證碼（MAC）能提供下列哪一種安全防護？",
        "options": [
            "機密性（Confidentiality，防止竊聽）",
            "真實性與完整性（Authenticity & Integrity，防止未授權竄改）",
            "不可否認性（Non-repudiation，防止發送方事後抵賴）",
            "完美保密性（Perfect Secrecy）"
        ],
        "answer": 1,
        "explanation": "對稱 MAC 僅提供真實性與完整性。因雙方共用金鑰，接收方也能產出相同標籤，故 MAC 無法提供抗抵賴（不可否認性需靠非對稱數位簽章）；且 MAC 不提供機密性防護。",
        "pitfalls": "混淆 MAC 與數位簽章（不可否認性），以及混淆完整性與機密性。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf & Joy Ch. 10.1"
    },

    # Mod 7: AE (Slides 1.5 Subsection 2.2 + Joy Ch 12)
    {
        "id": "q-all-7-1",
        "moduleId": "mod-all-7",
        "category": "理論關係",
        "question": "現代密碼學中關於驗證式加密（AE）與選擇密文安全性（IND-CCA）的黃金關係式為何？",
        "options": [
            "$\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$",
            "$\\mathrm{IND\\text{-}CPA} + \\mathrm{One\\text{-}Time\\text{ }Pad} \\implies \\mathrm{IND\\text{-}CCA}$",
            "$\\mathrm{INT\\text{-}PTXT} \\implies \\mathrm{INT\\text{-}CTXT}$",
            "$\\mathrm{IND\\text{-}CCA} \\implies \\mathrm{Perfect\\text{ }Secrecy}$"
        ],
        "answer": 0,
        "explanation": "定理指出：若一個加密系統同時具備選擇明文不可區分性（IND-CPA）以及密文完整性（INT-CTXT，攻擊者無法鍛造出有效的新密文），則該系統必然具備最強的選擇密文不可區分性（IND-CCA）。這是現代安全通訊協議（如 TLS 1.3）架構設計的核心理論依據。",
        "pitfalls": "混淆明文完整性（INT-PTXT）與密文完整性（INT-CTXT），INT-PTXT 無法推導出 IND-CCA。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 68 & Joy Ch. 12"
    },
    {
        "id": "q-all-7-2",
        "moduleId": "mod-all-7",
        "category": "架構比較",
        "question": "在結合加密與訊息驗證碼（MAC）構建驗證式加密（AE）的三大組合範式中，哪一種被證明具備通用安全性（Provably Secure under Generic Composition）？",
        "options": [
            "Encrypt-and-MAC（同時對明文加密與計算 MAC）",
            "MAC-then-Encrypt（先對明文計算 MAC，再將明文與 MAC 一同加密）",
            "Encrypt-then-MAC（先對明文加密得到密文，再對密文計算 MAC 標籤）",
            "MAC-only（僅傳送 MAC 標籤，不傳送密文）"
        ],
        "answer": 2,
        "explanation": "Encrypt-then-MAC（EtM）是唯一通用的安全組合範式。接收方收到封包後第一時間驗證密文的 MAC 標籤，若驗證失敗立即拋棄，惡意密文完全沒有機會被解密器處理，徹底杜絕了 Padding Oracle 等側信道攻擊。",
        "pitfalls": "誤以為 TLS 早期使用的 MAC-then-Encrypt 是安全的，MAC-then-Encrypt 正是導致 Lucky Thirteen 等重大漏洞的主因。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 65-72 & Joy Ch. 12.2"
    },
    {
        "id": "q-all-7-3",
        "moduleId": "mod-all-7",
        "category": "實務標準",
        "question": "現代主流 AEAD 演算法 AES-GCM（Galois/Counter Mode）具備何種技術優勢？",
        "options": [
            "採用非對稱 RSA 質數分解進行認證",
            "結合 CTR 模式的高速串流加密與 Galois 有限域 $\\mathrm{GF}(2^{128})$ 上的平行化 GHASH 認證，吞吐量極高",
            "不需要任何初始化向量 IV",
            "金鑰長度必須大於 4096 位元"
        ],
        "answer": 1,
        "explanation": "AES-GCM 是現代工業標準（TLS 1.3、IPsec）。CTR 模式可高度硬體平行化加密，GHASH 在硬體指令集（如 AES-NI、PCLMULQDQ）支援下運算極速，同時保障機密性與完整性。",
        "pitfalls": "誤以為 GCM 是 CBC 模式的變種，GCM 採用的是 CTR 計數器模式。",
        "reference": "1.5 Chosen-Ciphertext Attacks.pdf & Joy Ch. 12.4"
    },
    {
        "id": "q-all-7-4",
        "moduleId": "mod-all-7",
        "category": "工程禁忌",
        "question": "在實作 Encrypt-then-MAC 組合範式時，下列哪一項是密碼學絕對禁止的致命錯誤？",
        "options": [
            "加密演算法與 MAC 演算法共用同一把對稱金鑰 $k$",
            "使用獨立衍生出的兩把金鑰 $k_1, k_2$",
            "先校驗 MAC 標籤，校驗成功才執行解密",
            "對密文與額外認證資料（Associated Data）一同計算 MAC"
        ],
        "answer": 0,
        "explanation": "金鑰隔離（Key Separation）是密碼學基本安全原則。若加密與 MAC 共用同一個金鑰 $k$，兩者底層運算特性可能相互干擾，導致安全性證明崩潰，甚至遭構造特定關聯攻擊破譯。",
        "pitfalls": "誤以為省去一把金鑰更有效率，共用金鑰破壞了所有可證明安全性假設。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf & Joy Ch. 12"
    }
]

# Comprehensive Glossary of 20+ terms across all 6 PDFs
all_glossary = [
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
    },
    {
        "term": "IND-CCA (CCA1 / CCA2)",
        "chinese": "選擇密文攻擊不可區分性",
        "category": "安全模型 (Slides 1.5 / Joy Ch 9)",
        "definition": "攻擊者擁有解密預言機。CCA1 僅限挑戰前查詢；CCA2 允許在取得挑戰密文後，繼續查詢除挑戰密文本體以外的任意密文。",
        "pitfall": "純 CBC 模式與串流密碼均只達到 IND-CPA，無法抵抗 IND-CCA 攻擊。"
    },
    {
        "term": "Padding Oracle Attack",
        "chinese": "填充預言機攻擊",
        "category": "密碼分析 (Slides 1.5 / Joy Ch 9)",
        "definition": "利用伺服器解密後回傳的 PKCS#7 填充錯誤訊息，藉由修改前一密文區塊並觀察反應，在無金鑰情況下逐位元組還原明文。",
        "pitfall": "修補錯誤回傳字串往往不夠，時間差（Timing Side-channel）依然會造成洩漏，根本解法為採用 AEAD。"
    },
    {
        "term": "MAC (Message Authentication Code)",
        "chinese": "訊息驗證碼",
        "category": "完整性原語 (Slides 1.5 / Joy Ch 10)",
        "definition": "對稱金鑰機制，用於驗證訊息之完整性與真實性。標準安全模型為 EUF-CMA（存在不可偽造性）。",
        "pitfall": "MAC 僅保護完整性，不提供任何機密性防護。"
    },
    {
        "term": "HMAC",
        "chinese": "基於雜湊之訊息驗證碼",
        "category": "完整性原語 (Slides 1.5 / Joy Ch 11)",
        "definition": "利用雙重雜湊架構 $H((K \\oplus \\mathrm{opad}) \\parallel H((K \\oplus \\mathrm{ipad}) \\parallel m))$ 構造 MAC，徹底免疫長度延伸攻擊。",
        "pitfall": "不可直接以單次雜湊 $H(K \\parallel m)$ 作為 MAC，會遭受長度延伸攻擊直接偽造標籤。"
    },
    {
        "term": "AE (Authenticated Encryption)",
        "chinese": "驗證式加密",
        "category": "綜合機制 (Slides 1.5 / Joy Ch 12)",
        "definition": "同時保障機密性與完整性的密碼機制。滿足 $\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$。現代推薦採用 AES-GCM 或 ChaCha20-Poly1305。",
        "pitfall": "組合加密與 MAC 時，僅 Encrypt-then-MAC 具備通用證明安全，切勿採用 Encrypt-and-MAC。"
    }
]

js_content = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source strictly integrating ALL 6 PDFs:
// 1. Introduction to Modern Cryptography - Historical Ciphers
// 2. Introduction to Modern Cryptography - Perfectly Secret Encryption
// 3. 1.2 The Provable Security Mindset
// 4. 1.4 Pseudorandomness
// 5. 1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks
// 6. Cyrptography.pdf (The Joy of Cryptography by Mike Rosulek: Ch 0, 1, 2, 4, 5, 6, 7)

const MODULES_DATA = {json.dumps(all_modules, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(all_quizzes, ensure_ascii=False, indent=2)};

const GLOSSARY_DATA = {json.dumps(all_glossary, ensure_ascii=False, indent=2)};
"""

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated js/data.js integrating ALL 6 PDFs!")
print(f"Total Modules: {len(all_modules)}")
print(f"Total Quizzes: {len(all_quizzes)}")
print(f"Total Glossary: {len(all_glossary)}")
