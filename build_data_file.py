# -*- coding: utf-8 -*-
"""
Script to generate js/data.js containing complete cryptographic modules,
quizzes, and glossary for the review and interactive learning website.
"""

import json

modules_data = [
    {
        "id": "mod-0",
        "number": "00",
        "title": "古典密碼學與密碼分析",
        "subtitle": "Historical Ciphers & Cryptanalysis",
        "source": "Introduction to Modern Cryptography (Katz & Lindell Ch.1)",
        "summary": "探討密碼學發展初期的替換與移位機制、柯克霍夫原則（Kerckhoffs's Principle），以及利用語言統計特徵進行頻率分析破譯古典密碼的經典方法。",
        "sections": [
            {
                "title": "柯克霍夫原則與密碼學基本假設",
                "content": [
                    "**Kerckhoffs's Principle（柯克霍夫原則）**：加密系統的安全性絕不能仰賴於演算法本身的保密，而必須完全建立在金鑰（Secret Key）的保密之上。這也是現代密碼學「開放演算法、保密金鑰」的核心鐵律。",
                    "**秘密演算法的風險（Security through Obscurity）**：若演算法外洩，整個密碼系統將全面崩潰且無法補救；反之若僅金鑰外洩，只需撤銷並重新產生新金鑰即可恢復安全性。"
                ]
            },
            {
                "title": "三大古典密碼機制與數學定義",
                "content": [
                    "**1. 凱撒移位密碼（Shift Cipher / Caesar Cipher）**：",
                    "- 明文與密文空間 $\\mathcal{M} = \\mathcal{C} = \\mathbb{Z}_{26}$，金鑰空間 $\\mathcal{K} = \\{0, 1, \\dots, 25\\}$。",
                    "- 加密演算法：$c = \\mathrm{Enc}_k(m) = (m + k) \\pmod{26}$。",
                    "- 解密演算法：$m = \\mathrm{Dec}_k(c) = (c - k) \\pmod{26}$。",
                    "- 安全性漏洞：金鑰空間大小僅 $|\\mathcal{K}| = 26$。攻擊者可在數秒內進行暴力窮舉攻擊（Brute-force Key Search）。",
                    "**2. 單字母替換密碼（Monoalphabetic Substitution Cipher）**：",
                    "- 金鑰 $k$ 為 26 個字母的一個置換排列（Permutation $\\pi$），金鑰空間 $|\\mathcal{K}| = 26! \\approx 4 \\times 10^{26}$。",
                    "- 雖然金鑰空間龐大無法窮舉，但每個字母的一對一對應保留了語言的頻率分佈特徵，極易被「字母頻率分析」攻破。",
                    "**3. 維吉尼亞多表密碼（Vigenère Cipher）**：",
                    "- 金鑰為長度為 $t$ 的字串 $k = (k_1, k_2, \\dots, k_t)$，對明文依序做移位：$c_i = (m_i + k_{(i \\pmod t)}) \\pmod{26}$。",
                    "- 多表平滑了單一字母頻率，但在長密文中依然會週期性重複。"
                ]
            },
            {
                "title": "古典密碼分析技術（Cryptanalysis）",
                "content": [
                    "**單字母頻率分析（Frequency Analysis）**：在自然英文文本中，字母出現機率高度不均勻（例如 'E' 約佔 12.7%，'T' 約佔 9.1%，而 'Z'、'Q' 均低於 0.1%）。觀察密文中出現頻率最高者即可高機率推導對應字母。",
                    "**卡西斯基檢驗法（Kasiski Examination）**：尋找密文中重複出現長度大於等於 3 的字串，記錄各重複字串之間的間距，各間距的最大公因數（GCD）高機率即為金鑰長度 $t$。",
                    "**重合指數（Index of Coincidence, IC）**：定義為從密文中隨機抽取兩個字母時，兩者相同的機率：",
                    "$$\\mathrm{IC} = \\sum_{i=0}^{25} \\frac{f_i(f_i - 1)}{N(N - 1)}$$",
                    "其中 $N$ 為密文總長度，$f_i$ 為第 $i$ 個字母的出現次數。純隨機字串的 $\\mathrm{IC} \\approx 0.038$，而正常英文文本的 $\\mathrm{IC} \\approx 0.065$。透過比較單一週期子串的 $\\mathrm{IC}$ 可精準驗證金鑰長度 $t$。"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「金鑰空間龐大就代表系統絕對安全」——單字母替換密碼的 $|\\mathcal{K}| = 26!$ 超過 80 位元，但因為未能隱藏統計特徵，完全不堪一擊。",
                    "**誤區二**：「多表替換可以徹底解決頻率外洩」——只要密文長度大於金鑰週期，分組後的每一條子密文依然本質上是單字母移位密碼。"
                ]
            }
        ]
    },
    {
        "id": "mod-1",
        "number": "01",
        "title": "資訊理論安全性與完美保密",
        "subtitle": "Information-Theoretic Security & Perfectly Secret Encryption",
        "source": "Introduction to Modern Cryptography (Katz & Lindell Ch.2) & Cyrptography.pdf",
        "summary": "探討 Shannon 提出之資訊理論安全性定義，介紹具備無條件安全性的單次密鑰（One-Time Pad），以及揭示其代價的 Shannon 不可能定理。",
        "sections": [
            {
                "title": "完美保密性（Perfect Secrecy）之嚴格定義",
                "content": [
                    "**Shannon 的直覺觀念**：觀察密文不應該提供關於明文的任何額外資訊。",
                    "**形式化定義**：一個定義於明文空間 $\\mathcal{M}$、密文空間 $\\mathcal{C}$、金鑰空間 $\\mathcal{K}$ 的加密架構 $(\\mathrm{Gen}, \\mathrm{Enc}, \\mathrm{Dec})$ 達到完美保密，若對於明文上的任意先驗機率分佈、任意明文 $m \\in \\mathcal{M}$ 以及任意密文 $c \\in \\mathcal{C}$（滿足 $P[C=c] > 0$），均滿足：",
                    "$$P[M = m \\mid C = c] = P[M = m]$$",
                    "即明文的**後驗機率等於先驗機率**。",
                    "**等價定義（完美不可區分性）**：對於任意兩個明文 $m_0, m_1 \\in \\mathcal{M}$ 以及任意密文 $c \\in \\mathcal{C}$：",
                    "$$P[\\mathrm{Enc}_K(m_0) = c] = P[\\mathrm{Enc}_K(m_1) = c]$$"
                ]
            },
            {
                "title": "單次密鑰（One-Time Pad, OTP / Vernam Cipher）",
                "content": [
                    "由 Gilbert Vernam 於 1917 年發明。明文、密文與金鑰均為長度相同的二進位字串：$\\mathcal{M} = \\mathcal{C} = \\mathcal{K} = \\{0, 1\\}^\\ell$。",
                    "- **金鑰生成**：$K \\leftarrow \\{0, 1\\}^\\ell$ 均勻隨機抽取，即每個金鑰選中機率為 $2^{-\\ell}$。",
                    "- **加密**：$C = \\mathrm{Enc}_K(M) = M \\oplus K$（位元互斥或運算 XOR）。",
                    "- **解密**：$M = \\mathrm{Dec}_K(C) = C \\oplus K$。",
                    "**完美安全性證明推導**：",
                    "對於任意固定明文 $m$ 與密文 $c$，使 $\\mathrm{Enc}_k(m) = c$ 成立的金鑰 $k$ 恰好只有一個，即 $k = m \\oplus c$。因此：",
                    "$$P[C = c \\mid M = m] = P[K = m \\oplus c] = \\frac{1}{2^\\ell}$$",
                    "由於該機率對任意明文 $m$ 皆為常數 $2^{-\\ell}$，與 $m$ 完全獨立，故 One-Time Pad 嚴格滿足完美保密性！"
                ]
            },
            {
                "title": "Shannon 不可能定理（Shannon's Impossibility Theorem）",
                "content": [
                    "**定理內容**：若一個加密架構 $(\\mathrm{Gen}, \\mathrm{Enc}, \\mathrm{Dec})$ 滿足完美保密性，則其金鑰空間大小必須大於或等於明文空間大小：",
                    "$$|\\mathcal{K}| \\ge |\\mathcal{M}|$$",
                    "若在定長二進位字串情況下，金鑰長度必須大於或等於明文長度（$\\ell_K \\ge \\ell_M$）。",
                    "**證明要點（反證法）**：",
                    "假設 $|\\mathcal{K}| < |\\mathcal{M}|$。任取密文 $c$。考慮可能解密出的所有可能明文集合 $\\mathcal{M}(c) = \\{\\mathrm{Dec}_k(c) \\mid k \\in \\mathcal{K}\\}$。因為金鑰數量只有 $|\\mathcal{K}|$ 個，所以 $|\\mathcal{M}(c)| \\le |\\mathcal{K}| < |\\mathcal{M}|$。這意味著必然存在某個明文 $m^* \\in \\mathcal{M}$ 不在 $\\mathcal{M}(c)$ 中。對於該明文 $m^*$，$P[M = m^* \\mid C = c] = 0 \\ne P[M = m^*]$，產生矛盾！故 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 必然成立。"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「One-Time Pad 是完美的，所以我們在實務傳輸中全部用 OTP 即可」——Shannon 定理揭示了極大代價：要加密 1 GB 資料就必須預先安全傳遞 1 GB 的隨機金鑰，若雙方已有安全通道傳送金鑰，直接傳送明文即可。",
                    "**誤區二**：「One-Time Pad 的金鑰可以重複使用兩次」——絕對不行！這會引發嚴重的 Two-Time Pad 攻擊（見模組 2）。"
                ]
            }
        ]
    },
    {
        "id": "mod-2",
        "number": "02",
        "title": "可證明安全性思維與計算密碼學",
        "subtitle": "The Provable Security Mindset & Computational Cryptography",
        "source": "1.2 The Provable Security Mindset.pdf & Cyrptography.pdf",
        "summary": "現代密碼學的核心轉折：從無法實用的無條件保密轉向計算安全性。建立機率多項式時間（PPT）、可忽略函數、安全遊戲（Security Games）、歸約證明（Reductions）與 Two-Time Pad 破解手法。",
        "sections": [
            {
                "title": "計算安全性（Computational Security）的兩大鬆綁",
                "content": [
                    "為突破 Shannon 定理 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 的限制，現代密碼學做出了兩項合理的現實假設鬆綁：",
                    "1. **運算資源限制**：不要求能防範「擁有無限算力的攻擊者」，只要求能防範「在合理多項式時間內運行的攻擊者（Probabilistic Polynomial Time, PPT）」。",
                    "2. **成功機率容許**：不要求攻擊者破譯機率為 0，只要求其成功的優勢小於任何多項式的倒數，即為「可忽略機率（Negligible Probability）」。"
                ]
            },
            {
                "title": "核心數學概念：PPT 與可忽略函數（Negligible Function）",
                "content": [
                    "**安全參數（Security Parameter, $\\lambda$ 或 $n$）**：所有演算法（生成、加密、解密）的時間複雜度與金鑰長度皆以 $n$ 的多項式表示。",
                    "**可忽略函數 $\\mathrm{negl}(n)$ 之嚴格定義**：",
                    "一個函數 $\\mu(n): \\mathbb{N} \\to \\mathbb{R}$ 稱為可忽略（Negligible），若對於任意正整數常數 $c > 0$，皆存在一個門檻 $N_c$，使得對所有 $n > N_c$ 均滿足：",
                    "$$\\mu(n) < \\frac{1}{n^c}$$",
                    "常見範例：$2^{-n}$、$2^{-\\sqrt{n}}$ 為可忽略函數；而 $n^{-100}$、$1/\\log n$ 則不是可忽略函數。"
                ]
            },
            {
                "title": "安全遊戲範式與不可區分性（Security Games & Indistinguishability）",
                "content": [
                    "現代密碼學透過挑戰者（Challenger）與攻擊者（Adversary $\\mathcal{A}$）進行形式化遊戲來定義安全性：",
                    "1. Challenger 生成金鑰 $k \\leftarrow \\mathrm{Gen}(1^n)$。",
                    "2. 攻擊者 $\\mathcal{A}$ 選擇兩個長度相同的明文 $m_0, m_1$ 送給 Challenger。",
                    "3. Challenger 均勻隨機擲硬幣拋出一位元 $b \\leftarrow \\{0, 1\\}$，計算挑戰密文 $c^* = \\mathrm{Enc}_k(m_b)$ 並回傳給 $\\mathcal{A}$。",
                    "4. $\\mathcal{A}$ 輸出其猜測 $b' \\in \\{0, 1\\}$。",
                    "5. 若 $b' = b$，則攻擊者獲勝。攻擊者的優勢度（Advantage）定義為：",
                    "$$\\mathbf{Adv}_{\\mathcal{A}}(n) = \\left| P[b' = b] - \\frac{1}{2} \\right|$$",
                    "若對所有 PPT 攻擊者 $\\mathcal{A}$，$\\mathbf{Adv}_{\\mathcal{A}}(n) \\le \\mathrm{negl}(n)$，則稱該加密方案在該威脅模型下安全。"
                ]
            },
            {
                "title": "經典漏洞推導：Two-Time Pad 攻擊與延展性",
                "content": [
                    "**1. Two-Time Pad 攻擊（重用金鑰攻擊）**：",
                    "- 若以相同金鑰 $k$ 加密兩條訊息 $m_1, m_2$：$c_1 = m_1 \\oplus k, \\quad c_2 = m_2 \\oplus k$。",
                    "- 攻擊者計算密文的 XOR：",
                    "$$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2$$",
                    "- 金鑰 $k$ 被完全消去！攻擊者獲得明文的 XOR 結果。利用自然語言中 ASCII 空白鍵（0x20）與字母 XOR 的大小寫互換特徵，攻擊者能以 Crib Dragging 技術完全還原兩篇明文！",
                    "**2. 延展性（Malleability / Bit-flipping Attack）**：",
                    "- 對密文 $c$ 翻轉特定位元 $\\Delta$，解密後的明文為 $m' = (c \\oplus \\Delta) \\oplus k = (c \\oplus k) \\oplus \\Delta = m \\oplus \\Delta$。",
                    "- OTP 只保證機密性，**完全不保證完整性（Integrity）**！"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「只要攻擊者破譯機率很低，例如 $1/n^2$，系統就是安全的」——錯誤！$1/n^2$ 是多項式級別，只要重複嘗試 $n^2$ 次（多項式時間內）即可攻破，絕非安全；只有小於任何多項式倒數的 $\\mathrm{negl}(n)$ 才是計算安全。",
                    "**誤區二**：「可證明安全證明了演算法不可能被攻破」——安全性證明是在特定數學假設（如 RSA 難題、LWE 難題）與特定威脅模型下的歸約，若實作存在側信道洩漏（Side-channel）或假設被推翻，證明便不再成立。"
                ]
            }
        ]
    },
    {
        "id": "mod-3",
        "number": "03",
        "title": "偽隨機性與原語建構理論",
        "subtitle": "Pseudorandomness: PRG, PRF, and PRP",
        "source": "1.4 Pseudorandomness.pdf & Cyrptography.pdf",
        "summary": "深入偽隨機生成器（PRG）、偽隨機函數（PRF）與偽隨機置換（PRP）三大核心原語，剖析 GGM 樹狀建構、CTR 模式以及 Feistel 網路與 Luby-Rackoff 定理。",
        "sections": [
            {
                "title": "三大核心原語定義與區別",
                "content": [
                    "**1. 偽隨機生成器（PRG, Pseudorandom Generator）**：",
                    "- 定義：確定性演算法 $G: \\{0, 1\\}^n \\to \\{0, 1\\}^{\\ell(n)}$，其中擴展長度 $\\ell(n) > n$。",
                    "- 安全性：對任意 PPT 區分器 $\\mathcal{D}$，難以區分「真隨機場 $r \\leftarrow \\{0, 1\\}^{\\ell(n)}$」與「偽隨機場 $G(s), s \\leftarrow \\{0, 1\\}^n$」：",
                    "$$\\mathbf{Adv}_{\\mathcal{D}}^{\\mathrm{PRG}} = |P[\\mathcal{D}(G(s)) = 1] - P[\\mathcal{D}(r) = 1]| \\le \\mathrm{negl}(n)$$",
                    "**2. 偽隨機函數（PRF, Pseudorandom Function）**：",
                    "- 定義：帶金鑰之有效率演算法 $F_k: \\{0, 1\\}^n \\to \\{0, 1\\}^n$，其中 $k \\leftarrow \\{0, 1\\}^n$。",
                    "- 安全性：攻擊者只能透過黑盒子預言機（Oracle）查詢。攻擊者無法區分自己面對的是 $F_k$ 還是真正隨機均勻挑選的函數 $f \\leftarrow \\mathrm{Funcs}(n, n)$。",
                    "**3. 偽隨機置換（PRP, Pseudorandom Permutation）**：",
                    "- 定義：雙射函數族 $P_k: \\{0, 1\\}^n \\to \\{0, 1\\}^n$ 且存在多項式時間反函數 $P_k^{-1}$。即分組密碼（Block Cipher，如 AES）的理論模型。"
                ]
            },
            {
                "title": "原語之間的互相建構架構",
                "content": [
                    "現代密碼學最重要的成果之一是三大原語在理論上的等價互換性：",
                    "**1. PRG $\\to$ PRF：GGM 建構法（Goldreich-Goldwasser-Micali）**",
                    "- 利用輸出長度翻倍的 PRG $G(s) = (G_0(s), G_1(s))$，建構一棵深度為 $n$ 的二元樹。",
                    "- 輸入 $x = x_1 x_2 \\dots x_n$ 時，依循位元路徑向左（$G_0$）或向右（$G_1$）遞迴擴展，最終葉節點即為 $F_k(x)$。",
                    "**2. PRF $\\to$ PRG：CTR 計數器串接模式**",
                    "- 給定 PRF $F_k$，設定計數器 $G(k) = F_k(0) \\,|\\, F_k(1) \\,|\\, F_k(2) \\dots$，可將短金鑰 $k$ 展開為任意長度的偽隨機串流。",
                    "**3. PRF $\\to$ PRP：Feistel 網路（Feistel Networks）**",
                    "- 利用非可逆的隨機輪函數 $F$，透過對稱的折疊結構建構可逆置換。"
                ]
            },
            {
                "title": "Feistel 網路與 Luby-Rackoff 定理推導",
                "content": [
                    "將輸入字串分為左右兩半 $(L_i, R_i)$。第 $i$ 輪運算規則：",
                    "$$L_{i+1} = R_i, \\quad R_{i+1} = L_i \\oplus F_{k_i}(R_i)$$",
                    "- **解密對稱性**：解密時只需將順序顛倒並使用相同輪函數 $F$：$R_i = L_{i+1}, L_i = R_{i+1} \\oplus F_{k_i}(L_{i+1})$。這意味著輪函數 $F$ 本身不需要具備可逆性！",
                    "**Luby-Rackoff 定理之輪數里程碑**：",
                    "- **1 輪與 2 輪**：絕不安全，可輕易構造區分器。",
                    "- **3 輪 Feistel**：在面對僅能查詢正向 $P_k$ 的攻擊者時，可證明為安全的偽隨機置換（PRP）。但在面對能同時查詢反向 $P_k^{-1}$ 的攻擊者時會被攻破！",
                    "- **4 輪 Feistel**：面對能自由查詢正向與反向的攻擊者，依然具備不可區分性，達到**強偽隨機置換（Strong PRP）**！"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「PRG 的輸出是真隨機的」——PRG 是完全確定性演算法，只要種子相同，產生的輸出完全相同；它只是在任何多項式時間演算法檢驗下『看起來』與真隨機無法區分。",
                    "**誤區二**：「3 輪 Feistel 已經是 PRP，所以已經具備最強安全性」——3 輪僅能抵抗正向 CPA 攻擊，面對可反向解密的 CCA 攻擊需要至少 4 輪。"
                ]
            }
        ]
    },
    {
        "id": "mod-4",
        "number": "04",
        "title": "選擇攻擊與安全性強度",
        "subtitle": "Chosen-Plaintext & Chosen-Ciphertext Attacks",
        "source": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf & Cyrptography.pdf",
        "summary": "探討 IND-CPA 與 IND-CCA 安全模型，揭露確定性加密為何必然崩潰，並逐步解析實務上最著名的 CBC 模式填充預言機攻擊（Padding Oracle Attack）。",
        "sections": [
            {
                "title": "IND-CPA：選擇明文攻擊模型",
                "content": [
                    "**CPA 威脅模型**：攻擊者不僅能拿到密文，還能任意取得其所選擇之明文的對應密文（即擁有加密預言機 $\\mathcal{O}_{\\mathrm{Enc}_k}(\\cdot)$ 的無限次多項式查詢權限）。",
                    "**致命結論：確定性加密（Deterministic Encryption）無法達到 IND-CPA**：",
                    "- 若加密演算法每次對相同的 $m$ 產出相同的 $c$：",
                    "- 攻擊者只需向預言機查詢 $c_0 = \\mathrm{Enc}_k(m_0)$。",
                    "- 在挑戰階段送出 $m_0, m_1$，收到挑戰密文 $c^*$。",
                    "- 若 $c^* == c_0$，攻擊者立即確信 $b=0$，否則 $b=1$。勝率為 100%（$\\mathbf{Adv} = 1/2$）！",
                    "- **解決方案**：IND-CPA 加密演算法必須具備**隨機性（Randomized）**或維護狀態（Nonce / IV）。"
                ]
            },
            {
                "title": "以 PRF 建構 IND-CPA 安全加密",
                "content": [
                    "設 $F$ 為安全 PRF，金鑰為 $k$：",
                    "- **加密**：要加密明文 $m \\in \\{0, 1\\}^n$，均勻隨機挑選初始化向量 $r \\leftarrow \\{0, 1\\}^n$，輸出密文對：",
                    "$$c = \\langle r, \\; F_k(r) \\oplus m \\rangle$$",
                    "- **解密**：給定密文 $\\langle r, c_1 \\rangle$，明文為 $m = c_1 \\oplus F_k(r)$。",
                    "- **安全性直覺**：由於 $r$ 是隨機挑選的，重複機率僅 $2^{-n}$。每次產生的遮罩 $F_k(r)$ 均如同獨立全新的 OTP 金鑰，故達到 IND-CPA 安全。"
                ]
            },
            {
                "title": "IND-CCA 與 Padding Oracle 攻擊深度推導",
                "content": [
                    "**IND-CCA 模型**：攻擊者額外獲得**解密預言機（Decryption Oracle）**權限。攻擊者不能直接將挑戰密文 $c^*$ 送給解密預言機，但可查詢任何 $c \\ne c^*$ 的解密結果。",
                    "**CBC 模式之 Padding Oracle 攻擊（Serge Vaudenay, 2002）**：",
                    "- **背景**：分組密碼採 CBC 模式，明文末端使用 PKCS#7 填充。若區塊為 16 位元組，缺 1 位元組補 `0x01`，缺 2 位元組補 `0x02 0x02`，以此類推。",
                    "- **預言機洩漏**：伺服器若解密後發現填充錯誤，會回傳不同錯誤碼（Padding Error）。",
                    "- **攻擊運算步驟**：",
                    "1. 設前一密文區塊為 $C_1$，目標密文區塊為 $C_2$。解密時 $P_2 = D_k(C_2) \\oplus C_1$。令中間值 $I_2 = D_k(C_2)$。",
                    "2. 攻擊者構造偽造的前一區塊 $C'_1$。欲破解 $P_2$ 的最後一位元組：",
                    "3. 遍歷 $C'_1[15]$ 從 `0x00` 到 `0xFF`，送交伺服器解密。當伺服器回傳「填充正確」時，代表解密末尾等於 `0x01`：",
                    "$$I_2[15] \\oplus C'_1[15] = 0x01 \\implies I_2[15] = C'_1[15] \\oplus 0x01$$",
                    "4. 攻擊者計算出中間值 $I_2[15]$ 後，真正的明文立即還原：",
                    "$$P_2[15] = I_2[15] \\oplus C_1[15]$$",
                    "5. 接著設定 $C'_1[15] = I_2[15] \\oplus 0x02$，繼續暴力破解 $C'_1[14]$ 使其結尾為 `0x02 0x02`。以此類推，**每個位元組最多只需嘗試 256 次，即可在不持有金鑰的情況下完全還原全部明文**！"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「IND-CPA 安全的演算法已經很安全，足夠抵禦所有攻擊」——大錯特錯！純 CBC 模式與 CTR 模式皆是 IND-CPA 安全，但在面對能夠篡改傳輸封包的活躍攻擊者（Man-in-the-Middle）時，會遭到 Padding Oracle 徹底粉碎。",
                    "**誤區二**：「避免 Padding Oracle 的方法是修復 Padding 檢查程式碼使其更快」——只要伺服器解密後回傳的反應（時間差異、錯誤訊息）透露了 Padding 是否合法，側信道漏洞依然存在；根本解法是採用驗證式加密（AE）。"
                ]
            }
        ]
    },
    {
        "id": "mod-5",
        "number": "05",
        "title": "訊息驗證碼與驗證式加密",
        "subtitle": "Message Authentication Codes & Authenticated Encryption",
        "source": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf",
        "summary": "解析資料完整性之核心原語 MAC 與 EUF-CMA 安全定義，探討 CBC-MAC 與 HMAC，以及結合機密性與完整性的驗證式加密（Authenticated Encryption）三大範式。",
        "sections": [
            {
                "title": "訊息驗證碼（MAC, Message Authentication Code）",
                "content": [
                    "**目標**：確保訊息的真實性（Authenticity）與完整性（Integrity），防止攻擊者未經授權竄改內容。",
                    "**演算法組成**：$(\\mathrm{Gen}, \\mathrm{Mac}, \\mathrm{Vrfy})$。標籤產生 $t \\leftarrow \\mathrm{Mac}_k(m)$，驗證 $\\mathrm{Vrfy}_k(m, t) \\in \\{1, 0\\}$。",
                    "**安全模型：EUF-CMA（選擇訊息攻擊下的存在不可偽造性）**：",
                    "- 攻擊者可向 MAC 預言機查詢任意多筆訊息的合法標籤。",
                    "- 攻擊者獲勝條件：產出一組全新訊息 $m^*$（未曾查詢過）與其合法標籤 $t^*$，使得 $\\mathrm{Vrfy}_k(m^*, t^*) = 1$。",
                    "- 若對所有 PPT 攻擊者獲勝機率均為 $\\mathrm{negl}(n)$，則該 MAC 是 EUF-CMA 安全的。"
                ]
            },
            {
                "title": "經典 MAC 建構：CBC-MAC 與 HMAC",
                "content": [
                    "**1. CBC-MAC（針對固定長度訊息）**：",
                    "- 利用分組密碼進行 CBC 鏈接，最後一個區塊的輸出即為 MAC 標籤 $t$。",
                    "- **致命缺陷（長度延伸攻擊）**：若用於可變長度訊息，給定一區塊 $(m_1, t_1)$，攻擊者可輕易偽造兩區塊訊息 $m_1 \\,|\\, (m_2 \\oplus t_1)$ 的合法標籤恰為 $t_2$！",
                    "- **修復版**：CMAC 或 ECBC-MAC（在末尾使用額外金鑰進行遮罩）。",
                    "**2. HMAC（基於雜湊函數的 MAC）**：",
                    "- 結構：$\\mathrm{HMAC}_K(m) = H\\big((K \\oplus \\mathrm{opad}) \\,\\|\\, H((K \\oplus \\mathrm{ipad}) \\,\\|\\, m)\\big)$。",
                    "- 雙重雜湊設計能完全阻斷雜湊函數（如 SHA-256）的長度延伸攻擊（Length Extension Attack）。"
                ]
            },
            {
                "title": "驗證式加密（AE, Authenticated Encryption）",
                "content": [
                    "同時提供機密性（Confidentiality）與完整性（Integrity）。",
                    "**核心定理**：",
                    "$$\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$$",
                    "（只要密文具備密文完整性 INT-CTXT，任何偽造密文都會在解密前被拒絕，解密預言機便失去功效，直接升格為最強的 IND-CCA 安全！）",
                    "**三大組合範式評比**：",
                    "1. **Encrypt-and-MAC**（如 SSH 早期）：$c = \\mathrm{Enc}_{k_1}(m), t = \\mathrm{Mac}_{k_2}(m)$。**不安全**！MAC 標籤 $t$ 可能直接外洩明文資訊。",
                    "2. **MAC-then-Encrypt**（如 SSL/TLS 早期）：$t = \\mathrm{Mac}_{k_2}(m), c = \\mathrm{Enc}_{k_1}(m \\,|\\, t)$。**脆弱**！容易受到 Padding Oracle 攻擊破壞。",
                    "3. **Encrypt-then-MAC（EtM）**（IPsec, 現代標準）：$c = \\mathrm{Enc}_{k_1}(m), t = \\mathrm{Mac}_{k_2}(c)$。**唯一通用且安全**！接收端先校驗 $t$，不合法直接丟棄，完全不執行解密！",
                    "**現代 AEAD 演算法**：AES-GCM（Galois/Counter Mode）、ChaCha20-Poly1305。"
                ]
            },
            {
                "title": "核心防錯提醒（Pitfall Alerts）",
                "content": [
                    "**誤區一**：「加密（Encryption）自然就能保護資料不被竄改」——絕對不行！純加密只防偷看，不防篡改（如 OTP 的位元翻轉攻擊）。",
                    "**誤區二**：「在 Encrypt-then-MAC 中，加密與 MAC 可以使用同一個金鑰 $k$」——嚴格禁止！金鑰隔離是密碼學基本原則，共用金鑰可能導致加密與 MAC 的運算特性相互干擾而瓦解安全性證明。"
                ]
            }
        ]
    }
]

