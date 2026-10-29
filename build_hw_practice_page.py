# -*- coding: utf-8 -*-
"""
Standalone builder for Homework 1 and Practice 1 comprehensive data and webpage.
Filtered strictly up to Slides 1.5 Section 1 (Excludes Ch. 9 CCA/Padding Oracle/AE).
"""
import json
import os
import re
import sys

print("Building Homework 1 & Practice 1 in-scope dataset (Up to Slides 1.5 Section 1)...")

import build_exam_data

raw_hw1 = build_exam_data.HW1_SOLUTIONS
raw_p1 = build_exam_data.PRACTICE1_SOLUTIONS

HW1_CONCEPTS = {
    "hw1-1a": "夏農完善保密性定義（Shannon's Perfect Secrecy: $\\Pr[C = c \\mid M = m] = \\Pr[C = c]$）與解密正確性約束（Decryption Correctness: $\\text{Dec}(K, \\text{Enc}(K, M)) = M$）。AND 運算在布林域上非單射映射（$0 \\wedge 0 = 0 \\wedge 1 = 0$），破壞解密唯一性；當 $M=0$ 時 $\\Pr[C=1 \\mid M=0]=0 \\neq \\Pr[C=1 \\mid M=1]=\\frac{1}{2}$，違反密文獨立性。",
    "hw1-1b": "有限阿貝爾群 $\\mathbb{Z}_{10}$ 之加法同構與均勻分佈保持性質。群中每個元素皆具唯一加法反元素（Additive Inverse），使得同餘方程 $K \\equiv C - M \\pmod{10}$ 存在唯一解，密文條件機率恆為 $\\frac{1}{10}$，嚴格達成完善保密性。",
    "hw1-1c": "金鑰重用缺陷（Two-Time Pad Vulnerability）與夏農金鑰長度下界定理（$|\\mathcal{K}| \\ge |\\mathcal{M}|$）。雙區塊共用金鑰導致差分消除：$C_1 \\oplus C_2 = M_1 \\oplus M_2$，攻擊者可透過位元差分、已知標頭破譯（Crib Dragging）或區分者博弈徹底擊潰保密性。",
    "hw1-2a": "函式庫不可區分性定義（Library Indistinguishability: $\\mathcal{L}_1 \\equiv \\mathcal{L}_2$）與雙隨機獨立變數 XOR 均勻性引理。邏輯分支等價分析：當 $M = R_1$ 時，$M \\oplus R_1 \\oplus R_2 = R_1 \\oplus R_1 \\oplus R_2 = R_2$，分支完全恆等，輸出分佈無差別。",
    "hw1-2b": "密碼系統內部狀態保持與一致性約束（Consistency Constraint: $\\text{Dec}(K, \\text{Enc}(K, M)) = M$）。真隨機獨立查詢與密碼系統的本質區別在於金鑰跨查詢的一致性維護。",
    "hw1-3": "單次保密性（One-Time Secrecy / IND-OTS）定義。派生密文 $C_2 = C_1 \\oplus 1^n$ 具備雙射一對一確定性，密文對分佈不依賴於挑戰明文 $M_b$，區分優勢嚴格為 0。",
    "hw1-4a": "偽隨機產生器（PRG）安全性定義與內部中間狀態隱藏原則。串接結構（Cascaded PRG）若直接在輸出公開中間種子 $B$，攻擊者可直接本地計算 $G(B)$ 並比對後續區塊，區分優勢達 $1 - 2^{-2\\lambda}$。",
    "hw1-4b": "偽隨機函數（PRF）非線性要求與線性差分攻擊。線性構造 $F(K, X) = G(K) \\oplus X$ 具有恆等輸出差分 $F(K, X_1) \\oplus F(K, X_2) = X_1 \\oplus X_2$，與真隨機函數的獨立性矛盾。",
    "hw1-5a": "選擇明文安全模型（IND-CPA Security）、加密方案隨機化必要性（Randomized Encryption）、PRF 評估輸入不重複原則與 ECB 模式之決定性破綻。"
}

