# -*- coding: utf-8 -*-
"""
Builder for proof_sheet.html (期中考必考形式證明精華一覽表).
Strictly bounded by exam scope: Slides up to 1.5 Section 1 (Ch. 1, 2, 4, 5, 6, 7, 8).
Excludes all out-of-scope materials (Ch. 9 CCA, AE, Padding Oracle, MAC).
"""
import json
import os
import re

print("Starting to build proof_sheet.html and js/proof_sheet_data.js...")

PROOF_SHEET_DATA = [
    {
        "id": "proof-1",
        "category": "ch1-2",
        "chapter": "Ch. 1-2",
        "title": "夏農完善保密性充分必要條件",
        "source": "課本定理 / 投影片 1.2",
        "technique": "條件機率獨立性與全機率展開",
        "target": "對所有明文 $m \\in \\mathcal{M}$ 與密文 $c \\in \\mathcal{C}$，$\\Pr[C = c \\mid M = m] = \\Pr[C = c] = \\frac{1}{|\\mathcal{C}|}$，等價於明文與密文隨機變數相互獨立。",
        "steps": [
            "1. 設方案滿足完善保密性：由定義 $\\Pr[M = m \\mid C = c] = \\Pr[M = m]$。",
            "2. 應用貝氏定理（Bayes' Theorem）：$\\Pr[M = m \\mid C = c] = \\frac{\\Pr[C = c \\mid M = m] \\cdot \\Pr[M = m]}{\\Pr[C = c]}$。",
            "3. 兩端消去 $\\Pr[M = m] > 0$，即得 $\\frac{\\Pr[C = c \\mid M = m]}{\\Pr[C = c]} = 1$，故 $\\Pr[C = c \\mid M = m] = \\Pr[C = c]$。",
            "4. 因密文分佈與明文無關，對所有明文 $m_0, m_1$ 恆有 $\\Pr[C = c \\mid M = m_0] = \\Pr[C = c \\mid M = m_1]$。"
        ],
        "algorithm": "判定準則：檢驗對任意明文 $m$，方程式 $\\text{Enc}(K, m) = c$ 在金鑰空間 $\\mathcal{K}$ 中的解個數是否恆定相等（$|\\{k \\in \\mathcal{K} : \\text{Enc}(k, m) = c\\}| = \\text{const}$）。",
        "pitfall": "很多考生誤以為金鑰長度足夠即保密。金鑰長度足夠僅為必要條件，必須證明條件機率分佈嚴格相等且解的個數均勻。"
    },
    {
        "id": "proof-2",
        "category": "ch1-2",
        "chapter": "Ch. 2",
        "title": "夏農金鑰長度下界定理反證法",
        "source": "課本 Theorem 2.10 / 練習一 29 (Ex 2.14)",
        "technique": "嚴格反證法（Proof by Contradiction）與鴿籠原理",
        "target": "任何具備正確性（Correctness）且達成完善保密性（Perfect Secrecy）的加密方案，其金鑰空間大小必滿足 $|\\mathcal{K}| \\ge |\\mathcal{M}|$。",
        "steps": [
            "1. 假設相反：假設方案具備完善保密性且正確，但 $|\\mathcal{K}| < |\\mathcal{M}|$。",
            "2. 任取一具正出現機率之密文 $c \\in \\mathcal{C}$（即 $\\Pr[C = c] > 0$）。",
            "3. 定義密文 $c$ 在所有可能金鑰下的可能解密明文集合：$S(c) = \\{\\text{Dec}(k, c) \\mid k \\in \\mathcal{K}\\}$。",
            "4. 因 $\\text{Dec}$ 為確定性函數，解密集合元素數受限於金鑰數：$|S(c)| \\le |\\mathcal{K}|$。由假設 $|\\mathcal{K}| < |\\mathcal{M}|$，得 $|S(c)| < |\\mathcal{M}|$。",
            "5. 由鴿籠原理，明文空間中必存在至少一筆明文 $m^* \\in \\mathcal{M}$ 滿足 $m^* \\notin S(c)$。",
            "6. 根據正確性，若明文原為 $m^*$，則不可能存在任何金鑰 $k \\in \\mathcal{K}$ 使得 $\\text{Enc}(k, m^*) = c$（否則 $\\text{Dec}(k, c) = m^* \\in S(c)$ 產生矛盾）。",
            "7. 因此，$\\Pr[C = c \\mid M = m^*] = 0$。然而由 $c$ 的選取知 $\\Pr[C = c] > 0$。這導致 $\\Pr[C = c \\mid M = m^*] \\neq \\Pr[C = c]$，違反完善保密性，矛盾！故假設不成立，必定有 $|\\mathcal{K}| \\ge |\\mathcal{M}|$。"
        ],
        "algorithm": "反例構造法：只要找到密文 $c$，使其可能解密的明文種類數小於明文總數，挑選無法解出的 $m^*$ 即可直接證偽完善保密性。",
        "pitfall": "證明必須明確定義集合 $S(c)$ 並點出 $\\text{Dec}$ 函數確定性造成的基數不等式 $|S(c)| \\le |\\mathcal{K}|$。"
    },
    {
        "id": "proof-3",
        "category": "ch1-2",
        "chapter": "Ch. 1-2",
        "title": "OTP 挑戰者博弈不可區分性推導",
        "source": "課本 Lemma 2.3 / 練習一 15",
        "technique": "全機率展開與對稱性消去",
        "target": "在 IND-OTS 挑戰者博弈中，對任意攻擊者 $\\mathcal{A}$，猜中隨機位元 $b$ 之機率恆滿足 $\\Pr[b' = b] = \\frac{1}{2}$。",
        "steps": [
            "1. 攻擊者選擇兩筆等長明文 $M_0, M_1$。挑戰者均勻隨機抽取 $b \\leftarrow \\{0, 1\\}$ 與金鑰 $K \\leftarrow \\{0, 1\\}^n$。",
            "2. 挑戰密文為 $C = K \\oplus M_b$。因 $K$ 為均勻隨機字串，對任意給定明文 $M_b$，密文 $C$ 的分佈滿足 $\\Pr[C = c \\mid b = 0] = \\Pr[K = c \\oplus M_0] = 2^{-n}$，且 $\\Pr[C = c \\mid b = 1] = \\Pr[K = c \\oplus M_1] = 2^{-n}$。",
            "3. 攻擊者輸出 $b' = \\mathcal{A}(C)$。計算全機率：$\\Pr[b'=1 \\mid b=0] = \\sum_{c} \\Pr[\\mathcal{A}(c)=1] \\Pr[C=c \\mid b=0] = 2^{-n} \\sum_c \\Pr[\\mathcal{A}(c)=1]$。",
            "4. 同理，$\\Pr[b'=1 \\mid b=1] = \\sum_{c} \\Pr[\\mathcal{A}(c)=1] \\Pr[C=c \\mid b=1] = 2^{-n} \\sum_c \\Pr[\\mathcal{A}(c)=1]$。",
            "5. 兩條件機率完全相等，故優勢 $\\mathbf{Adv} = |\\Pr[b'=1 \\mid b=1] - \\Pr[b'=1 \\mid b=0]| = 0$。勝率 $\\Pr[b'=b] = \\frac{1}{2} + \\frac{1}{2}\\mathbf{Adv} = \\frac{1}{2}$。"
        ],
        "algorithm": "不可區分性結論：任何演算法在 OTP 密文上的輸出行為獨立於挑戰明文之選擇。",
        "pitfall": "證明中切勿只寫「因為 XOR 很安全」；必須明確寫出條件機率與全機率求和式。"
    },
    {
        "id": "proof-4",
        "category": "ch1-2",
        "chapter": "Ch. 1-2",
        "title": "模 10 加法 OTP 完善保密性形式證明",
        "source": "作業一 1(b)",
        "technique": "阿貝爾群同構與唯一加法反元素",
        "target": "在十進位數字 $\\{0, \\dots, 9\\}$ 上，$\\text{Enc}(K, M) = (K + M) \\bmod 10$ 具備正確性與完善保密性。",
        "steps": [
            "1. 正確性：對任意 $K, M \\in \\{0, \\dots, 9\\}$，$\\text{Dec}(K, \\text{Enc}(K, M)) = (((K + M) \\bmod 10) - K) \\bmod 10 \\equiv K + M - K \\equiv M \\pmod{10}$。因 $M \\in \\{0, \\dots, 9\\}$，結果精確還原為 $M$。",
            "2. 完善保密性：設金鑰 $K$ 均勻選自 $\\{0, \\dots, 9\\}$，則 $\\Pr[K = k] = \\frac{1}{10}$。",
            "3. 對任意固定明文 $m$ 與密文 $c$，$\\Pr[C = c \\mid M = m] = \\Pr[(K + m) \\bmod 10 = c]$。",
            "4. 在加法群 $(\\mathbb{Z}_{10}, +)$ 中，元素 $m$ 具備唯一加法反元素 $-m$。方程式 $K + m \\equiv c \\pmod{10}$ 存在唯一整數解 $K = (c - m) \\bmod 10 \\in \\{0, \\dots, 9\\}$。",
            "5. 故條件機率 $\\Pr[C = c \\mid M = m] = \\Pr[K = (c - m) \\bmod 10] = \\frac{1}{10}$，對所有明文 $m$ 恆定，達成完善保密性。"
        ],
        "algorithm": "關鍵代數條件：群 $(\\mathbb{Z}_N, +)$ 的加法位移映射 $x \\mapsto x + k$ 為雙射置換，均勻分佈經雙射映射後依然保持均勻分佈。",
        "pitfall": "須強調 $\\mathbb{Z}_{10}$ 中反元素唯一性，保證每個密文對應恰好一把金鑰。"
    },
    {
        "id": "proof-5",
        "category": "ch1-2",
        "chapter": "Ch. 1",
        "title": "模 n 乘法 OTP 之質數條件證明",
        "source": "課本 Exercise 1.15 / 練習一 27",
        "technique": "有限環乘法單位群與歐拉函數 $\\phi(n)$",
        "target": "在 $\\{1, \\dots, n-1\\}$ 上以模 $n$ 乘法加密 $\\text{Enc}(K, M) = (K \\cdot M) \\bmod n$，密文均勻分佈若且唯若 $n$ 為質數。",
        "steps": [
            "1. 正向（$n$ 為質數）：當 $n$ 為質數時，集合 $\\mathbb{Z}_n^* = \\{1, \\dots, n-1\\}$ 在模 $n$ 乘法下構成階數為 $n-1$ 的循環群。",
            "2. 對任意明文 $m \\in \\mathbb{Z}_n^*$，其乘法反元素 $m^{-1} \\pmod n$ 存在且唯一。同餘方程 $K \\cdot m \\equiv c \\pmod n$ 存在唯一解 $K = c \\cdot m^{-1} \\pmod n$。",
            "3. 當 $K$ 均勻取樣自 $\\{1, \\dots, n-1\\}$ 時，$\\Pr[C = c \\mid M = m] = \\frac{1}{n-1}$，密文分佈嚴格均勻。",
            "4. 反向（$n$ 為合數）：若 $n$ 為合數，必存在非平凡因子 $p \\mid n$ 滿足 $1 < p < n$。取明文 $m = p$。",
            "5. 對任意 $K \\in \\{1, \\dots, n-1\\}$，乘積 $(K \\cdot p) \\bmod n$ 恆為 $\\gcd(p, n) = p$ 之倍數，絕不可能取到任何與 $n$ 互質的數。",
            "6. 密文取值空間退化，至少有一個密文 $c^*$（如 $c^* = 1$）滿足 $\\Pr[C = 1 \\mid M = p] = 0 \\neq \\frac{1}{n-1}$，密文絕非均勻分佈。"
        ],
        "algorithm": "合數破譯法：選 $M_0 = p$（因子）與 $M_1 = 1$。若密文為 $p$ 的倍數則判定明文為 $M_0$。",
        "pitfall": "必須涵蓋合數存在零因數（Zero Divisors）導致映射非滿射的代數論證。"
    },
    {
        "id": "proof-6",
        "category": "ch1-2",
        "chapter": "Ch. 2",
        "title": "模 10 乘法加密不具單次保密性證明",
        "source": "課本 Exercise 2.13 / 練習一 28",
        "technique": "合數環零因子反例法",
        "target": "金鑰與明文取自 $\\{1, \\dots, 9\\}$，加密函數為 $\\text{Enc}(K, M) = (K \\cdot M) \\bmod 10$，該方案不具備單次保密性。",
        "steps": [
            "1. 構造反例明文對：挑選 $M_0 = 5$ 與 $M_1 = 1$。",
            "2. 分析 $M_0 = 5$ 之密文分佈：對任意金鑰 $K \\in \\{1, \\dots, 9\\}$，計算 $(K \\cdot 5) \\bmod 10$：若 $K$ 為奇數則結果為 5；若 $K$ 為偶數則結果為 0。",
            "3. 因密文空間定義為 $\\{1, \\dots, 9\\}$，即便考慮輸出非 0，密文亦僅能為 5。故 $\\Pr[C = 1 \\mid M = 5] = 0$。",
            "4. 分析 $M_1 = 1$ 之密文分佈：$C = (K \\cdot 1) \\bmod 10 = K$。當 $K$ 均勻選取時，$\\Pr[C = 1 \\mid M = 1] = \\Pr[K = 1] = \\frac{1}{9} > 0$。",
            "5. 因 $\\Pr[C = 1 \\mid M = 5] = 0 \\neq \\Pr[C = 1 \\mid M = 1] = \\frac{1}{9}$，密文條件機率不相等，違反完善保密性。"
        ],
        "algorithm": "區分者演算法：提交 $M_0 = 5, M_1 = 1$。若收到之挑戰密文 $C \\in \\{0, 5\\}$ 輸出 0；若收到 $C \\in \\{1, 2, 3, 4, 6, 7, 8, 9\\}$ 輸出 1。區分勝率達 $1$。",
        "pitfall": "考試切勿只寫「因為 10 是合數」；必須具體列出兩個明文與特定密文的機率不相等式。"
    },
    {
        "id": "proof-7",
        "category": "ch1-2",
        "chapter": "Ch. 1-2",
        "title": "AND 運算型 OTP 正確性與保密性破壞反例",
        "source": "作業一 1(a)",
        "technique": "非單射映射（Non-injective Mapping）證明",
        "target": "方案 $\\text{Enc}(K, M) = K \\wedge M$ 既不具備正確性，亦不具備完善保密性。",
        "steps": [
            "1. 正確性破壞：正確性要求存在 $\\text{Dec}$ 使得 $\\text{Dec}(K, \\text{Enc}(K, M)) = M$ 恆成立。當金鑰 $K = 0$ 時，$\\text{Enc}(0, 0) = 0 \\wedge 0 = 0$ 且 $\\text{Enc}(0, 1) = 0 \\wedge 1 = 0$。給定金鑰 $K=0$ 與密文 $C=0$，解密函數無法還原明文是 0 還是 1，映射非單射，故不具備正確性。",
            "2. 完善保密性破壞：設 $K \\leftarrow \\{0, 1\\}$ 均勻隨機。取明文 $M_0 = 0, M_1 = 1$。",
            "3. 當 $M = 0$ 時，密文 $C = K \\wedge 0 = 0$ 恆成立，故 $\\Pr[C = 1 \\mid M = 0] = 0$。",
            "4. 當 $M = 1$ 時，密文 $C = K \\wedge 1 = K$，故 $\\Pr[C = 1 \\mid M = 1] = \\Pr[K = 1] = \\frac{1}{2}$。",
            "5. $\\Pr[C = 1 \\mid M = 0] \\neq \\Pr[C = 1 \\mid M = 1]$，條件分佈依賴明文，違反完善保密性。"
        ],
        "algorithm": "資訊洩漏機制：一旦觀察到密文 $C = 1$，攻擊者百分之百確定明文必定為 1（因為若明文為 0 絕不可能輸出 1）。",
        "pitfall": "不可僅口語回答「AND 不可逆」；需寫出 $K=0$ 時兩個相異明文映射到同一個密文的反例。"
    },
    {
        "id": "proof-8",
        "category": "ch1-2",
        "chapter": "Ch. 1-2",
        "title": "金鑰減半 Two-Time Pad 差分消除破壞定理",
        "source": "作業一 1(c) / 練習一 16",
        "technique": "線性 XOR 差分消除與區分者建構",
        "target": "若 $\\text{Enc}(K, (M_1, M_2)) = (K \\oplus M_1, K \\oplus M_2)$ 且 $|K| = |M_1| = |M_2|$，此方案機密性徹底崩潰。",
        "steps": [
            "1. 密文由兩部分組成：$C_1 = K \\oplus M_1$ 與 $C_2 = K \\oplus M_2$。",
            "2. 攻擊者計算兩密文區塊之 XOR 和：$C_1 \\oplus C_2 = (K \\oplus M_1) \\oplus (K \\oplus M_2) = (K \\oplus K) \\oplus (M_1 \\oplus M_2) = M_1 \\oplus M_2$。",
            "3. 金鑰 $K$ 徹底抵消，攻擊者無條件獲得兩段明文的精確位元差分 $M_1 \\oplus M_2$。",
            "4. 若兩段明文相同（$M_1 = M_2$），則密文恆滿足 $C_1 \\oplus C_2 = 0^n$；若 $M_1$ 為已知協定標頭，則 $M_2 = (C_1 \\oplus C_2) \\oplus M_1$ 完全洩漏。"
        ],
        "algorithm": "區分者演算法 $D$：提交 $M^{(0)} = (0^n, 0^n)$ 與 $M^{(1)} = (0^n, 1^n)$。取得挑戰密文 $(C_1^*, C_2^*)$。若 $C_1^* \\oplus C_2^* == 0^n$ 輸出 0；否則輸出 1。區分優勢達 $\\mathbf{Adv} = 1$。",
        "pitfall": "必須明確說明：攻擊者不僅能判定明文是否重複，亦能透過已知明文（Crib Dragging）推導其餘內容。"
    },
    {
        "id": "proof-9",
        "category": "ch1-2",
        "chapter": "Ch. 2",
        "title": "函式庫等價性 L1 ≡ L2 分支恆等證明",
        "source": "作業一 2(a)",
        "technique": "分支等價性分析（Branch Equivalence）與隨機變數代換",
        "target": "證明 $\\mathcal{L}_1 \\equiv \\mathcal{L}_2$，其中 $\\mathcal{L}_1: \\text{query}(M) \\to K \\oplus M$；$\\mathcal{L}_2: \\text{query}(M) \\to [\\text{if } M=R_1 \\text{ return } R_2 \\text{ else } M \\oplus R_1 \\oplus R_2]$。",
        "steps": [
            "1. 分析 $\\mathcal{L}_2$ 之條件分支：當 $M = R_1$ 成立時，若代入 else 分支之表達式，計算結果為：$M \\oplus R_1 \\oplus R_2 = R_1 \\oplus R_1 \\oplus R_2 = 0^n \\oplus R_2 = R_2$。",
            "2. 計算結果與 if 條件分支的直接回傳值 $R_2$ 完全恆等！",
            "3. 因此，$\\mathcal{L}_2$ 的 if-else 條件判斷式在語義上為多餘無效程式碼。無論輸入 $M$ 為何，其輸出恆等於 $M \\oplus (R_1 \\oplus R_2)$。",
            "4. 令 $K' = R_1 \\oplus R_2$。因 $R_1, R_2$ 為獨立均勻隨機字串，根據 OTP 隨機性引理，$K'$ 在 $\\{0, 1\\}^n$ 上嚴格均勻分佈。",
            "5. 故 $\\mathcal{L}_2$ 之行為等價於每次隨機抽樣 $K' \\leftarrow \\{0, 1\\}^n$ 並回傳 $M \\oplus K'$，其聯合分佈與 $\\mathcal{L}_1$ 完全相同，$\\mathcal{L}_1 \\equiv \\mathcal{L}_2$。"
        ],
        "algorithm": "結論：兩函式庫在所有多項式時間程式下的回傳分佈恆等，無任何區分者能以大於 0 之優勢區分它們。",
        "pitfall": "切勿嘗試構造區分者；需先證明分支在代數上的恆等性，再引用隨機變數 XOR 的均勻分佈保持性。"
    },
    {
        "id": "proof-10",
        "category": "ch1-2",
        "chapter": "Ch. 2",
        "title": "加解密狀態一致性約束區分者建構",
        "source": "作業一 2(b)",
        "technique": "密碼系統跨查詢狀態一致性檢驗",
        "target": "證明 $\\mathcal{L}_C \\not\\equiv \\mathcal{L}_D$，其中 $\\mathcal{L}_C$ 為共用金鑰之加解密庫，$\\mathcal{L}_D$ 為獨立隨機回傳之加解密庫。",
        "steps": [
            "1. 在 $\\mathcal{L}_C$ 中，$\\text{enc}(M)$ 產生 $C = K \\oplus M$；當將 $C$ 送入 $\\text{dec}(C)$ 時，回傳 $K \\oplus C = K \\oplus (K \\oplus M) = M$ 恆成立（維持狀態一致性）。",
            "2. 在 $\\mathcal{L}_D$ 中，$\\text{enc}(M)$ 回傳獨立隨機字串 $C \\leftarrow \\{0, 1\\}^n$；$\\text{dec}(C)$ 亦回傳獨立隨機字串 $M' \\leftarrow \\{0, 1\\}^n$（兩次查詢無狀態綁定）。",
            "3. 構造區分者演算法 $D$：呼叫 $C := \\text{enc}(0^n)$；接著呼叫 $M' := \\text{dec}(C)$；若 $M' == 0^n$ 輸出 1；否則輸出 0。",
            "4. 優勢計算：在 $\\mathcal{L}_C$ 下，$M' = 0^n$ 機率為 1。在 $\\mathcal{L}_D$ 下，$M'$ 為獨立隨機抽取，$M' = 0^n$ 機率為 $2^{-n}$。優勢 $\\mathbf{Adv} = 1 - 2^{-n} \\approx 1$。"
        ],
        "algorithm": "區分者代碼：\n1. C = enc(0^n)\n2. M = dec(C)\n3. return (M == 0^n) ? 1 : 0",
        "pitfall": "密碼系統與真隨機預言機的最核心差異即在於解密是否能還原加密之輸入（狀態一致性）。"
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
            "1. 在 $\\mathcal{L}_A$ 中，輸出 $y$ 的邊際分佈為 $\\Pr_{\\mathcal{L}_A}[Y = y] = 2^{-n}$。",
            "2. 在 $\\mathcal{L}_B$ 中，內部聯合隨機變數為 $(Y, Z)$，聯合分佈為 $\\Pr[Y = y, Z = z] = 2^{-n} \\cdot 2^{-n} = 2^{-2n}$。",
            "3. 函式庫介面僅回傳 $y$，對未回傳之內部變數 $z$ 進行邊際化（求和）：$\\Pr_{\\mathcal{L}_B}[Y = y] = \\sum_{z \\in \\{0,1\\}^n} \\Pr[Y = y, Z = z] = 2^n \\cdot 2^{-2n} = 2^{-n}$。",
            "4. 對所有輸出值 $y$，兩函式庫之機率分佈嚴格相等，故不可區分。"
        ],
        "algorithm": "密碼學基本公理：任何未經介面洩漏、且與回傳值相互獨立的內部隨機抽樣，對攻擊者的視角不產生任何統計影響。",
        "pitfall": "不可因為「多了抽樣 $z$ 的運算時間」而判定可區分；在可證明安全模型中，介面輸出之分佈等價性為唯一衡量標準。"
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
            "1. 定義中間混合庫 $\\mathcal{L}_{\\text{hyb}}$：\n   $\\mathcal{L}_{\\text{hyb}}()$: 抽樣 $Y \\leftarrow \\{0, 1\\}^n$；令 $X' := Y \\oplus 1^n$；回傳 $(X', X' \\oplus 1^n)$。",
            "2. 證明 $\\mathcal{L}_1 \\equiv \\mathcal{L}_{\\text{hyb}}$：映射 $Y \\mapsto Y \\oplus 1^n$ 是 $\\{0, 1\\}^n$ 到自身的一對一雙射（Bijective Permutation）。當 $Y$ 為均勻隨機變數時，$X' = Y \\oplus 1^n$ 亦為嚴格均勻隨機變數。因此 $(X', X' \\oplus 1^n)$ 的分佈與 $(X, X \\oplus 1^n)$ 完全相同。",
            "3. 證明 $\\mathcal{L}_{\\text{hyb}} \\equiv \\mathcal{L}_2$：在 $\\mathcal{L}_{\\text{hyb}}$ 中，第二個分量為 $X' \\oplus 1^n = (Y \\oplus 1^n) \\oplus 1^n = Y$。代入得回傳值為 $(Y \\oplus 1^n, Y)$，其程式碼與輸出形式與 $\\mathcal{L}_2$ 完全一致。",
            "4. 根據不可區分性之傳遞性（Transitivity of Equivalence）：$\\mathcal{L}_1 \\equiv \\mathcal{L}_{\\text{hyb}} \\equiv \\mathcal{L}_2$。證明完畢。"
        ],
        "algorithm": "混合論證規範：每一跳（Hop）必須明確陳述代數等價性或引理支撐，確保兩端鏈結閉環。",
        "pitfall": "必須寫出中間庫 $\\mathcal{L}_{\\text{hyb}}$ 的具體演算法，切勿直接跳步宣稱等價。"
    },
    {
        "id": "proof-13",
        "category": "ch1-2",
        "chapter": "Ch. 2",
        "title": "修改型 OTP 方案 Σ' 單次保密性證明",
        "source": "作業一 3",
        "technique": "決定性派生密文（Deterministic Derivation）分佈分析",
        "target": "構造 $\\text{Enc}'(K, M) = (C_1, C_2) = (K \\oplus M, K \\oplus M \\oplus 1^n)$，證明 $\\Sigma'$ 在單次加密下依然具備完善保密性。",
        "steps": [
            "1. 攻擊者選擇兩筆等長明文 $M^{(0)}, M^{(1)}$。挑戰者抽取 $b \\leftarrow \\{0, 1\\}$ 與均勻隨機金鑰 $K \\leftarrow \\{0, 1\\}^n$。",
            "2. 挑戰密文對為 $(C_1^*, C_2^*) = (K \\oplus M^{(b)}, K \\oplus M^{(b)} \\oplus 1^n)$。",
            "3. 分析第一分量 $C_1^*$：根據標準 OTP 完善保密性，$C_1^* = K \\oplus M^{(b)}$ 在 $\\{0, 1\\}^n$ 上為嚴格均勻分佈，對任意固定明文 $m$，$\\Pr[C_1^* = c_1 \\mid M^{(b)} = m] = 2^{-n}$。",
            "4. 分析第二分量 $C_2^*$：第二分量為第一分量的確定性雙射函數 $C_2^* = C_1^* \\oplus 1^n$，其取值完全由 $C_1^*$ 唯一確定，不包含任何額外關於明文 $M^{(b)}$ 的資訊。",
            "5. 密文對的聯合條件機率為：$\\Pr[(C_1^*, C_2^*) = (c_1, c_2) \\mid M^{(b)} = m] = \\Pr[C_1^* = c_1 \\mid M^{(b)} = m] \\cdot \\mathbb{I}_{\\{c_2 = c_1 \\oplus 1^n\\}} = 2^{-n} \\cdot \\mathbb{I}_{\\{c_2 = c_1 \\oplus 1^n\\}}$。",
            "6. 該聯合機率對 $m = M^{(0)}$ 與 $m = M^{(1)}$ 完全恆等，攻擊者區分優勢嚴格為 0，方案在單次加密下安全。"
        ],
        "algorithm": "本質剖析：雖然密文長度膨脹為兩倍，但第二部分僅是第一部分的公開位元反轉，並未引入獨立金鑰，亦未洩漏明文之內容。",
        "pitfall": "需特別標明該安全性僅限於「單次加密（IND-OTS）」；若在多筆查詢（CPA）下則因確定性而失效。"
    },
    {
        "id": "proof-14",
        "category": "ch4-5",
        "chapter": "Ch. 4",
        "title": "生日悖論雜湊碰撞樣本數數學推導",
        "source": "課本 Ch. 4 / 練習一 21",
        "technique": "Taylor 級數近似 $1 - x \\approx e^{-x}$ 與機率積分",
        "target": "在大小為 $N = 2^n$ 的均勻隨機空間中，取樣 $k$ 個元素產生碰撞之機率達到 50% 時，$k \\approx \\sqrt{2 \\ln 2} \\cdot 2^{n/2} \\approx 1.177 \\times 2^{n/2}$。",
        "steps": [
            "1. 設隨機抽取 $k$ 個樣本，計算「所有樣本皆相異（無碰撞）」之機率 $q$：$q = 1 \\cdot \\left(1 - \\frac{1}{N}\\right) \\cdot \\left(1 - \\frac{2}{N}\\right) \\cdots \\left(1 - \\frac{k-1}{N}\\right) = \\prod_{i=1}^{k-1} \\left(1 - \\frac{i}{N}\\right)$。",
            "2. 應用 Taylor 展開不等式：當 $x \\ll 1$ 時，$1 - x \\approx e^{-x}$。代入得：$q \\approx \\prod_{i=1}^{k-1} e^{-i/N} = \\exp\\left( - \\sum_{i=1}^{k-1} \\frac{i}{N} \\right) = \\exp\\left( - \\frac{k(k-1)}{2N} \\right) \\approx \\exp\\left( - \\frac{k^2}{2N} \\right)$。",
            "3. 碰撞機率為 $p = 1 - q \\approx 1 - e^{-k^2 / (2N)}$。令碰撞機率達到 50%（$p = 1/2$），得：$1 - e^{-k^2 / (2N)} = \\frac{1}{2} \\implies e^{-k^2 / (2N)} = \\frac{1}{2}$。",
            "4. 兩端取自然對數：$-\\frac{k^2}{2N} = \\ln\\left(\\frac{1}{2}\\right) = -\\ln 2 \\implies k^2 = 2N \\ln 2$。",
            "5. 開平方得：$k = \\sqrt{2 \\ln 2} \\cdot \\sqrt{N} \\approx 1.1774 \\cdot 2^{n/2}$。證明完畢。"
        ],
        "algorithm": "安全長度結論：欲抵禦 $2^{128}$ 次運算之生日攻擊，雜湊函數輸出位元數必須達到 $n \\ge 2 \\times 128 = 256$ 位元（如 SHA-256）。",
        "pitfall": "推導中必須寫出連乘積展開式以及 $1 - x \\approx e^{-x}$ 的關鍵近似步驟。"
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
            "1. 核心破綻識別：$H$ 的第二區塊 $B$（長度 $\\lambda$）直接作為第二級 PRG 運算之種子，且 $B$ 與其輸出 $C\\|D = G(B)$ 同時公開在輸出字串中。",
            "2. 構造區分者演算法 $D(W)$，輸入候選字串 $W \\in \\{0, 1\\}^{4\\lambda}$：\n   a. 將 $W$ 切割為 4 個等長區塊：$W = w_1 \\| w_2 \\| w_3 \\| w_4$，每塊長度 $\\lambda$。\n   b. 取第二區塊 $w_2$，本地執行 PRG 運算：$Y := G(w_2) \\in \\{0, 1\\}^{2\\lambda}$。\n   c. 檢驗後半部是否吻合：若 $Y == (w_3 \\| w_4)$ 輸出 1；否則輸出 0。",
            "3. 真實 PRG 分佈下（$W = H(S)$）：根據定義 $C\\|D = G(B)$，故 $G(w_2) == w_3 \\| w_4$ 恆成立，$\\Pr[D(H(S)) = 1] = 1$。",
            "4. 真隨機字串分佈下（$W \\leftarrow \\{0, 1\\}^{4\\lambda}$）：$w_2, w_3, w_4$ 為獨立均勻隨機抽取，固定 $w_2$ 後 $G(w_2)$ 為固定值，與隨機字串 $w_3 \\| w_4$ 恰好相等的機率為 $2^{-2\\lambda}$，$\\Pr[D(U_{4\\lambda}) = 1] = 2^{-2\\lambda}$。",
            "5. 區分優勢計算：$\\mathbf{Adv}_H(D) = |\\Pr[D(H(S))=1] - \\Pr[D(U)=1]| = 1 - 2^{-2\\lambda}$。優勢不可忽略（接近 1），故 $H$ 絕非安全 PRG。"
        ],
        "algorithm": "區分者偽代碼：\n1. parse W as w1 || w2 || w3 || w4\n2. if G(w2) == (w3 || w4) return 1\n3. else return 0",
        "pitfall": "不可僅指出「因為 $B$ 洩漏了」；必須完整寫出區分者演算法 $D$ 的步驟並精確計算優勢差值。"
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
            "1. 構造 A（標準串流展開，Claim 5.7）：每輪計算 $s_i \\| t_i := G(s_{i-1})$，輸出 $t_1 \\| t_2 \\| \\dots \\| t_n$ 並將最終狀態 $s_n$ 隱藏。\n   證明：利用 Hybrid Argument，建立 $n+1$ 個混合函式庫 $H_0, \\dots, H_n$。在 $H_i$ 中前 $i$ 輪狀態替換為真隨機字串。由 $G$ 之 PRG 安全性保證相鄰混合庫不可區分，歸納證明整體優勢 $\\mathbf{Adv} \\le n \\cdot \\mathbf{Adv}_G$，判定為安全 PRG。",
            "2. 構造 B（反饋狀態洩漏）：若構造在輸出中暴露中間狀態種子 $s_i$（如輸出 $s_1 \\| t_1 \\| s_2 \\| t_2$），攻擊者直接取 $s_1$ 本地計算 $G(s_1)$ 並比對後續位元，區分優勢達 $1 - 2^{-\\lambda}$，判定為不安全。"
        ],
        "algorithm": "核心準則：密碼學 PRG 迭代之黃金鐵律在於「內部狀態轉移必須絕對黑箱保密，僅能公開非線性萃取之輸出位元」。",
        "pitfall": "答題時須先明確指出題目所提構造究竟有無隱藏中間狀態，分情況討論證明或給出攻擊。"
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
            "1. 核心破綻識別：對任意兩筆輸入 $X_1, X_2$，計算其輸出之 XOR 差分：$F(K, X_1) \\oplus F(K, X_2) = (G(K) \\oplus X_1) \\oplus (G(K) \\oplus X_2) = X_1 \\oplus X_2$。金鑰遮罩 $G(K)$ 徹底抵消，輸出差分恆等於輸入差分！",
            "2. 構造多項式時間區分者演算法 $D^{\\mathcal{O}}$：\n   a. 查詢 Oracle 輸入 $X_1 = 0^n$，取得輸出 $Y_1 := \\mathcal{O}(0^n)$。\n   b. 查詢 Oracle 輸入 $X_2 = 1^n$，取得輸出 $Y_2 := \\mathcal{O}(1^n)$。\n   c. 檢驗差分關係：若 $Y_1 \\oplus Y_2 == 1^n$ 輸出 1（判定為真實 PRF $F$）；否則輸出 0（判定為真隨機函數 $\\mathcal{R}$）。",
            "3. 真實 PRF 下（$\\mathcal{O} = F_K$）：$Y_1 \\oplus Y_2 = (G(K) \\oplus 0^n) \\oplus (G(K) \\oplus 1^n) = 1^n$ 恆成立，$\\Pr[D^{F_K} = 1] = 1$。",
            "4. 真隨機函數下（$\\mathcal{O} = \\mathcal{R}$）：$Y_1, Y_2$ 為獨立均勻隨機抽取，兩者 XOR 等於固定值 $1^n$ 的機率為 $2^{-n}$，$\\Pr[D^{\\mathcal{R}} = 1] = 2^{-n}$。",
            "5. 區分優勢計算：$\\mathbf{Adv}_F(D) = |1 - 2^{-n}| \\approx 1$。優勢極大，證明 $F$ 不是安全 PRF。"
        ],
        "algorithm": "區分者代碼：\n1. Y1 = Oracle(0^n)\n2. Y2 = Oracle(1^n)\n3. return (Y1 ^ Y2 == 1^n) ? 1 : 0",
        "pitfall": "切勿誤認「因為 $G(K)$ 是隨機字串，所以加了 $X$ 依然隨機」。PRF 考核的是多次查詢之間的函數映射結構，而非單次輸出的隨機性。"
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
            "1. 核心破綻識別：檢視全零輸入 $X = 0^n$ 時函數之取值：$H(K, 0^n) = F(K, 0^n) \\oplus F(K, 0^n) = 0^m$。無論金鑰 $K$ 為何，輸入 $0^n$ 時輸出恆為固定值 $0^m$！",
            "2. 構造區分者演算法 $D^{\\mathcal{O}}$：\n   a. 僅需向 Oracle 進行 1 次查詢：輸入 $X = 0^n$，獲得回傳值 $Y := \\mathcal{O}(0^n)$。\n   b. 判定：若 $Y == 0^m$ 輸出 1；否則輸出 0。",
            "3. 真實構造下（$\\mathcal{O} = H_K$）：$\\Pr[D^{H_K} = 1] = \\Pr[0^m == 0^m] = 1$。",
            "4. 真隨機函數下（$\\mathcal{O} = \\mathcal{R}$）：隨機函數在 $0^n$ 處之取值為均勻隨機抽取，命中全零字串的機率為 $2^{-m}$，$\\Pr[D^{\\mathcal{R}} = 1] = 2^{-m}$。",
            "5. 區分優勢計算：$\\mathbf{Adv}_H(D) = 1 - 2^{-m}$。單次查詢即可徹底攻破。"
        ],
        "algorithm": "區分者偽代碼：\n1. Y = Oracle(0^n)\n2. return (Y == 0^m) ? 1 : 0",
        "pitfall": "只需 1 次查詢即可打破，優勢計算為 $1 - 2^{-m}$。"
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
            "1. 考慮真隨機函數 $\\text{Func}: \\{0,1\\}^n \\to \\{0,1\\}^n$ 與真隨機置換 $\\text{Perm}: \\{0,1\\}^n \\to \\{0,1\\}^n$。",
            "2. 定義事件 $\\text{Coll}$：在對 $\\text{Func}$ 進行 $q$ 次相異查詢 $X_1, \\dots, X_q$ 時，輸出出現碰撞（即存在 $i \\neq j$ 使得 $\\text{Func}(X_i) = \\text{Func}(X_j)$）。",
            "3. 根據差異引理（Difference Lemma）：在事件 $\\text{Coll}$ 未發生前，真隨機函數的所有輸出皆兩兩相異，其條件機率分佈與無放回抽樣的真隨機置換完全相同！",
            "4. 故兩函式庫之區分優勢上限等於碰撞事件機率：$\\mathbf{Adv} \\le \\Pr[\\text{Coll}]$。",
            "5. 計算生日碰撞機率上限（Union Bound）：$\\Pr[\\text{Coll}] \\le \\sum_{1 \\le i < j \\le q} \\Pr[\\text{Func}(X_i) = \\text{Func}(X_j)] = \\binom{q}{2} \\frac{1}{2^n} = \\frac{q(q-1)}{2 \\cdot 2^n} < \\frac{q^2}{2^{n+1}}$。證明完畢。"
        ],
        "algorithm": "結論：當查詢次數 $q \\ll 2^{n/2}$ 時，任何置換（如 AES）皆可安全地被視為真隨機函數（PRF）。",
        "pitfall": "必須點出在「碰撞未發生前，兩者輸出完全不可區分」這一關鍵前提。"
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
            "1. Feistel 第 $i$ 輪正向加密公式（輸入 $(L_{i-1}, R_{i-1})$）：\n   $L_i = R_{i-1}$\n   $R_i = L_{i-1} \\oplus F(K_i, R_{i-1})$。",
            "2. 檢驗逆向解密運算（給定第 $i$ 輪輸出 $(L_i, R_i)$ 與子金鑰 $K_i$）：\n   a. 由於 $L_i = R_{i-1}$，解密端直接獲得上一輪之右半部：$R_{i-1} := L_i$。\n   b. 將 $R_{i-1}$ 代入輪函數計算 $F(K_i, R_{i-1}) = F(K_i, L_i)$。\n   c. 兩端 XOR 還原上一輪之左半部：$R_i \\oplus F(K_i, L_i) = (L_{i-1} \\oplus F(K_i, R_{i-1})) \\oplus F(K_i, R_{i-1}) = L_{i-1}$。",
            "3. 由於 XOR 運算滿足自反性（$A \\oplus B \\oplus B = A$），還原過程完全無需對輪函數 $F$ 求逆！",
            "4. 因此，只要子金鑰以反向順序（$K_r, K_{r-1}, \\dots, K_1$）代入，解密演算法可直接重用加密電路結構。"
        ],
        "algorithm": "架構優勢：允許密碼設計者在輪函數 $F$ 中任意使用單向不可逆組件（如 S-Box、Hash、非對稱壓縮映射）。",
        "pitfall": "切勿回答「因為輪函數 $F$ 可逆」；Feistel 的核心精髓恰恰在於輪函數不需可逆。"
    },
    {
        "id": "proof-21",
        "category": "ch6-7",
        "chapter": "Ch. 7",
        "title": "2 輪 Feistel 差分不變量破壞法形式證明",
        "source": "課本 Exercise 7.3 / 練習一 9",
        "technique": "差分消除不變量（Differential Invariant）破壞",
        "target": "證明 2 輪 Feistel 網路無法抵抗選擇明文攻擊，可在常數次查詢內被完全區分。",
        "steps": [
            "1. 設輸入明文為 $(L_0, R_0)$。計算 2 輪輸出：\n   第 1 輪：$L_1 = R_0$, $R_1 = L_0 \\oplus F(K_1, R_0)$。\n   第 2 輪：$L_2 = R_1 = L_0 \\oplus F(K_1, R_0)$, $R_2 = L_1 \\oplus F(K_2, R_1) = R_0 \\oplus F(K_2, L_2)$。",
            "2. 挑選兩筆具備「相同右半部」的相異明文：$P = (L_0, R_0)$ 與 $P' = (L'_0, R_0)$，其中 $R_0 = R'_0$ 且 $L_0 \\neq L'_0$。",
            "3. 計算兩者輸出左半部的 XOR 差分：\n   $L_2 = L_0 \\oplus F(K_1, R_0)$\n   $L'_2 = L'_0 \\oplus F(K_1, R_0)$。\n   $L_2 \\oplus L'_2 = (L_0 \\oplus F(K_1, R_0)) \\oplus (L'_0 \\oplus F(K_1, R_0)) = L_0 \\oplus L'_0$！",
            "4. 輪函數運算 $F(K_1, R_0)$ 徹底相消！輸出左半部差分嚴格等於輸入左半部差分。"
        ],
        "algorithm": "區分者演算法：\n1. 查詢 P = (0, 0) 得 (L2, R2)\n2. 查詢 P' = (1, 0) 得 (L'2, R'2)\n3. 檢驗：若 L2 ^ L'2 == 1 輸出 1 (判定為 2-round Feistel)；否則輸出 0 (判定為真隨機置換)。優勢為 1 - 2^(-w)。",
        "pitfall": "記住差分關係發生的條件是「輸入明文共享相同的右半部（$R_0 = R'_0$）」。"
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
            "1. 輪函數在向量空間 $\\mathbb{F}_2^w$ 上為純仿射線性映射：$F(K_i, X) = X \\oplus K_i$。",
            "2. Feistel 每輪運算僅涉及變數交換與 XOR 線性相加。若將整棟密碼視為整體，複合 $r$ 輪後的輸出 $(L_r, R_r)$ 必可表示為明文 $(L_0, R_0)$ 的線性組合加上金鑰相加項：\n   $\\begin{pmatrix} L_r \\\\ R_r \\end{pmatrix} = \\mathbf{A}_r \\begin{pmatrix} L_0 \\\\ R_0 \\end{pmatrix} \\oplus \\mathbf{B}_r(K_1, \\dots, K_r)$，其中 $\\mathbf{A}_r$ 為公開固定的可逆矩陣。",
            "3. 由於滿足線性疊加原理，任取 4 筆滿足 $P_1 \\oplus P_2 \\oplus P_3 \\oplus P_4 = 0$ 的明文，其對應的密文必然滿足：\n   $C_1 \\oplus C_2 \\oplus C_3 \\oplus C_4 = \\mathbf{A}_r (P_1 \\oplus P_2 \\oplus P_3 \\oplus P_4) \\oplus (\\mathbf{B} \\oplus \\mathbf{B} \\oplus \\mathbf{B} \\oplus \\mathbf{B}) = 0$ 恆成立！",
            "4. 金鑰項在 4 點差分下完全自我抵消！"
        ],
        "algorithm": "4 點差分區分者：選取任意 $P_1, P_2, P_3$，設定 $P_4 = P_1 \\oplus P_2 \\oplus P_3$。查詢 4 筆明文密文 $C_1, C_2, C_3, C_4$。若 $C_1 \\oplus C_2 \\oplus C_3 \\oplus C_4 == 0$ 輸出 1；否則輸出 0。在真實置換下成立機率為 $2^{-2w}$，區分優勢達 $1 - 2^{-2w} \\approx 1$。",
        "pitfall": "證明核心在於線性函數之組合依然為線性函數，疊加再多輪亦無法產生任何密碼學非線性度（混淆度）。"
    },
    {
        "id": "proof-23",
        "category": "ch8",
        "chapter": "Ch. 8",
        "title": "決定性加密無狀態下必破 IND-CPA 形式反證法",
        "source": "課本 Theorem 8.5 / 投影片 1.5 Section 1 / 練習一 24",
        "technique": "CPA 重複查詢博弈與相等性檢測",
        "target": "任何無狀態（Stateless）且具備正確性的確定性加密方案（Deterministic Encryption），絕不可能達成 IND-CPA 安全性。",
        "steps": [
            "1. 設加密方案 $\\text{Enc}$ 為無狀態確定性演算法，即對相同金鑰 $K$ 與明文 $M$，$\\text{Enc}(K, M)$ 恆輸出相同之密文 $C$。",
            "2. 構造 CPA 攻擊者演算法 $\\mathcal{A}$：\n   a. 攻擊者選擇兩筆相異明文 $M_0 \\neq M_1$。\n   b. 利用 CPA 提供之加密 Oracle $\\text{Enc}(K, \\cdot)$，預先查詢明文 $M_0$，獲得密文 $C_0 := \\text{Enc}(K, M_0)$。\n   c. 攻擊者將 $(M_0, M_1)$ 提交給挑戰 Oracle，獲得挑戰密文 $C^* = \\text{Enc}(K, M_b)$。\n   d. 比對密文：若 $C^* == C_0$，攻擊者猜測 $b' = 0$；否則猜測 $b' = 1$。",
            "3. 分析勝率：\n   若 $b = 0$，由確定性加密定義，$C^* = \\text{Enc}(K, M_0) = C_0$ 恆成立，$\\Pr[b' = 0 \\mid b = 0] = 1$。\n   若 $b = 1$，由方案之正確性 $\\text{Dec}(K, \\text{Enc}(K, M)) = M$，因為 $M_0 \\neq M_1$，故密文必定不相等 $C^* \\neq C_0$，$\\Pr[b' = 1 \\mid b = 1] = 1$。",
            "4. 區分優勢計算：$\\mathbf{Adv}_{\\text{cpa}} = |\\Pr[b'=0 \\mid b=0] - \\Pr[b'=0 \\mid b=1]| = |1 - 0| = 1$。方案在 CPA 下徹底被破譯。"
        ],
        "algorithm": "推論：所有達成 CPA 安全的對稱加密系統必須具備隨機性（如隨機 IV）或內部狀態（如不重複計數器）。",
        "pitfall": "必須強調攻擊者能在發起挑戰前後任意呼叫加密 Oracle，這是 CPA 相較於 OTS 的本質威力。"
    },
    {
        "id": "proof-24",
        "category": "ch8",
        "chapter": "Ch. 8",
        "title": "|M| = |C| 且具正確性之方案必破 CPA 證明",
        "source": "課本 Exercise 8.11 / 練習一 33",
        "technique": "有限集單射即雙射引理與確定性必然性",
        "target": "若加密方案滿足正確性且明文空間大小等於密文空間大小（$|\\mathcal{M}| = |\\mathcal{C}|$），則該方案絕不可能達成 CPA 安全。",
        "steps": [
            "1. 由正確性條件知：對任意固定金鑰 $K$，解密演算法滿足 $\\text{Dec}(K, \\text{Enc}(K, M)) = M$。這要求加密映射 $\\text{Enc}(K, \\cdot)$ 必須為單射（Injective），否則兩筆不同明文若映射到同一密文將無法唯一還原。",
            "2. 由集合基數條件：明文空間與密文空間為同等大小的有限集（$|\\mathcal{M}| = |\\mathcal{C}| < \\infty$）。根據有限集合論引理，有限集到等大有限集的單射映射必定亦為滿射（Surjective），從而必為雙射（Bijective）。",
            "3. 雙射映射之必然推論：對任意給定明文 $M$，其在密文空間中存在且僅存在唯一合法的密文 $C$。這意味著加密過程絕不可能消耗任何隨機位元（若有隨機位元，一筆明文將對應多個可能密文，導致 $|\\mathcal{C}| > |\\mathcal{M}|$ 產生矛盾）。",
            "4. 因此，該方案必定為無狀態確定性加密演算法（Deterministic Encryption）。",
            "5. 根據「決定性加密無狀態下必破 IND-CPA 定理」，確定性加密方案之 CPA 優勢恆為 1，絕不可能達成 CPA 安全。"
        ],
        "algorithm": "結論：任何 CPA 安全的加密方案密文長度必須嚴格大於明文長度（$|\\mathcal{C}| > |\\mathcal{M}|$），必須攜帶隨機鹽（IV 或 Nonce）。",
        "pitfall": "核心在於引用「有限集上單射必為雙射」，進而導出演算法無隨機擴展空間的確定性必然性。"
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
            "1. 建立遊戲序列：\n   Game 0：真實 CPA 遊戲，加密使用真實 PRF $F(K, \\cdot)$。\n   Game 1：將 PRF $F(K, \\cdot)$ 替換為真隨機函數 $\\mathcal{R}(\\cdot)$。\n   由 PRF 安全性：$|\\Pr[\\text{Win}_0] - \\Pr[\\text{Win}_1]| \\le \\mathbf{Adv}_F^{\\text{prf}}(\\mathcal{B})$。",
            "2. 分析 Game 1（使用真隨機函數 $\\mathcal{R}$）：每次加密隨機挑選 $R \\leftarrow \\{0, 1\\}^\\lambda$。定義壞事件 $\\text{Coll}$：在 $q$ 次加密查詢中，隨機數 $R$ 發生重複碰撞。",
            "3. 根據生日界限：$q$ 次獨立隨機抽樣之碰撞機率滿足 $\\Pr[\\text{Coll}] \\le \\frac{q(q-1)}{2 \\cdot 2^\\lambda} \\le \\frac{q^2}{2^{\\lambda+1}}$。",
            "4. 在事件 $\\text{Coll}$ 未發生前，所有查詢之 $R$ 兩兩相異。真隨機函數 $\\mathcal{R}$ 在相異輸入處的輸出 $\\mathcal{R}(R)$ 為獨立均勻隨機字串，等價於一次性密碼本（OTP）遮罩！",
            "5. 由 OTP 完善保密性，在無碰撞條件下攻擊者勝率嚴格為 $\\frac{1}{2}$：$\\Pr[\\text{Win}_1 \\mid \\neg\\text{Coll}] = \\frac{1}{2}$。",
            "6. 綜合差異引理：$\\mathbf{Adv}_{\\text{cpa}} \\le 2 \\cdot \\mathbf{Adv}_F^{\\text{prf}}(\\mathcal{B}) + \\frac{q^2}{2^\\lambda}$，優勢為可忽略函數，方案達成 IND-CPA。"
        ],
        "algorithm": "碰撞分析：只要查詢次數 $q \\ll 2^{\\lambda/2}$，方案即可提供堅不可摧的語義安全性。",
        "pitfall": "證明中切勿忘記考慮隨機數 $R$ 在生日界限下的碰撞機率項 $\\frac{q^2}{2^{\\lambda+1}}$。"
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
            "1. 密文格式為 $(C_1, C_2) = (R, F(K, M) \\oplus R)$。隨機數 $R$ 雖然是均勻隨機抽取，但居然未傳入 PRF 內部，而是直接外加在最外層！",
            "2. 攻擊者計算兩部分密文之 XOR 和：$C_1 \\oplus C_2 = R \\oplus (F(K, M) \\oplus R) = F(K, M)$！隨機數 $R$ 徹底相消，直接暴露出決定性的偽隨機評估值 $F(K, M)$！",
            "3. 構造 CPA 區分者演算法 $\\mathcal{A}$：\n   a. 提交兩筆明文 $M_0 = 0^n, M_1 = 1^n$ 給挑戰 Oracle，獲挑戰密文 $(C_1^*, C_2^*)$。\n   b. 計算挑戰特徵值：$V^* = C_1^* \\oplus C_2^* = F(K, M_b)$。\n   c. 呼叫加密 Oracle 查詢明文 $M_0$，獲得密文 $(C_1', C_2')$。\n   d. 計算特徵值：$V' = C_1' \\oplus C_2' = F(K, M_0)$。\n   e. 比對：若 $V^* == V'$ 輸出 0；否則輸出 1。",
            "4. 優勢計算：若 $b = 0$ 則 $V^* == V'$ 恆成立；若 $b = 1$ 則因 $F$ 之偽隨機性，$F(K, M_1) == F(K, M_0)$ 機率為 $2^{-\\lambda}$。優勢 $\\mathbf{Adv} = 1 - 2^{-\\lambda} \\approx 1$。"
        ],
        "algorithm": "區分者代碼：\n1. (C1*, C2*) = Challenge(M0, M1)\n2. (C1', C2') = Encrypt(M0)\n3. return ((C1* ^ C2*) == (C1' ^ C2')) ? 0 : 1",
        "pitfall": "隨機數 $R$ 必須作為 PRF 的輸入引數（如 $F(K, R) \\oplus M$），若置於 PRF 外部會被線性差分直接抹除。"
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
            "1. 標準 CBC 加密第一區塊公式：$C_1 = \\text{AES}_K(IV \\oplus M)$。若 IV 為均勻且不可預測，則 $IV \\oplus M$ 扮演隨機遮罩。",
            "2. 假設實作缺陷：攻擊者在發起下一次加密查詢前，能預先獲知下一次加密將使用的向量，記為 $IV_{\\text{next}}$。",
            "3. 攻擊演算法：\n   a. 提交明文對 $M_0, M_1$ 給挑戰 Oracle，獲得挑戰密文 $(IV^*, C_1^*)$，其中 $C_1^* = \\text{AES}_K(IV^* \\oplus M_b)$。\n   b. 獲取系統下一次將採用的可預測向量 $IV_{\\text{next}}$。\n   c. 構造特定差分補償明文：$M_{\\text{query}} = IV_{\\text{next}} \\oplus IV^* \\oplus M_0$。\n   d. 提交 $M_{\\text{query}}$ 給加密 Oracle，系統使用 $IV_{\\text{next}}$ 進行加密，其密文第一區塊為：\n      $C_{\\text{query}} = \\text{AES}_K(IV_{\\text{next}} \\oplus M_{\\text{query}}) = \\text{AES}_K(IV_{\\text{next}} \\oplus (IV_{\\text{next}} \\oplus IV^* \\oplus M_0)) = \\text{AES}_K(IV^* \\oplus M_0)$！\n   e. 比對：若 $C_{\\text{query}} == C_1^*$，代表 $M_b = M_0$，輸出 0；否則輸出 1。",
            "4. 優勢計算：若 $b = 0$，兩密文完全恆等；若 $b = 1$，相撞機率為 $2^{-128}$。區分優勢達 $\\mathbf{Adv} = 1 - 2^{-128} \\approx 1$。"
        ],
        "algorithm": "歷史警示：此機制即為歷史上攻破 TLS 1.0 的著名 BEAST（Browser Exploit Against SSL/TLS）攻擊原型，迫使產業全面淘汰可預測 IV。",
        "pitfall": "CBC 模式之 IV 不僅要保證不重複，而且在明文確定前必須保持不可預測（Unpredictable）。"
    }
]

# Write to js/proof_sheet_data.js
output_js_path = os.path.join("js", "proof_sheet_data.js")
with open(output_js_path, "w", encoding="utf-8") as f:
    f.write("// In-Scope Proof Cheat Sheet Data (Filtered strictly up to Slides 1.5 Section 1)\n")
    f.write("// Covering Ch. 1, 2, 4, 5, 6, 7, 8 (Excludes Ch. 9 CCA, Padding Oracle, AE)\n\n")
    f.write("const PROOF_SHEET_DATA = ")
    f.write(json.dumps(PROOF_SHEET_DATA, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Successfully generated {output_js_path} with {len(PROOF_SHEET_DATA)} in-scope formal proofs!")