quiz_data = [
    # Module 0
    {
        "id": "q0-1",
        "moduleId": "mod-0",
        "category": "概念辨析",
        "question": "根據柯克霍夫原則（Kerckhoffs's Principle），一個密碼系統的安全性應該建立在何種前提之上？",
        "options": [
            "加密演算法細節必須被嚴格保密，防止外界得知運算邏輯",
            "即使加密演算法被完全公開，只要金鑰（Secret Key）保密，系統就必須維持安全",
            "金鑰空間 $|\\mathcal{K}|$ 必須大於等於 $2^{128}$ 才能保證絕對不被攻破",
            "只要更換為多表替換密碼，即可確保系統的數學安全性"
        ],
        "answer": 1,
        "explanation": "柯克霍夫原則是現代密碼學的基石：密碼系統的安全絕不能仰賴於演算法的隱蔽（Security through Obscurity），而必須完全取決於金鑰的保密性。公開的演算法能接受大眾檢驗與密碼分析，而金鑰外洩時僅需替換金鑰即可恢復安全性。",
        "pitfalls": "將「演算法保密」誤認為更安全，忽視了演算法一旦逆向工程外洩將導致系統全面崩潰的不可逆後果。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 1, p. 6"
    },
    {
        "id": "q0-2",
        "moduleId": "mod-0",
        "category": "數學演算",
        "question": "單字母替換密碼（Monoalphabetic Substitution Cipher）的金鑰空間大小 $|\\mathcal{K}| = 26! \\approx 4 \\times 10^{26}$。為何此密碼系統在實務上依舊能被輕易攻破？",
        "options": [
            "因為金鑰空間雖然龐大，但現代電腦可在數分鐘內窮舉 $26!$ 種組合",
            "因為加密過程未將字母轉換為二進位位元組進行 XOR 運算",
            "因為每個明文字母與密文字母始終保持一對一固定映射，完全保留了自然語言的統計頻率特徵",
            "因為卡西斯基檢驗法可以直接算出單字母替換密碼的金鑰長度"
        ],
        "answer": 2,
        "explanation": "單字母替換密碼雖然無法使用暴力窮舉破解，但因對應關係固定，密文中出現頻率最高的字母（例如約佔 13% 者）極可能對應明文中的 'E'，透過單字母頻率分析與雙字母組合（Digraphs），即可在無需窮舉的情況下輕易還原明文。",
        "pitfalls": "誤以為「金鑰空間大就等於不可破解」，忽略了統計頻率特徵的外洩完全繞過了金鑰窮舉。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 1, p. 9"
    },
    {
        "id": "q0-3",
        "moduleId": "mod-0",
        "category": "分析推導",
        "question": "在使用重合指數（Index of Coincidence, IC）對維吉尼亞密碼（Vigenère Cipher）進行密碼分析時，其核心統計原理為何？",
        "options": [
            "當推測的金鑰週期長度 $t$ 正確時，將密文分組後的每組子密文之 IC 值會接近純隨機字串的 $0.038$",
            "當推測的金鑰週期長度 $t$ 正確時，將密文分組後的每組子密文相當於單字母移位密碼，其 IC 值會接近正常英語文本的 $0.065$",
            "重合指數是用來計算解密所需的多項式時間複雜度，IC 值越大代表破解越慢",
            "重合指數可以直接計算出金鑰的互斥或數值，無需透過單字母頻率推導"
        ],
        "answer": 1,
        "explanation": "隨機均勻字串中隨機抽取兩字母相同的機率約為 $1/26 \\approx 0.038$；而在正常英語文本中，由於字母分佈極不均勻，該機率躍升至約 $0.065$。若分組週期 $t$ 猜測正確，子密文內文字均以相同金鑰移位，保留了英語的非均勻頻率特性，故 IC 值會趨近 $0.065$。",
        "pitfalls": "混淆隨機文字（0.038）與英語文本（0.065）的 IC 理論基準數值。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 1"
    },
    {
        "id": "q0-4",
        "moduleId": "mod-0",
        "category": "概念辨析",
        "question": "使用凱撒移位密碼（Shift Cipher）對訊息進行加密時，其致命的結構弱點為何？",
        "options": [
            "加密後的密文長度大於明文長度",
            "有效金鑰空間大小只有 $|\\mathcal{K}| = 26$，攻擊者可使用暴力搜尋在瞬間完成所有解密測試",
            "移位運算在解密時無法還原原始字元",
            "運算需要龐大的機率多項式時間"
        ],
        "answer": 1,
        "explanation": "凱撒移位密碼定義於模 26 運算，$k \\in \\{0, \\dots, 25\\}$，金鑰空間只有 26 種可能，只需逐一列印 26 種解密結果，肉眼即可直接辨識出有意義的明文。",
        "pitfalls": "誤將凱撒移位密碼與複雜多表密碼的漏洞混為一談。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 1, p. 8"
    },

    # Module 1
    {
        "id": "q1-1",
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
        "explanation": "Shannon 定義完美保密性為：在觀察到特定密文 $C=c$ 後，明文為 $m$ 的後驗機率 $P[M=m \\mid C=c]$，與未看到密文前的先驗機率 $P[M=m]$ 完全相等。這意味著密文未透露任何有關明文的新資訊。",
        "pitfalls": "誤選 $P[M=m \\mid C=c] = 0$（代表不可能解密成功），完美保密不是機率為 0，而是後驗等於先驗。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 2, p. 25"
    },
    {
        "id": "q1-2",
        "moduleId": "mod-1",
        "category": "數學演算",
        "question": "在 One-Time Pad（OTP）中，設明文空間 $\\mathcal{M} = \\{0, 1\\}^\\ell$。若金鑰 $K$ 是由均勻隨機選取，則對於任意固定明文 $m$ 與任意密文 $c$，$P[C = c \\mid M = m]$ 的數值為何？",
        "options": [
            "$1$",
            "$\\frac{1}{2^\\ell}$",
            "$\\frac{1}{\\ell}$",
            "$0$"
        ],
        "answer": 1,
        "explanation": "因為 $C = M \\oplus K$，給定明文 $M=m$，要產生密文 $c$ 的唯一充要條件為 $K = m \\oplus c$。由於金鑰是在長度為 $\\ell$ 的字串中均勻隨機抽取，特定金鑰出現的機率嚴格等於 $1/2^\\ell$。該機率與明文 $m$ 完全無關，證明了 OTP 的完美安全性。",
        "pitfalls": "誤以為機率會受到明文長度 $\\ell$ 的倍數或文字內容影響。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 2, p. 28"
    },
    {
        "id": "q1-3",
        "moduleId": "mod-1",
        "category": "分析推導",
        "question": "根據 Shannon 不可能定理（Shannon's Impossibility Theorem），任何達到完美保密性的加密系統，其金鑰空間 $|\\mathcal{K}|$ 與明文空間 $|\\mathcal{M}|$ 必須滿足何種關係？",
        "options": [
            "$|\\mathcal{K}| \\le |\\mathcal{M}|$",
            "$|\\mathcal{K}| \\ge |\\mathcal{M}|$",
            "$|\\mathcal{K}| = \\log_2 |\\mathcal{M}|$",
            "$|\\mathcal{K}| = \\sqrt{|\\mathcal{M}|}$"
        ],
        "answer": 1,
        "explanation": "Shannon 定理證明：若 $|\\mathcal{K}| < |\\mathcal{M}|$，則對於某個密文 $c$，可能解密出的明文集合大小最多只有 $|\\mathcal{K}|$ 個，必定存在某些明文永遠無法由 $c$ 解出（後驗機率為 0），從而破壞完美保密。因此金鑰空間必須至少與明文空間一樣大（$|\\mathcal{K}| \\ge |\\mathcal{M}|$）。",
        "pitfalls": "誤記為 $|\\mathcal{K}| \\le |\\mathcal{M}|$ 或對數關係。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 2, p. 33"
    },
    {
        "id": "q1-4",
        "moduleId": "mod-1",
        "category": "概念辨析",
        "question": "One-Time Pad 在實務應用上無法被廣泛取代現代對稱加密演算法的主要原因為何？",
        "options": [
            "因為其 XOR 運算過於複雜，計算延遲極高",
            "因為其金鑰長度必須與明文一樣長且不可重複使用，面臨嚴峻的金鑰分配與傳輸難題",
            "因為量子電腦可在多項式時間內透過 Shor 演算法還原 OTP 金鑰",
            "因為 OTP 只能加密數字，無法加密二進位檔案"
        ],
        "answer": 1,
        "explanation": "OTP 要求金鑰長度至少等於明文長度，且每次傳輸都必須消耗全新金鑰。若雙方已具備足夠安全的通道能預先傳送龐大的金鑰，則直接利用該通道傳送明文即可，失去了實用價值。",
        "pitfalls": "誤以為 OTP 會被量子演算法攻破。事實上 OTP 具有無條件資訊理論安全，即使面對無窮算力或量子電腦依然無法破譯。",
        "reference": "Introduction to Modern Cryptography, Katz & Lindell, Ch. 2, p. 34"
    },

    # Module 2
    {
        "id": "q2-1",
        "moduleId": "mod-2",
        "category": "概念辨析",
        "question": "現代計算密碼學（Computational Cryptography）將無條件保密性放寬為計算安全性，其核心基石為下列哪兩項條件？",
        "options": [
            "限制攻擊者的算力為機率多項式時間（PPT），並容許可忽略的失敗機率（Negligible Probability）",
            "限制攻擊者不能取得密文，且金鑰必須每年更換",
            "將對稱密鑰演算法替換為公鑰加密，並使用 2048 位元模數",
            "禁止攻擊者使用量子電腦，且明文必須先進行壓縮"
        ],
        "answer": 0,
        "explanation": "計算安全性建立在兩項務實放寬之上：(1) 攻擊者僅具備有限的多項式時間算力（PPT）；(2) 系統允許攻擊者成功的機率小於任何多項式的倒數（即可忽略函數 negl(n)）。",
        "pitfalls": "混淆「公鑰加密」與「計算安全性基石」的定義，計算安全性適用於對稱與非對稱所有現代體系。",
        "reference": "1.2 The Provable Security Mindset.pdf, p. 48-52"
    },
    {
        "id": "q2-2",
        "moduleId": "mod-2",
        "category": "數學演算",
        "question": "下列哪一個數學函數 $\\mu(n)$ 符合現代密碼學中「可忽略函數（Negligible Function）」的定義？",
        "options": [
            "$\\mu(n) = \\frac{1}{n^5}$",
            "$\\mu(n) = \\frac{1}{\\log_2 n}$",
            "$\\mu(n) = 2^{-n}$",
            "$\\mu(n) = \\frac{1}{1000n}$"
        ],
        "answer": 2,
        "explanation": "根據定義，可忽略函數必須對任意正整數 $c$，最終滿足 $\\mu(n) < 1/n^c$。指數衰減函數 $2^{-n}$ 比任何多項式倒數 $1/n^c$ 衰減得更快，屬於可忽略函數；而 $1/n^5$、$1/\\log n$ 和 $1/(1000n)$ 都是多項式或次多項式等級，並非可忽略函數。",
        "pitfalls": "誤認為分母有 $n^5$ 很大就是可忽略，忽略了定義要求對『任意 $c$』皆須成立。",
        "reference": "1.2 The Provable Security Mindset.pdf, p. 55"
    },
    {
        "id": "q2-3",
        "moduleId": "mod-2",
        "category": "攻擊推導",
        "question": "若發送方使用相同的 One-Time Pad 金鑰 $k$ 連續加密兩條不同的明文 $m_1$ 與 $m_2$，攻擊者取得 $c_1 = m_1 \\oplus k$ 與 $c_2 = m_2 \\oplus k$。攻擊者將 $c_1 \\oplus c_2$ 計算後會得到何種結果？",
        "options": [
            "得到全新的隨機密文，完全無法分析",
            "得到 $m_1 \\oplus m_2$，金鑰 $k$ 被完全抵消，可藉由語言特徵與 Crib Dragging 還原明文",
            "得到金鑰 $k$ 的平方數值",
            "得到 $m_1$ 與 $m_2$ 的位元總長度"
        ],
        "answer": 1,
        "explanation": "根據 XOR 運算的結合律與反身律：$c_1 \\oplus c_2 = (m_1 \\oplus k) \\oplus (m_2 \\oplus k) = m_1 \\oplus m_2 \\oplus (k \\oplus k) = m_1 \\oplus m_2$。金鑰完全被消去，攻擊者直接掌握兩篇明文的互斥或，此即為著名的 Two-Time Pad 漏洞。",
        "pitfalls": "誤以為金鑰仍然留在密文 XOR 結果中保護資料。",
        "reference": "1.2 The Provable Security Mindset.pdf, p. 28-30"
    },
    {
        "id": "q2-4",
        "moduleId": "mod-2",
        "category": "概念辨析",
        "question": "One-Time Pad 具有延展性（Malleability），這代表中間人攻擊者在不曉得金鑰 $k$ 的情況下，可以做到以下何種攻擊？",
        "options": [
            "逆向計算出金鑰 $k$ 的所有位元",
            "對密文翻轉特定位元 $\\Delta$（$c' = c \\oplus \\Delta$），使得解密後的明文精確變更為 $m' = m \\oplus \\Delta$",
            "讓解密演算法進入無窮迴圈而當機",
            "將密文解密為完全不同的長度"
        ],
        "answer": 1,
        "explanation": "解密過程為 $m' = c' \\oplus k = (c \\oplus \\Delta) \\oplus k = (c \\oplus k) \\oplus \\Delta = m \\oplus \\Delta$。攻擊者能精確操控明文特定位元的翻轉（Bit-flipping Attack），例如將匯款金額從 $100 改為 $900，證明了純 OTP 完全不具備完整性防護。",
        "pitfalls": "將延展性誤認為能直接還原金鑰。",
        "reference": "1.2 The Provable Security Mindset.pdf, p. 31"
    },

    # Module 3
    {
        "id": "q3-1",
        "moduleId": "mod-3",
        "category": "概念辨析",
        "question": "在偽隨機生成器（PRG）的安全性定義中，區分器 $\\mathcal{D}$ 的優勢度（Advantage）通常表示為何？",
        "options": [
            "$\\mathbf{Adv} = P[\\mathcal{D}(G(s)) = 1] + P[\\mathcal{D}(r) = 1]$",
            "$\\mathbf{Adv} = |P[\\mathcal{D}(G(s)) = 1] - P[\\mathcal{D}(r) = 1]|$",
            "$\\mathbf{Adv} = P[\\mathcal{D}(G(s)) = 0] \\times P[\\mathcal{D}(r) = 1]$",
            "$\\mathbf{Adv} = \\frac{P[\\mathcal{D}(G(s)) = 1]}{P[\\mathcal{D}(r) = 1]}$"
        ],
        "answer": 1,
        "explanation": "區分器的任務是區別輸入字串來自 PRG 偽隨機場 $G(s)$ 還是真隨機場 $r$。其優勢度即為將偽隨機判定為 1 的機率與將真隨機判定為 1 的機率之絕對差值 $|P[\\mathcal{D}(G(s)) = 1] - P[\\mathcal{D}(r) = 1]|$。PRG 安全要求此優勢度必須為可忽略函數 $\\mathrm{negl}(n)$。",
        "pitfalls": "混淆加法、相除或乘法關係，優勢度是機率差的絕對值。",
        "reference": "1.4 Pseudorandomness.pdf, p. 8-10"
    },
    {
        "id": "q3-2",
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
        "explanation": "GGM 建構法利用將 $n$ 位元種子擴展為 $2n$ 位元的 PRG，將輸出切為左半部 $G_0$ 與右半部 $G_1$，以輸入的 $n$ 位元作為樹狀尋訪路徑，遞迴 $n$ 層構建出長度為 $n$ 的偽隨機函數 $F_k(x)$，證明了 PRG 可建構出 PRF。",
        "pitfalls": "誤記為 CTR 模式（CTR 是 PRF 轉 PRG）或 Feistel（PRF 轉 PRP）。",
        "reference": "1.4 Pseudorandomness.pdf, p. 25-28"
    },
    {
        "id": "q3-3",
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
        "explanation": "Luby-Rackoff 定理指出：(1) 1 輪與 2 輪不安全；(2) 3 輪可達到抗選擇明文攻擊的偽隨機置換（PRP）；(3) 4 輪則可抵抗同時具有正向加密與反向解密預言機查詢的攻擊者，達成強偽隨機置換（Strong PRP）。",
        "pitfalls": "誤選 3 輪。注意 3 輪只滿足 PRP，要達到 Strong PRP 必須為 4 輪。",
        "reference": "1.4 Pseudorandomness.pdf, p. 45-50"
    },
    {
        "id": "q3-4",
        "moduleId": "mod-3",
        "category": "原語辨析",
        "question": "偽隨機函數（PRF）與偽隨機置換（PRP）之間最關鍵的結構差異為何？",
        "options": [
            "PRF 必須是非對稱的，而 PRP 必須是對稱的",
            "PRP 本質上是一個雙射函數（一對一且映成），且解密方向也是高效率可逆的置換；而 PRF 僅為一般函數，通常不可逆",
            "PRF 只能輸入單一位元，而 PRP 可以輸入任意長度位元",
            "PRF 需要金鑰，而 PRP 不需要金鑰"
        ],
        "answer": 1,
        "explanation": "置換（Permutation）在數學上是一對一且映成的雙射（Bijection），因此 PRP 具有唯一的反函數 $P_k^{-1}$，是分組密碼的抽象模型；而 PRF 僅保證輸入到輸出的對應無法與隨機函數區分，可能存在碰撞，且通常不具備高效率的逆向求解演算法。",
        "pitfalls": "誤以為 PRF 與 PRP 都能高效率逆向解密。",
        "reference": "1.4 Pseudorandomness.pdf, p. 33-35"
    },

    # Module 4
    {
        "id": "q4-1",
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
        "explanation": "在 IND-CPA 遊戲中，攻擊者擁有加密預言機。若演算法為確定性，同一明文每次產生的密文必然相同。攻擊者只要預先查詢 $m_0$ 得 $c_0$，若挑戰密文 $c^* = c_0$ 則猜 $b=0$，否則猜 $b=1$，獲勝機率恆為 1，優勢度為 1/2。因此 IND-CPA 安全加密必須引入隨機性（如隨機 IV 或 Nonce）。",
        "pitfalls": "誤以為是算力不足或金鑰長度問題，這純粹是確定性映射導致的結構性安全缺陷。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 5-7"
    },
    {
        "id": "q4-2",
        "moduleId": "mod-4",
        "category": "攻擊推導",
        "question": "在 CBC 模式的 Padding Oracle 攻擊中，攻擊者修改前一密文區塊 $C_1$ 得到 $C'_1$，並發送給伺服器解密。當伺服器回傳「Padding Valid」且目標填充為單一位元組 `0x01` 時，中間值 $I_2[15]$ 與構造值 $C'_1[15]$ 滿足何種數學關係？",
        "options": [
            "$I_2[15] = C'_1[15] \\oplus 0x01$",
            "$I_2[15] = C'_1[15] + 0x01$",
            "$I_2[15] = C_1[15] \\oplus C'_1[15]$",
            "$I_2[15] = 0x01$"
        ],
        "answer": 0,
        "explanation": "CBC 解密時最後一位元組明文為 $P'_2[15] = I_2[15] \\oplus C'_1[15]$。若伺服器判定填充合法為 `0x01`，則代表 $P'_2[15] = 0x01$。由 $I_2[15] \\oplus C'_1[15] = 0x01$，兩邊同時 $\\oplus 0x01$ 即得 $I_2[15] = C'_1[15] \\oplus 0x01$。",
        "pitfalls": "誤將 XOR 寫為加法，或忘記中間值是由偽造的 $C'_1$ 與填充目標計算得出。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 25-32"
    },
    {
        "id": "q4-3",
        "moduleId": "mod-4",
        "category": "演算複雜度",
        "question": "使用 Padding Oracle 攻擊還原一個 16 位元組（128-bit）的 CBC 密文區塊時，攻擊者在最差情況下最多需向伺服器發送幾次解密預言機查詢？",
        "options": [
            "$2^{128}$ 次",
            "$16 \\times 256 = 4096$ 次",
            "$16^{16}$ 次",
            "$256^{16}$ 次",
        ],
        "answer": 1,
        "explanation": "該攻擊以位元組為單位獨立逐一破解。一個位元組只有 256 種可能數值（`0x00` 到 `0xFF`），因此每個位元組最多需 256 次查詢。整個 16 位元組區塊最差情況下僅需 $16 \\times 256 = 4096$ 次查詢，將指數級的密鑰窮舉降至微不足道的多項式查詢次數！",
        "pitfalls": "誤認為區塊長度會導致查詢次數呈現指數爆炸（如 $256^{16}$）。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 33"
    },
    {
        "id": "q4-4",
        "moduleId": "mod-4",
        "category": "概念辨析",
        "question": "IND-CCA1 與 IND-CCA2 最核心的威脅模型差異為何？",
        "options": [
            "IND-CCA1 攻擊者不能取得密文，而 IND-CCA2 可以",
            "IND-CCA1（非適應性）僅允許攻擊者在收到挑戰密文 $c^*$『之前』查詢解密預言機；而 IND-CCA2（適應性）在收到 $c^*$『之後』仍可查詢除 $c^*$ 以外的任意密文",
            "IND-CCA1 是針對對稱密碼，而 IND-CCA2 專門針對公鑰密碼",
            "IND-CCA1 採用量子電腦攻擊，IND-CCA2 採用經典電腦攻擊"
        ],
        "answer": 1,
        "explanation": "IND-CCA1（也稱午餐時間攻擊 Lunchtime Attack）在挑戰密文產生後立即關閉解密預言機；IND-CCA2 是完全適應性攻擊（Adaptive CCA），攻擊者收到挑戰密文 $c^*$ 後，除了不得直接查詢 $c^*$ 本身外，仍可繼續查詢任何竄改後的密文 $c \\ne c^*$，安全性要求最高。",
        "pitfalls": "混淆前後查詢權限，IND-CCA2 是在挑戰密文產生後仍能持續進行有條件查詢。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 15-18"
    },

    # Module 5
    {
        "id": "q5-1",
        "moduleId": "mod-5",
        "category": "概念辨析",
        "question": "在訊息驗證碼（MAC）的 EUF-CMA 安全模型中，攻擊者獲勝的標準是什麼？",
        "options": [
            "計算出發送方的私密金鑰 $k$",
            "成功解密出一篇未曾公開的機密訊息",
            "產出一組未曾在預言機查詢過的全新訊息 $m^*$，並給出合法的標籤 $t^*$ 使其驗證通過",
            "使驗證伺服器的 CPU 使用率達到 100%"
        ],
        "answer": 2,
        "explanation": "EUF-CMA 代表「選擇訊息攻擊下的存在不可偽造性（Existential Unforgeability under Chosen-Message Attacks）」。攻擊者只要能針對任何一條未曾查詢過的訊息 $m^*$ 鍛造出合法標籤 $t^*$，即使該訊息毫無語意價值，也算完全攻破該 MAC 系統。",
        "pitfalls": "誤以為攻擊者必須還原出金鑰 $k$ 才算獲勝。密碼學安全要求更嚴格：哪怕只偽造一則無意義訊息的標籤就算破解。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 48"
    },
    {
        "id": "q5-2",
        "moduleId": "mod-5",
        "category": "架構比較",
        "question": "在結合加密（Encryption）與訊息驗證碼（MAC）構建驗證式加密（AE）的三大範式中，哪一種在理論與實務上被證明具備通用安全性（Provably Secure under Generic Composition）？",
        "options": [
            "Encrypt-and-MAC（同時對明文進行加密與計算 MAC）",
            "MAC-then-Encrypt（先對明文計算 MAC，再將明文與 MAC 一同加密）",
            "Encrypt-then-MAC（先對明文加密得到密文，再對密文計算 MAC 標籤）",
            "MAC-only（僅傳送 MAC 標籤，不傳送密文）"
        ],
        "answer": 2,
        "explanation": "Encrypt-then-MAC（EtM）是唯一通用的安全組合範式。接收方在收到封包後，第一時間驗證密文的 MAC 標籤，若驗證失敗立即丟棄，攻擊者偽造的惡意密文完全沒有機會被解密器處理，從根本上杜絕了 Padding Oracle 等解密側信道攻擊。",
        "pitfalls": "誤以為 TLS 早期使用的 MAC-then-Encrypt 是安全的，MAC-then-Encrypt 正是導致 Lucky Thirteen 等重大漏洞的主因。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 65-72"
    },
    {
        "id": "q5-3",
        "moduleId": "mod-5",
        "category": "攻擊推導",
        "question": "基礎的 CBC-MAC 若直接應用於「可變長度訊息（Variable-length messages）」，會面臨何種致命攻擊？",
        "options": [
            "金鑰會在傳輸第 3 個區塊時自動洩漏",
            "長度延伸攻擊（Extension / Splicing Attack）：給定單區塊合法對 $(m_1, t_1)$，攻擊者可偽造雙區塊訊息 $m_1 \\,|\\, (m_2 \\oplus t_1)$ 其標籤恰好等於單區塊 $m_2$ 之標籤 $t_2$",
            "CBC 模式在解密時無法平行化",
            "會導致雜湊函數發生碰撞"
        ],
        "answer": 1,
        "explanation": "CBC-MAC 僅對固定長度訊息保證安全。若長度可變，第二區塊在加密前會與前一區塊的密文（即標籤 $t_1$）進行 XOR：$(m_2 \\oplus t_1) \\oplus t_1 = m_2$。因此輸入至分組密碼的內容與直接對 $m_2$ 計算完全相同，標籤自然等於 $t_2$，攻擊者可輕易偽造兩區塊訊息！",
        "pitfalls": "誤認為 CBC-MAC 可直接用於任意長度檔案，必須使用 CMAC 或在最後一區塊異或特殊金鑰。",
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 55-58"
    },
    {
        "id": "q5-4",
        "moduleId": "mod-5",
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
        "reference": "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf, p. 68"
    }
]