P1_CONCEPTS = {
    "p1-1": "夏農完善保密性定義：對所有明文 $m$ 與密文 $c$，條件機率 $\\Pr[C = c \\mid M = m]$ 恆等於無條件機率 $\\Pr[C = c]$，密文分佈與明文獨立。",
    "p1-2": "黑箱函式庫模型（Black-Box Library Model）：攻擊者程式僅能透過公開介面進行 query，不可直接讀取內部金鑰或變數狀態。",
    "p1-3": "函式庫互換性（Interchangeability）：介面相同且所有多項式時間程式皆無法區分兩者輸出（$\\mathcal{L}_1 \\equiv \\mathcal{L}_2$）。",
    "p1-4": "可忽略函數定義（Negligible Function）：$\\forall c > 0, \\exists N_0, \\forall \\lambda > N_0: \\mu(\\lambda) < \\frac{1}{\\lambda^c}$，比任何多項式倒數收斂更快。",
    "p1-5": "生日界限定理（Birthday Bound）：在大小為 $N$ 的均勻隨機空間中，約取樣 $\\sqrt{N}$ 次即可產生 50% 碰撞機率（$\\approx 1.177 \\sqrt{N}$）。",
    "p1-6": "差異引理（Difference Lemma / Bad Event）：兩函式庫在壞事件發生前行為完全相同，區分優勢上限受限於壞事件機率 $\\mathbf{Adv} \\le \\Pr[\\text{bad}]$。",
    "p1-7": "PRG 與 PRF 的本質差異：PRG 僅能順序展開固定長度串流，PRF 支援任意指數級輸入空間之隨機存取。",
    "p1-8": "Feistel 密碼結構之可逆性（Invertibility）：每輪結構透過對稱 XOR 運算保證逆運算存在，完全無需輪函數 $F$ 本身可逆。",
    "p1-9": "2 輪 Feistel 差分不變量：當兩筆輸入右半部相同時，輸出左半部的 XOR 差分恆等於輸入左半部的 XOR 差分，金鑰完全抵消。",
    "p1-10": "PRF 黃金法則（Golden Rule of PRFs）：在同一個金鑰下，絕不可傳入重複輸入給 PRF，保證輸出等價於獨立真隨機字串。",
    "p1-11": "現代密碼學語意安全洩漏邊界：所有標準加密方案允許且不可避免洩漏明文的長度 $|M|$。",
    "p1-14": "OTP 理論與工程實務之鴻溝：金鑰同步衝突、快閃記憶體 Wear Leveling 物理殘留、金鑰分發網路爆炸（$O(N^2)$ 通道瓶頸）。",
    "p1-15": "IND-OTS 挑戰者博弈架構：利用全機率公式與條件對稱性，嚴格推導 $\\Pr[b' = b] = \\frac{1}{2}$，證明 OTP 之完美不可區分性。",
    "p1-16": "偽可證明安全辨析：混淆 XOR 運算與 OTP 的本質、金鑰長度不足、Two-time pad 災難與伺服器單點故障。",
    "p1-17": "邊際機率分佈不變性（Marginal Distribution Invariance）：未被介面回傳之獨立隨機變數對函式庫行為完全無統計影響。",
    "p1-18": "隨機數線性重用破壞法：建構區分者 $D$ 消除重複隨機數，並利用 PRF 實現非線性隨機遮罩進行修復。",
    "p1-19": "混淆論證技術（Hybrid Argument）：構造中間混合函式庫 $\\mathcal{L}_{\\text{hyb}}$，逐步推導各步驟等價性與統計不可區分性。",
    "p1-20": "計算安全性與資訊理論安全性實務權衡：計算安全性以多項式時間界限突破夏農下界，允許短金鑰加密長訊息。",
    "p1-21": "雜湊碰撞之生日界限數學推導：$k \\approx \\sqrt{2 \\ln 2 \\cdot 2^n} \\approx 1.177 \\times 2^{n/2}$，未來十年安全強度要求至少 256 位元。",
    "p1-22": "OTP 實務瓶頸與 PRG 必要性：突破夏農金鑰長度限制 $|\\mathcal{K}| \\ge |\\mathcal{M}|$，以短金鑰種子偽隨機展開長串流。",
    "p1-23": "PRF 與 PRP 綜合對比：定義差異、雙射約束、PRF/PRP Switching Lemma 降級引理與生日碰撞必然性。",
    "p1-24": "決定性加密必破 CPA 定理：雙查詢區分者演算法建構、相等性測試與實務重放安全破壞。",
    "p1-27": "模 $n$ 乘法 OTP 之質數條件：有限環 $\\mathbb{Z}_n$ 乘法群 $\\mathbb{Z}_n^\\times$、群階數 $\\phi(n)=n-1$ 與零因子分析，證明 $n$ 為質數時密文均勻分佈。",
    "p1-28": "模 10 乘法加密無單次保密性嚴格反例證明：利用合數環零因子 $5 \\times 2 \\equiv 0 \\pmod{10}$ 導致機率退化。",
    "p1-29": "夏農金鑰長度下界定理 $|\\mathcal{K}| \\ge |\\mathcal{M}|$ 嚴格反證法：解密可能像集合 $S(c) = \\{\\text{Dec}(k, c) \\mid k \\in \\mathcal{K}\\}$ 與鴿籠原理。",
    "p1-30": "PRG 反饋型構造安全判定：狀態隱藏構造之 Hybrid Proof 歸納法，與狀態洩漏構造之攻擊演算法。",
    "p1-31": "$H(K, X) = F(K, X) \\oplus F(K, 0^n)$ 非安全 PRF 證明：零輸入全零漏洞與區分優勢計算 $\\mathbf{Adv} = 1 - 2^{-m}$。",
    "p1-32": "線性輪函數 Feistel 任意輪數必破證明：$\\mathbb{F}_2^w$ 仿射空間奇偶差分守恆與 4 點差分區分者建構。",
    "p1-33": "$|\\mathcal{M}| = |\\mathcal{C}|$ 且具備正確性之加密方案絕不可能達成 CPA 安全：有限集單射即雙射引理與決定性加密必然性證明。"
}

