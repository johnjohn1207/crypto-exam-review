# -*- coding: utf-8 -*-
"""
Generate complete data for Joy of Cryptography (Mike Rosulek)
Target Chapters: 0, 1, 2, 4, 5, 6, 7
"""

import json

joy_modules = [
    {
        "id": "mod-joy-0",
        "number": "Ch 0",
        "title": "概念與符號回顧",
        "subtitle": "Review of Concepts & Notation",
        "source": "The Joy of Cryptography, Ch. 0 (p. 1 - 9)",
        "summary": "回顧密碼學不可或缺之離散數學基礎：對數與指數、模除同餘運算、二進位字串與 XOR 四大代數特性、函數映射（單射/映成/雙射）、機率論與條件機率，以及虛擬碼與大 O 漸近複雜度符號。",
        "sections": [
            {
                "title": "0.1 對數與指數運算（Logs & Exponents）",
                "content": [
                    "**核心恆等式**：$(x^a)(x^b) = x^{a+b}$、$(x^a)^b = x^{ab}$、$\\log_x(ab) = \\log_x a + \\log_x b$、以及 $a \\log_x b = \\log_x(b^a)$。",
                    "**重大禁忌**：嚴格禁止寫出 $(x^a)(x^b) = x^{ab}$。指數相乘代表底數相同時冪次相加，混淆兩者將導致離散對數等密碼難題推導全面崩潰。"
                ]
            },
            {
                "title": "0.2 模運算與同餘系統（Modular Arithmetic & Congruence）",
                "content": [
                    "**整數與自然數集合**：整數集合 $\\mathbb{Z} = \\{\\dots, -2, -1, 0, 1, 2, \\dots\\}$；自然數集合 $\\mathbb{N} = \\{0, 1, 2, \\dots\\}$（0 視為自然數）。",
                    "**整除定義（Divides $n \\mid x$）**：若存在整數 $k$ 使得 $x = kn$，則稱 $n$ 整除 $x$（或 $x$ 為 $n$ 的倍數）。注意 1 整除所有整數，而 0 只能整除 0 本身。",
                    "**模除運算子（% Operator）**：設 $n > 0$，$a \\% n$ 定義為將 $a$ 除以 $n$ 所得的唯一餘數 $r \\in \\{0, 1, \\dots, n - 1\\}$，使得 $n \\mid (a - r)$。**關鍵特性：無論 $a$ 為正或負，$a \\% n$ 恆為非負數**。例如：$20 \\% 7 = 6$、$-20 \\% 7 = 1$（因為 $-20 = (-3) \\times 7 + 1$）、$-1 \\% 7 = 6$。",
                    "**同餘關係（Congruence Modulo $n$, $\\equiv_n$）**：若 $n \\mid (a - b)$，或等價地 $a \\% n = b \\% n$，則記為 $a \\equiv_n b$（亦即 $a \\equiv b \\pmod n$）。",
                    "**關鍵辨析：$a \\equiv_n b$ 與 $a = b \\% n$ 之本質差異**：",
                    "- $a \\equiv_n b$：兩側 $a, b$ 可為任意大小與正負的整數，描述的是整數之間的模同餘關係。",
                    "- $a = b \\% n$：此為整數相等關係。右側 $b \\% n$ 是運算子輸出，結果值必然落在 $\\{0, \\dots, n-1\\}$ 區間。例如 $99 \\equiv_{10} 19$ 為真，但 $99 = 19 \\% 10$ 為假（因為 $19 \\% 10 = 9 \\ne 99$）。",
                    "**歐幾里得演算法（Euclid's Algorithm）與最大公因數（GCD）**：若 $\\gcd(x, y) = 1$，則稱 $x$ 與 $y$ 互質（Relatively Prime）。遞迴計算式為 $\\gcd(x, y) = \\gcd(y, x \\% y)$。",
                    "**計算化簡技巧（Tips & Tricks）**：在計算複雜乘積模除時，隨時化簡中間數值。例如計算 $6 \\times 7 \\times 8 \\times 9 \\times 10 \\% 11$，先計算 $6 \\times 7 = 42 \\equiv_{11} 9$，接著 $9 \\times 8 = 72 \\equiv_{11} 6$，持續化簡最後得出 1，無需算出巨大數值。"
                ]
            },
            {
                "title": "0.3 字串與互斥或四大性質（Strings & Bitwise XOR）",
                "content": [
                    "二進位字串集合以 $\\{0, 1\\}^n$ 表示，字串串接以 $x \\parallel y$ 表示。",
                    "**互斥或（XOR, $\\oplus$）四大代數基石**：",
                    "1. **交換律（Commutative）**：$x \\oplus y = y \\oplus x$。",
                    "2. **結合律（Associative）**：$(x \\oplus y) \\oplus z = x \\oplus (y \\oplus z)$。",
                    "3. **單位元（Identity）**：$x \\oplus 0 = x$。",
                    "4. **自相反身性（Self-inverse）**：$x \\oplus x = 0$。此性質推導出若 $x \\oplus y = z$，則必有 $x \\oplus z = y$ 以及 $y \\oplus z = x$。這是對稱密碼加解密能夠使用完全相同電路的核心數學依據！"
                ]
            },
            {
                "title": "0.4 函數映射分類（Functions）",
                "content": [
                    "設函數 $f: X \\to Y$：",
                    "- **單射（Injective / One-to-one）**：若 $x \\ne x'$ 則 $f(x) \\ne f(x')$。充要條件為 $|X| \\le |Y|$。",
                    "- **映成（Surjective / Onto）**：對任意 $y \\in Y$，皆存在 $x \\in X$ 使得 $f(x) = y$。充要條件為 $|X| \\ge |Y|$。",
                    "- **雙射（Bijective / One-to-one Correspondence）**：同時為單射與映成。必然要求 $|X| = |Y|$，且必然存在唯一的反函數 $f^{-1}: Y \\to X$。在有限集合上的雙射即為**置換（Permutation）**，是分組密碼（PRP/AES）的數學本質。"
                ]
            },
            {
                "title": "0.5 機率論基礎（Probability Fundamentals）",
                "content": [
                    "**均勻隨機抽取**：以 $x \\leftarrow S$ 表示從有限集合 $S$ 中均勻隨機選取元素，每個元素被選中的機率恰為 $1/|S|$。",
                    "**條件機率**：$P[A \\mid B] = \\frac{P[A \\cap B]}{P[B]}$（前提 $P[B] > 0$）。",
                    "**全機率定理（Law of Total Probability）**：若事件 $B_1, \\dots, B_k$ 構成樣本空間的分割，則 $P[A] = \\sum_{i=1}^k P[A \\mid B_i] P[B_i]$。",
                    "**事件獨立性**：事件 $A$ 與 $B$ 獨立若且唯若 $P[A \\cap B] = P[A] \\times P[B]$，等價於 $P[A \\mid B] = P[A]$。",
                    "**聯集上界（Union Bound / Boole's Inequality）**：對於任意事件集合 $E_1, \\dots, E_k$（無論彼此是否獨立），恆滿足：",
                    "$$P\\left[\\bigcup_{i=1}^k E_i\\right] \\le \\sum_{i=1}^k P[E_i]$$",
                    "此不等式是密碼學證明中計算攻擊者在多項式查詢下各類失敗機率上限的最關鍵工具。"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-1",
        "number": "Ch 1",
        "title": "單次密鑰與柯克霍夫原則",
        "subtitle": "One-Time Pad & Kerckhoffs' Principle",
        "source": "The Joy of Cryptography, Ch. 1 (p. 10 - 20)",
        "summary": "探討密碼學的守備範疇與柯克霍夫原則（Kerckhoffs' Principle），剖析經典單次密鑰（One-Time Pad）的規格、完美保密性推導、Shannon 不可能定理、Two-Time Pad 致命金鑰重用攻擊以及位元翻轉延展性攻擊。",
        "sections": [
            {
                "title": "1.1 什麼是密碼學？柯克霍夫原則（What Is [Not] Cryptography?）",
                "content": [
                    "**密碼學防範什麼？** 密碼學關注於在惡意中間人（Adversary / Eve）監聽與操縱通訊通道的情境下，保障資訊的機密性與完整性。",
                    "**密碼學不防範什麼？** 密碼學無法防範端點物理遭竊、作業系統漏洞、惡意軟體側信道鍵擊記錄或使用者被社交工程詐欺。",
                    "**柯克霍夫原則（Kerckhoffs' Principle）**：加密演算法本身必須假設完全對外公開，整個系統的安全性必須且只能建立在金鑰（Key）的保密性之上。",
                    "- 演算法公開能讓全世界的密碼專家進行嚴格檢驗。",
                    "- 金鑰外洩時，只需要撤銷並重新抽樣生成一把新金鑰，無需重新發明與部屬全新演算法。"
                ]
            },
            {
                "title": "1.2 單次密鑰規格與完美保密推導（Specifics of One-Time Pad）",
                "content": [
                    "**One-Time Pad（OTP）規格**：明文空間 $\\mathcal{M} = \\{0, 1\\}^\\ell$，金鑰空間 $\\mathcal{K} = \\{0, 1\\}^\\ell$，密文空間 $\\mathcal{C} = \\{0, 1\\}^\\ell$。",
                    "- 金鑰生成：$k \\leftarrow \\{0, 1\\}^\\ell$ 均勻隨機抽取。",
                    "- 加密演算法：$\\mathrm{Enc}(k, m) = m \\oplus k$。",
                    "- 解密演算法：$\\mathrm{Dec}(k, c) = c \\oplus k$。",
                    "**完美保密性推導（Shannon's Perfect Secrecy）**：",
                    "給定任意固定明文 $m$ 與任意觀察到的密文 $c$，使其成立的金鑰 $k$ 恰好只有一個：$k = m \\oplus c$。因為金鑰是均勻隨機抽取的，所以：",
                    "$$P[C = c \\mid M = m] = P[K = m \\oplus c] = \\frac{1}{2^\\ell}$$",
                    "該機率對任意明文 $m$ 都是恆定的常數 $2^{-\\ell}$，與明文內容毫無關聯。因此密文完全不外洩明文的任何資訊，後驗機率嚴格等於先驗機率！"
                ]
            },
            {
                "title": "Shannon 不可能定理與實務限制（Shannon's Theorem）",
                "content": [
                    "**Shannon 不可能定理**：任何達到完美保密性的加密系統，其金鑰空間必須至少與明文空間一樣大：$|\\mathcal{K}| \\ge |\\mathcal{M}|$。若為二進位字串，金鑰長度必須大於或等於明文長度（$\\ell_K \\ge \\ell_M$）。",
                    "**代價與限制**：若要加密 1 TB 的資料，雙方必須事先安全傳遞 1 TB 的隨機金鑰；金鑰不可重複使用，使得 OTP 在大規模實務傳輸中極度不實用。"
                ]
            },
            {
                "title": "致命弱點：Two-Time Pad 攻擊與延展性（Insecurity of Key Reuse）",
                "content": [
                    "**1. Two-Time Pad 攻擊（重用金鑰的災難）**：",
                    "若使用相同金鑰 $k$ 加密 $m_1$ 與 $m_2$ 產生 $c_1 = m_1 \\oplus k$ 與 $c_2 = m_2 \\oplus k$：",
                    "$$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$$",
                    "金鑰完全抵消！利用 ASCII 碼特性：英文字母高 3 位為 `010` 或 `011`，而空白鍵為 `0x20`（`00100000`）。任何字母與空白鍵 XOR，只會翻轉大小寫；非空白鍵互斥或會產生小於 `0x40` 的值。攻擊者利用 Crib Dragging 技術可迅速全數還原明文！",
                    "**2. 延展性（Malleability / Bit-flipping Attack）**：",
                    "中間人將密文 $c$ 修改為 $c' = c \\oplus \\Delta$，解密後的明文為 $m' = c' \\oplus k = (c \\oplus k) \\oplus \\Delta = m \\oplus \\Delta$。攻擊者能在未知金鑰與明文下精準竄改資料內容。**OTP 僅具備機密性，完全不具備完整性！**"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-2",
        "number": "Ch 2",
        "title": "可證明安全性基礎與混合證明法",
        "subtitle": "The Basics of Provable Security & The Hybrid Technique",
        "source": "The Joy of Cryptography, Ch. 2 (p. 21 - 46)",
        "summary": "奠定現代密碼學的安全證明範式：如何撰寫安全定義（Security Definitions）、安全遊戲（Security Games）、Left-vs-Right 與 Real-vs-Random 兩大風格、攻擊者優勢度（Advantage）計算，以及核心證明武器：混合證明技術（The Hybrid Technique）。",
        "sections": [
            {
                "title": "2.1 & 2.2 如何撰寫形式化安全定義（Game-Based Definitions）",
                "content": [
                    "**直覺定義的破綻**：『攻擊者無法算出金鑰』不是好的定義（因為直接洩漏明文的加密法金鑰也可能沒被算出）；『攻擊者無法還原明文』也不是好的定義（因為攻擊者可能算出明文的前 80% 或奇偶性）。",
                    "**遊戲範式（Game-Based Template）**：安全定義由一組包含預言機（Oracles）的挑戰者程式與攻擊者 $\\mathcal{A}$ 進行互動遊戲。",
                    "**兩大主流風格**：",
                    "1. **Left-vs-Right 風格（$\\mathcal{L}_{\\mathrm{ots\\text{-}L}}$ vs $\\mathcal{L}_{\\mathrm{ots\\text{-}R}}$）**：",
                    "- 攻擊者提交兩個等長明文對 $(m_0, m_1)$。",
                    "- 遊戲 0（Left）加密回傳 $m_0$；遊戲 1（Right）加密回傳 $m_1$。",
                    "2. **Real-vs-Random 風格（$\\mathcal{L}_{\\mathrm{ots\\text{-}real}}$ vs $\\mathcal{L}_{\\mathrm{ots\\text{-}rand}}$）**：",
                    "- 攻擊者提交明文 $m$。",
                    "- 遊戲 0 回傳真實密文 $\\mathrm{Enc}(k, m)$；遊戲 1 回傳與密文長度相同的純隨機字串 $r \\leftarrow \\{0, 1\\}^\\ell$。",
                    "**優勢度（Advantage）數學定義**：",
                    "$$\\mathbf{Adv}(\\mathcal{A}) = \\big| P[\\mathcal{A} \\text{ outputs 1 in Game 0}] - P[\\mathcal{A} \\text{ outputs 1 in Game 1}] \\big|$$"
                ]
            },
            {
                "title": "2.3 如何透過攻擊證明不安全性（Demonstrating Insecurity）",
                "content": [
                    "若要證明某加密機制在某安全定義下是不安全的，必須具體建構一個具備顯著優勢度（Non-negligible Advantage）的攻擊者演算法 $\\mathcal{A}$。",
                    "**標準攻擊三步驟**：",
                    "1. 明確寫出 $\\mathcal{A}$ 的演算法流程（包含詢問預言機的輸入與判斷邏輯）。",
                    "2. 分別推導並計算 $P[\\mathcal{A} \\text{ outputs 1 in Game 0}]$ 與 $P[\\mathcal{A} \\text{ outputs 1 in Game 1}]$ 的精準數值。",
                    "3. 計算兩者之差的絕對值，展示 $\\mathbf{Adv}(\\mathcal{A})$ 為顯著常數（如 1 或 0.5），而非接近 0 的可忽略值。"
                ]
            },
            {
                "title": "2.4 核心證明武器：混合證明技術（The Hybrid Technique）",
                "content": [
                    "**原理與重要性**：當 Game 0 與 Game 1 差異過大無法直接分析時，在兩者之間插入一連串中間遊戲序列（Hybrids）：$G_0, G_1, G_2, \\dots, G_k$。",
                    "- 其中 $G_0$ 為原始的真實遊戲，$G_k$ 為目標隨機遊戲。",
                    "- 每相鄰兩個中間遊戲 $G_i$ 與 $G_{i+1}$ 之間，**只有微小的單一步驟差異**（例如僅將第 $i$ 個金鑰或第 $i$ 個運算替換為隨機數）。",
                    "**三角不等式上界推導（Triangle Inequality）**：",
                    "$$\\big| P[\\mathcal{A} \\text{ outputs 1 in } G_0] - P[\\mathcal{A} \\text{ outputs 1 in } G_k] \\big| \\le \\sum_{i=0}^{k-1} \\big| P[\\mathcal{A} \\text{ outputs 1 in } G_i] - P[\\mathcal{A} \\text{ outputs 1 in } G_{i+1}] \\big|$$",
                    "若相鄰遊戲之間的不可區分性皆受限於底層原語的優勢度 $\\epsilon$，則總優勢度不超過 $k \\cdot \\epsilon$。只要 $k$ 為多項式大小，系統便具備可證明安全性！"
                ]
            },
            {
                "title": "2.5 安全定義的比較與等價性（Comparing Security Definitions）",
                "content": [
                    "**強弱關係判定**：若符合定義 X 的方案必然符合定義 Y，則稱定義 X 比定義 Y 更強（或等價）。",
                    "在單次密鑰環境下，Left-vs-Right 與 Real-vs-Random 兩種風格在數學上是完全等價的；但在多次加密環境中，細微的語意差異將決定是否能抵抗選擇密文攻擊。"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-4",
        "number": "Ch 4",
        "title": "基於難題之計算密碼學與生日界",
        "subtitle": "Basing Cryptography on Intractable Computations",
        "source": "The Joy of Cryptography, Ch. 4 (p. 67 - 84)",
        "summary": "剖析現代計算密碼學的實用基石：計算上不可行（Computationally Infeasible）攻擊、可忽略函數（Negligible Function）之嚴格界定、計算不可區分性，以及在密碼分析中無所不在的生日問題機率（Birthday Bound）。",
        "sections": [
            {
                "title": "4.1 & 4.2 計算不可行與可忽略函數（Computationally Infeasible & Negligible）",
                "content": [
                    "**計算資源限制（PPT）**：真實世界攻擊者不可能進行 $2^{128}$ 次操作（地球原子總數約 $10^{80} \\approx 2^{265}$，全宇宙運算能力有限）。攻擊者運算時間受限於安全參數 $n$ 的機率多項式時間（Probabilistic Polynomial Time, PPT）。",
                    "**可忽略函數 $\\mathrm{negl}(n)$ 之嚴格定義**：",
                    "函數 $\\mu(n)$ 是可忽略的，若對任意多項式次方 $c > 0$，皆存在門檻 $n_0$ 使得當 $n > n_0$ 時均有：",
                    "$$\\mu(n) < \\frac{1}{n^c}$$",
                    "**直觀含義**：攻擊者即使重複嘗試多項式次數，成功的機率依然微乎其微。例如 $2^{-n}$、$2^{-\\sqrt{n}}$ 為可忽略函數；而 $n^{-10}$、$1/\\log n$ 則不是可忽略函數。"
                ]
            },
            {
                "title": "4.3 計算不可區分性（Computational Indistinguishability）",
                "content": [
                    "兩個機率分佈族 $X_n$ 與 $Y_n$ 稱為計算不可區分（記為 $X_n \\approx Y_n$），若對於任意 PPT 區分器 $\\mathcal{D}$，其區分優勢度為可忽略函數：",
                    "$$\\mathbf{Adv}(\\mathcal{D}) = \\big| P[\\mathcal{D}(X_n) = 1] - P[\\mathcal{D}(Y_n) = 1] \\big| \\le \\mathrm{negl}(n)$$",
                    "這意味著在多項式時間內，任何演算法都無法將偽造的隨機分佈與真正的均勻分佈區分開來。"
                ]
            },
            {
                "title": "4.4 生日問題機率與抽樣邊界（Birthday Probabilities & Birthday Bound）",
                "content": [
                    "**經典生日問題**：一個房間需要多少人，才能讓其中兩人同一天生日的機率超過 50%？答案僅需 23 人（遠小於 365 天）。",
                    "**密碼學生日定理（Birthday Bound）**：",
                    "從大小為 $N$ 的集合中進行 $q$ 次**有放回**的均勻隨機抽樣，發生至少一次碰撞（重複抽取相同數值）的機率近似為：",
                    "$$P[\\text{Collision}] \\approx 1 - e^{-\\frac{q(q-1)}{2N}} \\approx \\frac{q^2}{2N}$$",
                    "**碰撞臨界值**：當抽樣次數 $q \\approx \\sqrt{N}$ 時，碰撞機率即達到約 50%！",
                    "**密碼學重大實務影響**：",
                    "- 若分組密碼區塊大小為 64 位元（$N = 2^{64}$，如 DES、3DES），只需加密 $q \\approx 2^{32} \\approx 40$ 億個區塊（約 32 GB 資料），IV 或密文區塊即有極高機率發生碰撞，瓦解 CBC 模式安全性（此即 Sweet32 攻擊）！",
                    "- 因此現代密碼學（如 AES）全面採用 128 位元區塊（$N = 2^{128}$），其生日碰撞門檻高達 $2^{64}$ 區塊，保證絕對安全。"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-5",
        "number": "Ch 5",
        "title": "偽隨機生成器（PRG）與對稱棘輪",
        "subtitle": "Pseudorandom Generators & Applications",
        "source": "The Joy of Cryptography, Ch. 5 (p. 85 - 105)",
        "summary": "探討突破 Shannon 定理的第一步：偽隨機生成器（PRG）。涵蓋 PRG 安全定義、Pseudo-OTP 加密架構與歸約證明、PRG 伸展長度擴充定理，以及在現代即時通訊中實現前向保密的對稱棘輪（Symmetric Ratchet）機制。",
        "sections": [
            {
                "title": "5.1 偽隨機生成器定義（PRG Definition）",
                "content": [
                    "**語意**：確定性有效率演算法 $G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + \\ell}$，將長度為 $\\lambda$ 的短隨機種子（Seed $s$）伸展為長度為 $\\lambda + \\ell$（$\\ell > 0$）的長字串。",
                    "**安全定義（PRG Security Game）**：",
                    "- 遊戲 0（Real）：Challenger 隨機挑選種子 $s \\leftarrow \\{0, 1\\}^\\lambda$，回傳 $G(s)$。",
                    "- 遊戲 1（Random）：Challenger 直接挑選真隨機長字串 $r \\leftarrow \\{0, 1\\}^{\\lambda + \\ell}$ 回傳。",
                    "- 對任意 PPT 區分器 $\\mathcal{D}$，優勢度必須可忽略：",
                    "$$\\mathbf{Adv}_{\\mathrm{prg}}(\\mathcal{D}) = \\big| P[\\mathcal{D}(G(s)) = 1] - P[\\mathcal{D}(r) = 1] \\big| \\le \\mathrm{negl}(\\lambda)$$"
                ]
            },
            {
                "title": "5.3 應用：縮短金鑰的 Pseudo-OTP 加密與歸約證明",
                "content": [
                    "**方案設計**：利用長度擴展為 $\\ell$ 的 PRG $G$，金鑰空間只需 $\\mathcal{K} = \\{0, 1\\}^\\lambda$（短種子），加密長度為 $\\ell$ 的訊息：",
                    "$$c = \\mathrm{Enc}(k, m) = m \\oplus G(k)$$",
                    "解密：$m = c \\oplus G(k)$。這徹底突破了 Shannon 定理的金鑰長度限制！",
                    "**安全性歸約證明（Reduction Proof using Hybrid）**：",
                    "- **Hybrid 0**：真實遊戲，密文為 $m_b \\oplus G(k)$。",
                    "- **Hybrid 1**：將 $G(k)$ 替換為真正的均勻隨機字串 $r \\leftarrow \\{0, 1\\}^\\ell$，密文為 $m_b \\oplus r$。",
                    "- 由於 Hybrid 1 實質上就是真 One-Time Pad，攻擊者在此遊戲中的優勢度**嚴格為 0**！",
                    "- 根據 PRG 安全性，Hybrid 0 與 Hybrid 1 的不可區分性受限於 $\\mathbf{Adv}_{\\mathrm{prg}}$，故 Pseudo-OTP 達成計算可證明安全性！"
                ]
            },
            {
                "title": "5.4 擴展 PRG 的伸展長度（Extending the Stretch）",
                "content": [
                    "**Blum-Micali 建構定理**：只要存在輸出僅比輸入多 1 位元的 PRG（$G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + 1}$），即可遞迴擴展為任意多項式長度的 PRG！",
                    "**串接展開法**：每次將種子輸入 $G$ 產生 $(\\text{新種子 } s', \\text{輸出位元 } b)$，將 $s'$ 作為下一次輸入，依序產出無限串流。"
                ]
            },
            {
                "title": "5.5 對稱棘輪機制與前向保密（Symmetric Ratchet & Forward Secrecy）",
                "content": [
                    "**現代通訊應用（如 Signal 協議）**：利用 PRG 構建狀態單向演進的棘輪（Ratchet）。",
                    "- 狀態更新：$(k_{\\mathrm{next}}, k_{\\mathrm{enc}}) \\leftarrow G(k_{\\mathrm{current}})$。",
                    "- 傳送訊息使用 $k_{\\mathrm{enc}}$，隨後立即從記憶體徹底抹除 $k_{\\mathrm{current}}$。",
                    "**前向保密性（Forward Secrecy）**：即使攻擊者在時間點 $T$ 成功入侵並竊取了裝置當前的狀態金鑰，由於 PRG 的單向不可逆性，攻擊者**完全無法計算出過去的歷史金鑰**，過往的歷史通訊紀錄依舊固若金湯！"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-6",
        "number": "Ch 6",
        "title": "偽隨機函數（PRF）與分組密碼",
        "subtitle": "Pseudorandom Functions & Block Ciphers",
        "source": "The Joy of Cryptography, Ch. 6 (p. 106 - 129)",
        "summary": "探討帶金鑰之偽隨機函數（PRF）與作為雙射置換的分組密碼（PRP/Block Cipher）。涵蓋 PRF vs PRG 轉換、Variable-Hybrid 證明、PRP/PRF 切換引理（Switching Lemma）以及強偽隨機置換（Strong PRP）。",
        "sections": [
            {
                "title": "6.1 偽隨機函數定義（PRF Definition）",
                "content": [
                    "**語意**：金鑰化演算法 $F: \\{0, 1\\}^\\lambda \\times \\{0, 1\\}^\\mathrm{in} \\to \\{0, 1\\}^\\mathrm{out}$。以金鑰 $k$ 索引函數 $F(k, \\cdot)$。",
                    "**黑盒子預言機安全遊戲**：",
                    "- 遊戲 0（Real PRF）：預言機背後使用真正的金鑰 $k \\leftarrow \\{0, 1\\}^\\lambda$ 計算 $F(k, x)$ 回傳。",
                    "- 遊戲 1（Truly Random Function, RF）：預言機背後維護動態查表，對每個全新輸入 $x$ 均勻隨機抽取一個輸出 $y \\leftarrow \\{0, 1\\}^\\mathrm{out}$ 並記錄之（相同輸入回傳相同隨機值）。",
                    "- 對任意能進行多項式次數查詢的 PPT 區分器 $\\mathcal{D}$，優勢度滿足 $\\mathbf{Adv}_{\\mathrm{prf}}(\\mathcal{D}) \\le \\mathrm{negl}(\\lambda)$。"
                ]
            },
            {
                "title": "6.2 PRF 與 PRG 的轉換關係",
                "content": [
                    "**CTR 模式：PRF $\\to$ PRG**：",
                    "給定 PRF $F$，令 $G(k) = F(k, 0) \\parallel F(k, 1) \\parallel F(k, 2) \\dots$，可將短金鑰 $k$ 擴展為任意長度的偽隨機場。",
                    "**GGM 建構法：PRG $\\to$ PRF**：",
                    "利用輸出長度加倍的 PRG $G(s) = (G_0(s), G_1(s))$ 建構深度為 $n$ 的二元樹，輸入字串的位元決定尋訪方向，葉節點輸出即為 $F_k(x)$。證明採用了 **Variable-Hybrid 技術**。"
                ]
            },
            {
                "title": "6.3 & 6.4 分組密碼（PRP）與 PRP/PRF 切換引理（Switching Lemma）",
                "content": [
                    "**分組密碼（Block Cipher / PRP）**：輸入與輸出長度相同（$n$ 位元），且對每個金鑰 $k$，$P(k, \\cdot)$ 都是一個**雙射置換（Permutation）**，存在高效率的反向解密演算法 $P^{-1}(k, \\cdot)$。現代標準如 AES（128 位元區塊）。",
                    "**PRP/PRF 切換引理（PRP/PRF Switching Lemma）**：",
                    "分組密碼在數學上是置換（不允許碰撞），而真隨機函數 RF 允許碰撞。兩者在進行 $q$ 次查詢時的行為差異嚴格受限於生日碰撞機率：",
                    "$$\\big| \\mathbf{Adv}_{\\mathrm{prp}}(\\mathcal{D}) - \\mathbf{Adv}_{\\mathrm{prf}}(\\mathcal{D}) \\big| \\le \\frac{q(q-1)}{2 \\cdot 2^n} \\le \\frac{q^2}{2^{n+1}}$$",
                    "這意味著只要查詢次數 $q \\ll 2^{n/2}$，分組密碼就可以直接當作理想的 PRF 使用！"
                ]
            },
            {
                "title": "6.5 & 6.6 強偽隨機置換（Strong PRP）與 Feistel 輪數",
                "content": [
                    "**強偽隨機置換（Strong PRP / SPRP）**：攻擊者不僅能向正向預言機查詢 $P(k, x)$，還能向反向預言機查詢 $P^{-1}(k, y)$。只有當雙向查詢皆無法與隨機置換區分時，才達到 Strong PRP。",
                    "**Feistel 網路之 Luby-Rackoff 定理**：",
                    "- 3 輪 Feistel 網路可將 PRF 轉為 PRP（抗正向查詢）。",
                    "- **必須達到 4 輪 Feistel 網路**，才能抵抗正向與反向雙向預言機攻擊，達到 Strong PRP！"
                ]
            }
        ]
    },
    {
        "id": "mod-joy-7",
        "number": "Ch 7",
        "title": "選擇明文攻擊（CPA）安全性",
        "subtitle": "Security Against Chosen Plaintext Attacks",
        "source": "The Joy of Cryptography, Ch. 7 (p. 130 - 143)",
        "summary": "探討多次加密情境下的選擇明文攻擊（CPA）。揭露確定性加密的結構性死穴、偽隨機密文（Pseudorandom Ciphertexts）概念，以及如何利用 PRF 建構現代 CPA 安全加密方案。",
        "sections": [
            {
                "title": "7.1 確定性加密的極限（Limits of Deterministic Encryption）",
                "content": [
                    "**定義**：若加密演算法 $\\mathrm{Enc}(k, m)$ 沒有使用隨機數也沒有維護內部狀態，則稱為確定性加密（Deterministic Encryption）。例如 ECB 模式。",
                    "**CPA 遊戲下的 100% 破譯證明**：",
                    "- 攻擊者在 CPA 遊戲中擁有加密預言機 $\\mathcal{O}_{\\mathrm{Enc}}(\\cdot)$。",
                    "- 攻擊者預先向預言機查詢 $m_0$，記錄密文 $c_0 = \\mathrm{Enc}(k, m_0)$。",
                    "- 挑戰階段送出明文對 $(m_0, m_1)$，接收挑戰密文 $c^*$。",
                    "- 由於演算法為確定性，若 $c^* = c_0$ 則 100% 確信 $b=0$；否則 $b=1$。",
                    "- 攻擊者優勢度 $\\mathbf{Adv} = 1 - 0 = 1$。**任何確定性加密演算法在理論上絕對無法達到 IND-CPA 安全！**"
                ]
            },
            {
                "title": "7.2 偽隨機密文（Pseudorandom Ciphertexts）",
                "content": [
                    "更強的安全屬性：密文不僅在不同明文之間不可區分，而且對於任何不知道金鑰的觀察者而言，密文的外觀與純隨機二進位字串不可區分。",
                    "達成此目標能防止流量分析，並徹底隱藏訊息的格式、協議特徵與元數據。"
                ]
            },
            {
                "title": "7.3 基於 PRF 之 CPA 安全加密方案（CPA-Secure Scheme from PRF）",
                "content": [
                    "**方案構造**：設 $F$ 為安全 PRF，金鑰為 $k \\leftarrow \\{0, 1\\}^\\lambda$：",
                    "- 加密明文 $m \\in \\{0, 1\\}^\\mathrm{out}$：均勻隨機選取初始化向量 $r \\leftarrow \\{0, 1\\}^\\mathrm{in}$，輸出密文對：",
                    "$$c = \\langle r, \\; F(k, r) \\oplus m \\rangle$$",
                    "- 解密密文 $\\langle r, c_1 \\rangle$：計算 $m = c_1 \\oplus F(k, r)$。",
                    "**安全性推導（The Hybrid Technique 應用）**：",
                    "1. **Game 0**：真實 CPA 遊戲，密文使用 $F(k, r) \\oplus m_b$。",
                    "2. **Game 1**：將 PRF $F(k, \\cdot)$ 替換為真正的隨機函數 $\\mathrm{RF}(\\cdot)$。兩遊戲之不可區分性受限於 PRF 的優勢度 $\\mathbf{Adv}_{\\mathrm{prf}}$。",
                    "3. **Game 2**：在隨機函數下，只要隨機選取的 $r$ 沒有發生碰撞（重複），$F(k, r)$ 就是全新的真隨機一次性金鑰。由生日界可知，$q$ 次查詢發生 $r$ 碰撞的機率小於 $q^2 / (2 \\cdot 2^\\mathrm{in})$。",
                    "4. 在無碰撞情況下，密文相當於 One-Time Pad，攻擊者優勢度為 0！故該方案在 $q \\ll 2^{\\mathrm{in}/2}$ 下具備可證明 CPA 安全性！"
                ]
            },
            {
                "title": "狀態化（Stateful）vs 隨機化（Randomized）",
                "content": [
                    "避免確定性加密漏洞的兩種途徑：",
                    "1. **隨機化（Randomized）**：如上述方案，每次加密生成隨機 IV $r$。優點為無需儲存狀態，缺點為密文長度增加且存在生日碰撞機率。",
                    "2. **狀態化（Stateful / Counter）**：通訊雙方維護計數器 Nonce（$r = 0, 1, 2, \\dots$）。優點為保證 $r$ 永不重複（徹底消除生日碰撞），缺點為若計數器在斷電或同步失敗時重置，將導致嚴重災難。"
                ]
            }
        ]
    }
]

joy_quizzes = [
    # Ch 0
    {
        "id": "q-joy-0-1",
        "moduleId": "mod-joy-0",
        "category": "數學運算",
        "question": "根據《The Joy of Cryptography》Chapter 0 的定義，計算負數模除 $-20 \\% 7$ 的正確結果為何？",
        "options": [
            "-6",
            "1",
            "-1",
            "6"
        ],
        "answer": 1,
        "explanation": "在數學與密碼學中，餘數 $r = a \\% n$ 必須是非負數且落在 $\\{0, \\dots, n-1\\}$ 區間。因為 $-20 = (-3) \\times 7 + 1$，餘數為 1。$-20$ 比 7 的倍數（$-21$）剛好大 1。",
        "pitfalls": "某些程式語言（如 C/C++）定義負數餘數為 $-6$，這在密碼學運算中是嚴格錯誤的，密碼學餘數必須為非負數。",
        "reference": "The Joy of Cryptography, Ch. 0, Definition 0.2, p. 2"
    },
    {
        "id": "q-joy-0-2",
        "moduleId": "mod-joy-0",
        "category": "代數性質",
        "question": "位元互斥或運算（XOR, $\\oplus$）的四大基本代數性質中，使得對稱加密與解密能夠使用同一套運算邏輯的關鍵性質為何？",
        "options": [
            "分配律（Distributive Property）",
            "自相反身性（Self-inverse Property）：$x \\oplus x = 0$ 且 $(x \\oplus y) \\oplus y = x$",
            "結合律使得字串長度可以無限擴展",
            "零元素性質：$x \\oplus 1 = 1$"
        ],
        "answer": 1,
        "explanation": "自相反身性保證了任何數值與自身 XOR 都會得到 0，且 $(m \\oplus k) \\oplus k = m \\oplus (k \\oplus k) = m \\oplus 0 = m$。因此解密只需將密文再次與金鑰 XOR 即可完整還原明文。",
        "pitfalls": "混淆自反性與分配律，XOR 是對稱密碼抵消金鑰的基礎代數原理。",
        "reference": "The Joy of Cryptography, Ch. 0.3, p. 4"
    },
    {
        "id": "q-joy-0-3",
        "moduleId": "mod-joy-0",
        "category": "概念辨析",
        "question": "同餘式「$a \\equiv_n b$」與等式「$a = b \\% n$」在數學意義上的最關鍵差別為何？",
        "options": [
            "兩者完全相同，只是不同數學家的書寫習慣差異",
            "在 $a \\equiv_n b$ 中，$a$ 與 $b$ 可為任意大小與符號的整數；而 $a = b \\% n$ 則強制要求 $a \\in \\{0, \\dots, n-1\\}$",
            "$a \\equiv_n b$ 只能用於質數，而 $a = b \\% n$ 可用於合數",
            "$a = b \\% n$ 只能在量子電腦上運算"
        ],
        "answer": 1,
        "explanation": "$a \\equiv_n b$ 描述的是整數模 $n$ 的同餘關係，例如 $99 \\equiv_{10} 19$ 是正確的；但 $99 = 19 \\% 10$ 是錯誤的，因為右側 $19 \\% 10$ 輸出整數 9，而 99 不等於 9。",
        "pitfalls": "誤將同餘符號等同於等號，忽略了 % 運算子的輸出範圍限制。",
        "reference": "The Joy of Cryptography, Ch. 0.2, Definition 0.4, p. 2"
    },
    {
        "id": "q-joy-0-4",
        "moduleId": "mod-joy-0",
        "category": "機率推導",
        "question": "在密碼學證明中，聯集上界（Union Bound）指出：對於任意 $k$ 個事件 $E_1, \\dots, E_k$，$P[\\bigcup_{i=1}^k E_i]$ 與 $\\sum_{i=1}^k P[E_i]$ 的關係為何？",
        "options": [
            "$P[\\bigcup_{i=1}^k E_i] = \\prod_{i=1}^k P[E_i]$",
            "$P[\\bigcup_{i=1}^k E_i] \\le \\sum_{i=1}^k P[E_i]$（無論事件之間是否獨立皆成立）",
            "只有在事件相互獨立時，$P[\\bigcup_{i=1}^k E_i] \\le \\sum_{i=1}^k P[E_i]$ 才成立",
            "$P[\\bigcup_{i=1}^k E_i] \\ge \\sum_{i=1}^k P[E_i]$"
        ],
        "answer": 1,
        "explanation": "聯集上界（Boole's Inequality）是機率論極強大的工具，對於任意事件集合，聯集的機率永遠小於或等於各事件機率之和，完全不需要事件獨立的假設。",
        "pitfalls": "誤以為聯集上界需要獨立性假設。獨立性只在相乘時需要，相加上界永遠成立。",
        "reference": "The Joy of Cryptography, Ch. 0.5, p. 6"
    },

    # Ch 1
    {
        "id": "q-joy-1-1",
        "moduleId": "mod-joy-1",
        "category": "概念辨析",
        "question": "根據《The Joy of Cryptography》第 1 章，柯克霍夫原則（Kerckhoffs' Principle）主張密碼系統的安全性應建立在何種基礎上？",
        "options": [
            "演算法本身必須保密，防止攻擊者得知運算架構",
            "演算法應完全公開透明，安全性必須完全依賴於金鑰的保密",
            "金鑰長度必須隨通訊次數呈指數增長",
            "通訊協定必須透過專有硬體閉源封裝"
        ],
        "answer": 1,
        "explanation": "柯克霍夫原則指出演算法必須假設公開。隱蔽式安全（Security through Obscurity）極易破功且一旦外洩無法修復，唯有金鑰保密才能在金鑰外洩時透過重新發行金鑰恢復安全。",
        "pitfalls": "將專利或閉源演算法視為安全保障，實務證明閉源演算法往往隱藏致命漏洞。",
        "reference": "The Joy of Cryptography, Ch. 1.1, p. 11"
    },
    {
        "id": "q-joy-1-2",
        "moduleId": "mod-joy-1",
        "category": "數學證明",
        "question": "在 One-Time Pad（OTP）中，對於長度為 $\\ell$ 的任意固定明文 $m$ 與密文 $c$，$P[C=c \\mid M=m]$ 的精準機率為何？",
        "options": [
            "0",
            "$2^{-\\ell}$",
            "$1/\\ell$",
            "取決於明文中 0 與 1 的分佈比例"
        ],
        "answer": 1,
        "explanation": "因 $C = M \\oplus K$，給定 $M=m$ 時，產生密文 $c$ 的唯一充要條件為 $K = m \\oplus c$。金鑰從長度 $\\ell$ 的字串中均勻隨機抽取，機率恆為 $1/2^\\ell = 2^{-\\ell}$，與明文完全獨立。",
        "pitfalls": "誤以為機率會受到明文文字意義或 Hamming 重量影響。",
        "reference": "The Joy of Cryptography, Ch. 1.2, p. 13"
    },
    {
        "id": "q-joy-1-3",
        "moduleId": "mod-joy-1",
        "category": "攻擊推導",
        "question": "當發送方使用相同 OTP 金鑰加密兩篇明文得到 $c_1$ 與 $c_2$，攻擊者計算 $c_1 \\oplus c_2$ 會發生什麼事？",
        "options": [
            "得到純隨機亂碼，無法進行分析",
            "得到 $m_1 \\oplus m_2$，金鑰被完全抵消，可透過 ASCII 空白鍵（0x20）特徵與 Crib Dragging 破譯兩篇明文",
            "金鑰以平方形式顯現",
            "密文會自動銷毀"
        ],
        "answer": 1,
        "explanation": "$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$。金鑰完全消失，攻擊者掌握明文互斥或，透過語言統計特徵能迅速還原內容。",
        "pitfalls": "誤以為金鑰依然能保護資料。",
        "reference": "The Joy of Cryptography, Ch. 1.2, p. 16"
    },
    {
        "id": "q-joy-1-4",
        "moduleId": "mod-joy-1",
        "category": "理論極限",
        "question": "Shannon 不可能定理揭示了完美保密加密（Perfect Secrecy）的何種實務代價？",
        "options": [
            "加密演算法需要耗費超多項式時間運算",
            "金鑰空間大小必須大於或等於明文空間大小（$|\\mathcal{K}| \\ge |\\mathcal{M}|$），金鑰長度不得短於明文長度",
            "系統只能在量子電腦上實現",
            "解密結果必然存在多義性"
        ],
        "answer": 1,
        "explanation": "Shannon 證明若 $|\\mathcal{K}| < |\\mathcal{M}|$，必然存在某個明文在觀察到特定密文後後驗機率為 0，破壞完美保密。這意味著加密 1 GB 資料必須消耗 1 GB 金鑰。",
        "pitfalls": "誤記為 $|\\mathcal{K}| \\le |\\mathcal{M}|$。",
        "reference": "The Joy of Cryptography, Ch. 1.2, p. 18"
    },

    # Ch 2
    {
        "id": "q-joy-2-1",
        "moduleId": "mod-joy-2",
        "category": "概念辨析",
        "question": "在可證明安全性遊戲中，Left-vs-Right（$\\mathcal{L}_{\\mathrm{ots\\text{-}L}}$ vs $\\mathcal{L}_{\\mathrm{ots\\text{-}R}}$）風格的核心定義為何？",
        "options": [
            "挑戰者回傳金鑰的左半部或右半部給攻擊者",
            "攻擊者提交等長明文對 $(m_0, m_1)$，挑戰者在 Game 0 加密 $m_0$，在 Game 1 加密 $m_1$",
            "攻擊者必須在左手邊的伺服器與右手邊的伺服器之間進行分散式運算",
            "演算法使用向左移位或向右移位"
        ],
        "answer": 1,
        "explanation": "Left-vs-Right 風格要求攻擊者提交兩個明文 $m_0$（Left）與 $m_1$（Right），挑戰者隨機決定加密回傳哪一個，測試攻擊者是否有能力區分密文來自左側還是右側。",
        "pitfalls": "誤以為與金鑰切片或移位運算有關。",
        "reference": "The Joy of Cryptography, Ch. 2.2, p. 26"
    },
    {
        "id": "q-joy-2-2",
        "moduleId": "mod-joy-2",
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
        "id": "q-joy-2-3",
        "moduleId": "mod-joy-2",
        "category": "攻擊設計",
        "question": "若要嚴謹證明某個加密方案是不安全的（Insecure），證明者必須提出什麼？",
        "options": [
            "提出數學證明該演算法在 NP-hard 類別之外",
            "建構一個具體的多項式時間攻擊者演算法 $\\mathcal{A}$，並計算其在兩遊戲中的行為差異，證明其優勢度 $\\mathbf{Adv}(\\mathcal{A})$ 為顯著非可忽略數值",
            "找到該演算法的原始碼中的語法錯誤",
            "證明金鑰長度小於 256 位元"
        ],
        "answer": 1,
        "explanation": "密碼學證明不安全性的標準做法是提供攻擊實例：寫出攻擊演算法 $\\mathcal{A}$，並給出概率計算展示 $\\mathbf{Adv}(\\mathcal{A})$ 顯著大於可忽略函數（例如等於 1 或 0.5）。",
        "pitfalls": "誤以為只要口頭指出漏洞即可，必須有嚴格的優勢度概率計算。",
        "reference": "The Joy of Cryptography, Ch. 2.3, p. 30"
    },
    {
        "id": "q-joy-2-4",
        "moduleId": "mod-joy-2",
        "category": "概念辨析",
        "question": "Real-vs-Random 風格的安全定義中，挑戰者在 Random 遊戲中回傳給攻擊者的是什麼？",
        "options": [
            "均勻隨機選取的金鑰",
            "與真實密文長度相同的真正隨機字串（$r \\leftarrow \\{0, 1\\}^\\ell$）",
            "將明文字元隨機洗牌後的結果",
            "隨機的錯誤訊息"
        ],
        "answer": 1,
        "explanation": "Real-vs-Random 測試密文是否看起來就像純隨機字串。在 Real 遊戲中回傳真實加密結果，在 Random 遊戲中回傳獨立均勻隨機抽樣的二進位字串。",
        "pitfalls": "誤以為是回傳隨機金鑰或隨機明文。",
        "reference": "The Joy of Cryptography, Ch. 2.2, p. 25"
    },

    # Ch 4
    {
        "id": "q-joy-4-1",
        "moduleId": "mod-joy-4",
        "category": "生日問題",
        "question": "根據生日定理（Birthday Bound），從大小為 $N = 2^{64}$ 的集合中進行 $q$ 次隨機抽樣，欲使發生至少一次碰撞的機率達到約 50%，抽樣次數 $q$ 約為多少？",
        "options": [
            "$2^{63}$ 次",
            "$\\approx \\sqrt{N} = 2^{32}$ 次（約 40 億次）",
            "$2^{64}$ 次",
            "64 次"
        ],
        "answer": 1,
        "explanation": "生日碰撞臨界值發生在 $q \\approx \\sqrt{N}$。當 $N = 2^{64}$ 時，$\\sqrt{2^{64}} = 2^{32} \\approx 4.29 \\times 10^9$ 次。這也是為何 64 位元區塊密碼（如 3DES）在加密數十 GB 資料時即會面臨 Sweet32 碰撞攻擊的原因！",
        "pitfalls": "誤以為需要抽樣一半（$2^{63}$）才會碰撞，生日悖論展示了碰撞機率增長遠比直覺快速得多。",
        "reference": "The Joy of Cryptography, Ch. 4.4, p. 76 - 78"
    },
    {
        "id": "q-joy-4-2",
        "moduleId": "mod-joy-4",
        "category": "複雜度理論",
        "question": "下列哪一個數學函數 $\\mu(n)$ 嚴格符合現代密碼學「可忽略函數（Negligible Function）」的定義？",
        "options": [
            "$\\mu(n) = \\frac{1}{n^{100}}$",
            "$\\mu(n) = 2^{-\\sqrt{n}}$",
            "$\\mu(n) = \\frac{1}{\\log_2 n}$",
            "$\\mu(n) = \\frac{1}{2n}$"
        ],
        "answer": 1,
        "explanation": "可忽略函數要求對任意正整數 $c$，最終均有 $\\mu(n) < 1/n^c$。$2^{-\\sqrt{n}}$ 為次指數衰減，其衰減速度超越任何多項式倒數 $n^{-c}$；而 $n^{-100}$ 與 $1/\\log n$ 均為多項式或次多項式等級，非可忽略函數。",
        "pitfalls": "看到 $n^{100}$ 很大就誤以為可忽略，定義要求對所有 $c$ 均成立，當 $c=101$ 時 $n^{-100} > n^{-101}$ 破功。",
        "reference": "The Joy of Cryptography, Ch. 4.2, p. 70"
    },
    {
        "id": "q-joy-4-3",
        "moduleId": "mod-joy-4",
        "category": "概念辨析",
        "question": "在現代計算密碼學中，為何將攻擊者的能力限制為「機率多項式時間（PPT）」？",
        "options": [
            "因為多項式時間演算法在現實物理世界中才是可行算力（Feasible Computation）的嚴謹抽象模型，排除不可行算力（如窮舉 $2^{128}$ 次）",
            "因為量子電腦只能運行多項式時間演算法",
            "因為密碼學演算法本身的執行時間是指數級的",
            "因為多項式函數的導數恆為常數"
        ],
        "answer": 0,
        "explanation": "PPT 模型排除一切荒謬的無限算力攻擊（如遍歷全宇宙原子），將安全性定義在面對具備合理計算資源的攻擊者時依然堅不可摧。",
        "pitfalls": "誤將 PPT 限制當成密碼學的弱點，實際上這才是讓實用密碼學得以存在的基石。",
        "reference": "The Joy of Cryptography, Ch. 4.1, p. 67"
    },
    {
        "id": "q-joy-4-4",
        "moduleId": "mod-joy-4",
        "category": "定義推導",
        "question": "兩個分佈族 $X_n \\approx Y_n$ 滿足計算不可區分性，其代表的意義為何？",
        "options": [
            "兩個分佈在統計上完全相同",
            "任何 PPT 演算法在多項式時間內，區分輸入來自 $X_n$ 或 $Y_n$ 的成功優勢皆小於可忽略函數",
            "兩個分佈的字串長度必然小於 128 位元",
            "演算法無法計算兩個分佈的平均值"
        ],
        "answer": 1,
        "explanation": "計算不可區分性是指沒有任何多項式時間區分器 $\\mathcal{D}$ 能以顯著優勢判定樣本來源，在實務計算層面上兩者等同。",
        "pitfalls": "混淆計算不可區分（PPT 限制）與統計不可區分（無限制算力）。",
        "reference": "The Joy of Cryptography, Ch. 4.3, p. 72"
    },

    # Ch 5
    {
        "id": "q-joy-5-1",
        "moduleId": "mod-joy-5",
        "category": "架構分析",
        "question": "使用偽隨機生成器（PRG）構建的 Pseudo-OTP 加密方案（$c = m \\oplus G(k)$），為何能突破 Shannon 不可能定理？",
        "options": [
            "因為它將安全性假設由資訊理論完美保密放寬為「計算安全性（面對 PPT 攻擊者不可區分）」",
            "因為 PRG 的輸出是真隨機的，產生了無限大的金鑰空間",
            "因為它使用了非對稱公鑰加密技術",
            "因為 XOR 運算被替換為模乘法運算"
        ],
        "answer": 0,
        "explanation": "Shannon 定理是在無限算力的資訊理論假設下成立。Pseudo-OTP 透過 PRG 放寬為計算安全性，PPT 攻擊者無法在多項式時間內將 $G(k)$ 與真隨機字串區分，從而以短金鑰實現計算上的安全加密。",
        "pitfalls": "誤以為 PRG 產出的是真隨機數，PRG 本質是完全確定性的演算法。",
        "reference": "The Joy of Cryptography, Ch. 5.3, p. 90"
    },
    {
        "id": "q-joy-5-2",
        "moduleId": "mod-joy-5",
        "category": "理論定理",
        "question": "根據 Blum-Micali 定理，如果我們擁有一個伸展長度僅為 1 位元的安全 PRG（$G: \\{0, 1\\}^\\lambda \\to \\{0, 1\\}^{\\lambda + 1}$），我們可以達成什麼？",
        "options": [
            "只能加密長度為 $\\lambda + 1$ 的明文",
            "可藉由級聯與串接迭代，建構出伸展長度為任意多項式長度 $p(\\lambda)$ 的安全 PRG",
            "可以直接構建出抗量子的公鑰加密系統",
            "無法保證多於 2 位元的安全性"
        ],
        "answer": 1,
        "explanation": "Blum-Micali 證明只要存在能擴充 1 位元的 PRG，透過輸出位元與反饋新種子的遞迴架構，就能擴充為任意多項式長度的 PRG，這是 PRG 理論的里程碑定理。",
        "pitfalls": "誤以為每次只能擴展少量位元，定理證明了任意長度的可擴展性。",
        "reference": "The Joy of Cryptography, Ch. 5.4, p. 92"
    },
    {
        "id": "q-joy-5-3",
        "moduleId": "mod-joy-5",
        "category": "實務應用",
        "question": "在即時通訊協議（如 Signal）的對稱棘輪（Symmetric Ratchet）機制中，如何達成「前向保密（Forward Secrecy）」？",
        "options": [
            "將所有通訊紀錄上傳至去中心化區塊鏈儲存",
            "利用 PRG 單向演進金鑰狀態：$(k_{\\mathrm{next}}, k_{\\mathrm{enc}}) \\leftarrow G(k_{\\mathrm{curr}})$，並立即銷毀 $k_{\\mathrm{curr}}$，使攻擊者即使入侵裝置也無法逆推歷史金鑰",
            "每分鐘向金鑰伺服器請求下載全新 RSA 私鑰",
            "將密文以明文廣播"
        ],
        "answer": 1,
        "explanation": "對稱棘輪利用 PRG 的單向不可逆性。每次傳訊後狀態推進並銷毀舊狀態，即使當前狀態金鑰遭竊，攻擊者在計算上無法逆推先前的金鑰，保障過往通訊不被解密。",
        "pitfalls": "誤以為前向保密必須隨時向中心伺服器連線更換金鑰。",
        "reference": "The Joy of Cryptography, Ch. 5.5, p. 98"
    },
    {
        "id": "q-joy-5-4",
        "moduleId": "mod-joy-5",
        "category": "概念辨析",
        "question": "PRG 的輸入稱為種子（Seed $s$），種子的挑選方式必須符合何種條件？",
        "options": [
            "可以由使用者隨意輸入常用的密碼字串",
            "必須由高熵源均勻隨機（Uniformly Random）抽取，長度達到安全參數 $\\lambda$",
            "必須是質數",
            "必須小於 10 個字元以利傳輸"
        ],
        "answer": 1,
        "explanation": "PRG 的所有不可區分性證明均建立在「種子 $s$ 是均勻隨機抽取」的嚴格前提下。若種子可被預測或熵值不足，PRG 的輸出將徹底喪失安全性。",
        "pitfalls": "誤以為 PRG 能將低熵的弱密碼直接變成安全金鑰，低熵密碼需要金鑰衍生函數（KDF）與加鹽延展。",
        "reference": "The Joy of Cryptography, Ch. 5.1, p. 85"
    },

    # Ch 6
    {
        "id": "q-joy-6-1",
        "moduleId": "mod-joy-6",
        "category": "引理推導",
        "question": "根據 PRP/PRF 切換引理（Switching Lemma），將分組密碼（PRP）視為偽隨機函數（PRF）使用時，產生的優勢度差距受限於何種邊界？",
        "options": [
            "$\\mathbf{Adv}$ 差距為 0，兩者完全相同",
            "$\\big| \\mathbf{Adv}_{\\mathrm{prp}} - \\mathbf{Adv}_{\\mathrm{prf}} \\big| \\le \\frac{q^2}{2^{n+1}}$（受生日碰撞機率上界限制）",
            "差距是指數級的 $2^n$",
            "差距只取決於金鑰長度與輪數"
        ],
        "answer": 1,
        "explanation": "分組密碼是置換（不允許碰撞），而真隨機函數允許碰撞。區分兩者的唯一機會就是觀察到輸出碰撞，根據生日定理，在 $q$ 次查詢下碰撞機率不超過 $q(q-1)/(2 \\cdot 2^n) \\le q^2 / 2^{n+1}$。",
        "pitfalls": "誤以為 PRP 與 PRF 沒有任何統計差異，置換無碰撞的特性是其唯一的區分依據。",
        "reference": "The Joy of Cryptography, Ch. 6.4, p. 121"
    },
    {
        "id": "q-joy-6-2",
        "moduleId": "mod-joy-6",
        "category": "原語建構",
        "question": "GGM 建構法（Goldreich-Goldwasser-Micali）展示了如何利用何種原語構建出何種原語？",
        "options": [
            "利用偽隨機生成器（PRG）建構出偽隨機函數（PRF）",
            "利用雜湊函數建構出對稱加密",
            "利用分組密碼建構出公鑰加密",
            "利用串流密碼建構出單次密鑰"
        ],
        "answer": 0,
        "explanation": "GGM 樹狀結構使用將長度擴展為兩倍的 PRG，依據輸入位元尋訪二元樹路徑，成功以 PRG 建構出 PRF，其安全性證明採用了 Variable-Hybrid 技術。",
        "pitfalls": "混淆 CTR 模式（PRF 轉 PRG）與 GGM（PRG 轉 PRF）。",
        "reference": "The Joy of Cryptography, Ch. 6.2, p. 110"
    },
    {
        "id": "q-joy-6-3",
        "moduleId": "mod-joy-6",
        "category": "結構理論",
        "question": "根據 Luby-Rackoff 定理，Feistel 網路需要至少幾輪（Rounds）才能達到強偽隨機置換（Strong PRP）？",
        "options": [
            "1 輪",
            "2 輪",
            "3 輪",
            "4 輪"
        ],
        "answer": 3,
        "explanation": "Luby-Rackoff 定理指出：3 輪 Feistel 僅能抵禦正向查詢（達到 PRP），若攻擊者具備反向解密查詢權限，3 輪會被攻破；必須達到 4 輪 Feistel 才能在雙向查詢下達成 Strong PRP。",
        "pitfalls": "誤記為 3 輪。3 輪只滿足 PRP，Strong PRP 需要 4 輪。",
        "reference": "The Joy of Cryptography, Ch. 6.6, p. 125"
    },
    {
        "id": "q-joy-6-4",
        "moduleId": "mod-joy-6",
        "category": "概念辨析",
        "question": "分組密碼（Block Cipher，如 AES）在數學抽象模型上對應下列哪一項？",
        "options": [
            "偽隨機生成器（PRG）",
            "偽隨機置換（PRP）",
            "非對稱陷門函數",
            "無碰撞雜湊函數"
        ],
        "answer": 1,
        "explanation": "分組密碼對固定長度區塊（如 128 位元）進行可逆的雙射替換與置換，因此在理論密碼學中被建模為偽隨機置換（PRP）。",
        "pitfalls": "混淆 PRF 與 PRP，分組密碼具備可逆解密性，因此是置換（Permutation）。",
        "reference": "The Joy of Cryptography, Ch. 6.3, p. 120"
    },

    # Ch 7
    {
        "id": "q-joy-7-1",
        "moduleId": "mod-joy-7",
        "category": "概念辨析",
        "question": "在選擇明文攻擊（CPA）模型下，為何確定性加密（Deterministic Encryption，如 ECB 模式）絕對無法達成 IND-CPA 安全？",
        "options": [
            "因為確定性加密的運算速度太慢",
            "因為攻擊者可向加密預言機查詢 $m_0$ 得到 $c_0$，隨後比對挑戰密文 $c^*$ 是否等於 $c_0$，即可 100% 辨別明文來源",
            "因為確定性加密無法加密超過 64 位元的區塊",
            "因為金鑰會在第 2 次加密時自動外洩"
        ],
        "answer": 1,
        "explanation": "確定性加密對相同明文產生相同密文。在 CPA 遊戲中攻擊者手握預言機，只要先查 $m_0$ 的密文，收到挑戰密文後直接比對即可獲勝，優勢度恆為 1。",
        "pitfalls": "誤以為是演算法數學不夠複雜，這是確定性映射的固有結構弱點，CPA 安全加密必須具備隨機性或狀態。",
        "reference": "The Joy of Cryptography, Ch. 7.1, p. 130"
    },
    {
        "id": "q-joy-7-2",
        "moduleId": "mod-joy-7",
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
        "reference": "The Joy of Cryptography, Ch. 7.3, p. 135"
    },
    {
        "id": "q-joy-7-3",
        "moduleId": "mod-joy-7",
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
        "id": "q-joy-7-4",
        "moduleId": "mod-joy-7",
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
]

joy_glossary = [
    {
        "term": "Kerckhoffs's Principle",
        "chinese": "柯克霍夫原則",
        "category": "基礎概念 (Ch 1)",
        "definition": "加密演算法必須假設完全公開，系統的安全性必須完全建立在金鑰的保密性之上。",
        "pitfall": "切勿實施『隱蔽式安全（Security through Obscurity）』，私有演算法往往暗藏致命設計漏洞。"
    },
    {
        "term": "Perfect Secrecy",
        "chinese": "完美保密性",
        "category": "資訊理論 (Ch 1)",
        "definition": "觀察到密文前後，明文的後驗機率嚴格等於先驗機率：$P[M=m|C=c] = P[M=m]$。即使攻擊者擁有無限算力亦不可破譯。",
        "pitfall": "達成完美保密性必須付出 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 的代價，實務上難以大規模應用。"
    },
    {
        "term": "One-Time Pad (OTP)",
        "chinese": "單次密鑰",
        "category": "對稱加密 (Ch 1)",
        "definition": "密碼學經典機制，加密 $c = m \\oplus k$，具備完美保密性，但金鑰長度必須與明文相同且嚴禁重複使用。",
        "pitfall": "若金鑰重複使用兩次，$c_1 \\oplus c_2 = m_1 \\oplus m_2$ 會直接消除金鑰並洩漏明文。"
    },
    {
        "term": "The Hybrid Technique",
        "chinese": "混合證明技術",
        "category": "證明技術 (Ch 2)",
        "definition": "在真實遊戲與目標遊戲間構造序列遊戲 $G_0, G_1, \\dots, G_k$，每步僅微調單一元件，透過三角不等式將總優勢度限制在各步驟差異之和。",
        "pitfall": "中間遊戲的總數量 $k$ 必須為多項式大小，否則累積優勢度無法保證可忽略性。"
    },
    {
        "term": "Advantage",
        "chinese": "優勢度",
        "category": "安全模型 (Ch 2)",
        "definition": "衡量攻擊者區分兩遊戲或破譯機制的指標：$\\mathbf{Adv} = |P[\\text{Output 1 in Game 0}] - P[\\text{Output 1 in Game 1}]|$。",
        "pitfall": "優勢度為可忽略函數才算安全；常數優勢（如 0.5 或 1）代表系統被攻破。"
    },
    {
        "term": "PPT (Probabilistic Polynomial Time)",
        "chinese": "機率多項式時間",
        "category": "複雜度理論 (Ch 4)",
        "definition": "現實可行攻擊者的運算模型。運算步數受安全參數的多項式限制，可進行隨機硬幣投擲分支。",
        "pitfall": "PPT 排除非現實的指數窮舉（如遍歷 $2^{128}$ 金鑰）。"
    },
    {
        "term": "Negligible Function",
        "chinese": "可忽略函數",
        "category": "複雜度理論 (Ch 4)",
        "definition": "衰減速度超越任何多項式倒數的函數：對任意 $c>0$，存在 $n_0$ 使得 $n>n_0$ 時 $\\mu(n) < 1/n^c$。",
        "pitfall": "$1/n^{10}$ 衰減很慢不是可忽略函數；$2^{-n}$ 與 $2^{-\\sqrt{n}}$ 才是可忽略函數。"
    },
    {
        "term": "Birthday Bound",
        "chinese": "生日界 / 生日問題機率",
        "category": "機率推導 (Ch 4)",
        "definition": "從大小 $N$ 集合中隨機抽樣 $q$ 次，碰撞機率約為 $q^2 / (2N)$。當 $q \\approx \\sqrt{N}$ 時碰撞機率達約 50%。",
        "pitfall": "64 位元區塊密碼在加密 $2^{32}$ 區塊時即面臨生日碰撞（Sweet32 攻擊），現代應使用 128 位元 AES。"
    },
    {
        "term": "PRG (Pseudorandom Generator)",
        "chinese": "偽隨機生成器",
        "category": "核心原語 (Ch 5)",
        "definition": "確定性演算法，將短種子 $s \\in \\{0, 1\\}^\\lambda$ 擴展為長偽隨機場 $G(s)$，且對任意 PPT 區分器與真隨機不可區分。",
        "pitfall": "PRG 是確定性的，並非真正隨機，但能以短金鑰實現 Pseudo-OTP 加密。"
    },
    {
        "term": "Symmetric Ratchet",
        "chinese": "對稱棘輪",
        "category": "通訊應用 (Ch 5)",
        "definition": "利用 PRG 單向演進狀態金鑰並立即銷毀舊金鑰的機制，實現前向保密（Forward Secrecy）。",
        "pitfall": "只要舊狀態徹底從記憶體抹除，即使當前狀態遭竊，過往通訊紀錄依然無法逆推。"
    },
    {
        "term": "PRF (Pseudorandom Function)",
        "chinese": "偽隨機函數",
        "category": "核心原語 (Ch 6)",
        "definition": "帶金鑰函數族 $F_k$，任何 PPT 攻擊者透過黑盒子預言機查詢時，無法將其與真正均勻隨機的函數區分。",
        "pitfall": "PRF 通常不具備可逆性，輸出允許碰撞。"
    },
    {
        "term": "PRP (Pseudorandom Permutation)",
        "chinese": "偽隨機置換 / 分組密碼",
        "category": "核心原語 (Ch 6)",
        "definition": "雙射（一對一且映成）的函數族 $P_k$，正向與反向皆為多項式時間可計算。為分組密碼（如 AES）的理論抽象。",
        "pitfall": "PRP 不允許碰撞，與 PRF 的差異受限於生日碰撞界（Switching Lemma）。"
    },
    {
        "term": "Strong PRP",
        "chinese": "強偽隨機置換",
        "category": "核心原語 (Ch 6)",
        "definition": "面對能同時查詢正向加密預言機與反向解密預言機的攻擊者，依然無法與隨機置換區分的 PRP。",
        "pitfall": "由 Luby-Rackoff 定理：3 輪 Feistel 僅為 PRP，必須達到 4 輪才可保證 Strong PRP。"
    },
    {
        "term": "IND-CPA",
        "chinese": "選擇明文攻擊不可區分性",
        "category": "安全模型 (Ch 7)",
        "definition": "攻擊者擁有加密預言機查詢權限，給定明文對 $(m_0, m_1)$，無法以顯著優勢猜中挑戰密文由何者加密而成。",
        "pitfall": "任何確定性加密演算法絕對無法達到 IND-CPA 安全，必須引入隨機 IV 或 Nonce 狀態。"
    },
    {
        "term": "Pseudorandom Ciphertexts",
        "chinese": "偽隨機密文",
        "category": "安全屬性 (Ch 7)",
        "definition": "密文外觀在多項式時間內與純隨機二進位字串不可區分，能徹底掩蓋訊息長度、協議特徵與格式元數據。",
        "pitfall": "偽隨機密文仍需搭配 MAC 才能抵禦主動的中間人竄改攻擊。"
    }
]

js_content = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source strictly aligned with The Joy of Cryptography (Mike Rosulek)
// Chapters included: 0, 1, 2, 4, 5, 6, 7

const MODULES_DATA = {json.dumps(joy_modules, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(joy_quizzes, ensure_ascii=False, indent=2)};

const GLOSSARY_DATA = {json.dumps(joy_glossary, ensure_ascii=False, indent=2)};
"""

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated js/data.js aligned with Joy of Cryptography!")
print(f"Modules: {len(joy_modules)} (Ch 0, 1, 2, 4, 5, 6, 7)")
print(f"Quizzes: {len(joy_quizzes)}")
print(f"Glossary: {len(joy_glossary)}")