glossary_data = [
    {
        "term": "Kerckhoffs's Principle",
        "chinese": "柯克霍夫原則",
        "category": "基礎概念",
        "definition": "現代密碼學鐵律：加密系統的安全性必須完全建立在金鑰的保密性之上，演算法本身必須假設完全對外公開。",
        "pitfall": "切勿實施『隱蔽式安全（Security through Obscurity）』，私有閉門演算法往往隱藏致命設計缺陷。"
    },
    {
        "term": "Perfect Secrecy",
        "chinese": "完美保密性 / 資訊理論安全",
        "category": "資訊理論",
        "definition": "由 Shannon 提出，定義為觀察到密文前後，明文的後驗機率嚴格等於先驗機率：$P[M=m|C=c] = P[M=m]$。即使攻擊者擁有無限計算能力依然不可破解。",
        "pitfall": "達到完美保密性必須付出 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 的代價，在實務大規模儲存與傳輸中無法實現。"
    },
    {
        "term": "One-Time Pad (OTP)",
        "chinese": "單次密鑰 / 一次一密",
        "category": "對稱加密",
        "definition": "Vernam 發明的經典密碼。金鑰長度與明文相同，加密 $C = M \\oplus K$，解密 $M = C \\oplus K$。具備完美保密性，但金鑰絕對不可重複使用。",
        "pitfall": "若金鑰重複使用兩次（Two-Time Pad），$C_1 \\oplus C_2 = M_1 \\oplus M_2$ 將直接消除金鑰並外洩明文。"
    },
    {
        "term": "PPT (Probabilistic Polynomial Time)",
        "chinese": "機率多項式時間",
        "category": "複雜度理論",
        "definition": "攻擊者運算能力模型。演算法執行步數受安全參數 $n$ 的某個多項式 $O(n^c)$ 限制，且可在運算中擲隨機硬幣決定分支。",
        "pitfall": "PPT 模型排除了一切需要指數級算力（如窮舉全部 $2^{128}$ 金鑰）的非現實攻擊。"
    },
    {
        "term": "Negligible Function (negl)",
        "chinese": "可忽略函數",
        "category": "複雜度理論",
        "definition": "對於任意正多項式次數 $c > 0$，存在臨界值 $N_c$，使得當 $n > N_c$ 時，皆有 $\\mu(n) < 1/n^c$。代表在多項式時間內發生機率微乎其微。",
        "pitfall": "例如 $1/n^{10}$ 衰減很慢，不是可忽略函數；$2^{-n}$ 與 $2^{-\\sqrt{n}}$ 才是可忽略函數。"
    },
    {
        "term": "PRG (Pseudorandom Generator)",
        "chinese": "偽隨機生成器",
        "category": "密碼學原語",
        "definition": "確定性演算法，能將短隨機種子 $s \\in \\{0, 1\\}^n$ 擴展為長字串 $G(s) \\in \\{0, 1\\}^{\\ell(n)}$（$\\ell(n) > n$），且對任何 PPT 區分器而言與真隨機不可區分。",
        "pitfall": "PRG 是確定性的，並非真正隨機，但在多項式時間檢驗下具備無規律統計外觀。"
    },
    {
        "term": "PRF (Pseudorandom Function)",
        "chinese": "偽隨機函數",
        "category": "密碼學原語",
        "definition": "金鑰化函數族 $F_k: \\{0, 1\\}^n \\to \\{0, 1\\}^n$。任何 PPT 攻擊者僅能透過黑盒子黑盒查詢時，無法區分面對的是 $F_k$ 還是真正均勻隨機的函數。",
        "pitfall": "PRF 通常不要求可逆性，其輸出可能發生碰撞。"
    },
    {
        "term": "PRP (Pseudorandom Permutation)",
        "chinese": "偽隨機置換",
        "category": "密碼學原語",
        "definition": "雙射（一對一且映成）的函數族 $P_k$，正向與反向運算均可在多項式時間內完成。是分組密碼（如 AES）的理論抽象。",
        "pitfall": "若攻擊者能同時查詢逆向預言機 $P_k^{-1}$ 且無法區分，則稱為 Strong PRP。"
    },
    {
        "term": "Feistel Network",
        "chinese": "飛斯特網路",
        "category": "分組密碼結構",
        "definition": "對稱加密結構，每輪計算 $L_{i+1} = R_i$ 與 $R_{i+1} = L_i \\oplus F_{k_i}(R_i)$。優點為即使輪函數 $F$ 不可逆，整體架構天然可逆解密。",
        "pitfall": "由 Luby-Rackoff 定理：3 輪達 PRP，4 輪才可達 Strong PRP。"
    },
    {
        "term": "IND-CPA",
        "chinese": "選擇明文攻擊不可區分性",
        "category": "安全模型",
        "definition": "攻擊者擁有加密預言機 $\\mathcal{O}_{\\mathrm{Enc}}(\\cdot)$，給定自選之 $m_0, m_1$，無法以超過可忽略優勢猜出挑戰密文 $c^*$ 是由何者加密而成。",
        "pitfall": "任何確定性加密（如 ECB 模式、無隨機性的 RSA）絕對無法達到 IND-CPA 安全。"
    },
    {
        "term": "IND-CCA (IND-CCA1 / IND-CCA2)",
        "chinese": "選擇密文攻擊不可區分性",
        "category": "安全模型",
        "definition": "攻擊者擁有解密預言機。CCA1 僅限挑戰前查詢；CCA2 允許在取得挑戰密文後，繼續查詢除挑戰密文本體以外的任意密文。為對抗主動中間人攻擊的最嚴格標準。",
        "pitfall": "純 CBC 模式與串流密碼均只達到 IND-CPA，無法抵抗 IND-CCA 攻擊。"
    },
    {
        "term": "Padding Oracle Attack",
        "chinese": "填充預言機攻擊",
        "category": "密碼分析實務",
        "definition": "利用伺服器解密後回傳的 PKCS#7 填充錯誤訊息，藉由修改前一密文區塊並觀察反應，在無金鑰情況下逐位元組還原明文。",
        "pitfall": "修補錯誤回傳字串往往不夠，時間差（Timing Side-channel）依然會造成洩漏，根本解法為採用 AEAD。"
    },
    {
        "term": "MAC (Message Authentication Code)",
        "chinese": "訊息驗證碼",
        "category": "完整性原語",
        "definition": "對稱金鑰機制，用於驗證訊息之完整性與來源真實性。標準安全模型為 EUF-CMA（存在不可偽造性）。",
        "pitfall": "MAC 僅保護完整性，不提供任何機密性防護。"
    },
    {
        "term": "HMAC",
        "chinese": "基於雜湊之訊息驗證碼",
        "category": "完整性原語",
        "definition": "利用雙重雜湊架構 $H((K \\oplus \\mathrm{opad}) \\,|\\, H((K \\oplus \\mathrm{ipad}) \\,|\\, m))$ 構造 MAC，徹底免疫 Merkle-Damgård 結構之長度延伸攻擊。",
        "pitfall": "不可直接以單次雜湊 $H(K \\,|\\, m)$ 作為 MAC，會遭受長度延伸攻擊直接偽造標籤。"
    },
    {
        "term": "AE (Authenticated Encryption)",
        "chinese": "驗證式加密",
        "category": "綜合安全機制",
        "definition": "同時保障機密性與完整性的密碼機制。滿足 $\\mathrm{IND\\text{-}CPA} + \\mathrm{INT\\text{-}CTXT} \\implies \\mathrm{IND\\text{-}CCA}$。現代推薦採用 AES-GCM 或 ChaCha20-Poly1305。",
        "pitfall": "組合加密與 MAC 時，僅 Encrypt-then-MAC 具備通用證明安全，切勿採用 Encrypt-and-MAC。"
    }
]

js_content = f"""// Cryptography Review & Learning Platform Data
// Auto-generated data source for modern & post-quantum cryptography review

const MODULES_DATA = {json.dumps(modules_data, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(quiz_data, ensure_ascii=False, indent=2)};

const GLOSSARY_DATA = {json.dumps(glossary_data, ensure_ascii=False, indent=2)};
"""

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"js/data.js successfully written with {len(modules_data)} modules, {len(quiz_data)} quizzes, and {len(glossary_data)} glossary terms.")