# 排除範圍外題目（Ch. 9 CCA、Padding Oracle、AE）
OUT_OF_SCOPE_IDS = set(["hw1-5b", "p1-12", "p1-13", "p1-25", "p1-26", "p1-34"])

# 考點證明題集合（In-scope Proofs）
PROOF_IDS = set([
    "hw1-1a", "hw1-1b", "hw1-1c", "hw1-2a", "hw1-2b", "hw1-3", "hw1-4a", "hw1-4b", "hw1-5a",
    "p1-9", "p1-15", "p1-17", "p1-18", "p1-19", "p1-21", "p1-23", "p1-24",
    "p1-27", "p1-28", "p1-29", "p1-30", "p1-31", "p1-32", "p1-33"
])

PROCESSED_ITEMS = []

for h in raw_hw1:
    item_id = h["id"]
    if item_id in OUT_OF_SCOPE_IDS:
        continue
    PROCESSED_ITEMS.append({
        "id": item_id,
        "source": "作業一",
        "source_tag": "hw1",
        "part": "作業一",
        "chapter": h.get("chapter", "Ch. 1-2"),
        "category": h.get("category", "ch1-2"),
        "title": h.get("title", ""),
        "is_proof": item_id in PROOF_IDS,
        "question": h.get("question", ""),
        "concept": HW1_CONCEPTS.get(item_id, "核心觀念解析"),
        "intuition": h.get("intuition", ""),
        "proof": h.get("proof", ""),
        "pitfall": h.get("pitfall", ""),
        "answer": None
    })

for p in raw_p1:
    item_id = p["id"]
    if item_id in OUT_OF_SCOPE_IDS:
        continue
    part_str = p.get("part", "Part A")
    source_tag = "p1_a" if "Part A" in part_str else ("p1_b" if "Part B" in part_str else "p1_c")
    PROCESSED_ITEMS.append({
        "id": item_id,
        "source": f"練習一 ({part_str})",
        "source_tag": source_tag,
        "part": part_str,
        "number": p.get("number", ""),
        "chapter": p.get("chapter", "Ch. 1"),
        "category": p.get("category", "ch1-2"),
        "title": p.get("title", ""),
        "is_proof": item_id in PROOF_IDS,
        "question": p.get("question", ""),
        "concept": P1_CONCEPTS.get(item_id, "核心觀念解析"),
        "intuition": p.get("intuition", ""),
        "proof": p.get("proof", ""),
        "pitfall": p.get("pitfall", ""),
        "answer": p.get("answer", None)
    })

output_js_path = os.path.join("js", "hw_practice_data.js")
with open(output_js_path, "w", encoding="utf-8") as f:
    f.write("// In-Scope Homework 1 & Practice 1 Data (Strictly up to Slides 1.5 Section 1)\n")
    f.write("// Excludes Ch. 9 CCA/AE/Padding Oracle (hw1-5b, p1-12, p1-13, p1-25, p1-26, p1-34)\n\n")
    f.write("const HW_PRACTICE_DATA = ")
    f.write(json.dumps(PROCESSED_ITEMS, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Generated {output_js_path} with {len(PROCESSED_ITEMS)} in-scope items ({len(PROOF_IDS)} proofs).")
print(f"Excluded {len(OUT_OF_SCOPE_IDS)} out-of-scope items.")
