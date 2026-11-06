// Final Exam Curriculum Framework Data (Post-Midterm Modules)
// Covering Ch. 9 (CCA, Padding Oracle, AE) and subsequent Final Exam topics

const FINAL_EXAM_MODULES = [
  {
    id: "final-mod-1",
    chapter: "Ch. 9",
    title: "選擇密文攻擊 (CCA) 與認證加密 (AE)",
    status: "completed",
    badge: "已注入上線・點擊進入",
    page_url: "final_ch9_cca_ae.html",
    description: "完整收錄投影片 1-5 Section 2 至 Section 2.2（P.15-85）。深入剖析解密預言機（Decryption Oracle）、延展性破壞、Null-Oracle 盲解、PKCS#7 Padding Oracle 攻擊、Encrypt-then-MAC 形式化證明、AES-GCM (GHASH) 與 AEAD 綁定機制。",
    key_topics: [
      "CCA 安全性 Library 庫定義與解密預言機",
      "延展性 (Malleability) 與 Null-Oracle 逐字節盲解推導",
      "PKCS#7 Padding Oracle 攻擊 (POODLE 原理) 與 Timing 側信道",
      "Encrypt-then-MAC vs Encrypt-and-MAC vs MAC-then-Encrypt 三大組合嚴格證明",
      "AES-GCM (GHASH 有限體乘法) 與 AEAD 關聯資料防範重放攻擊"
    ],
    expected_materials: ["投影片 1-5 Section 2 (已完成注入)", "形式證明與區分器 (已完備)", "全真模擬測驗題庫 (已上線)"]
  },
  {
    id: "final-mod-2",
    chapter: "Ch. 10",
    title: "密碼雜湊函數與訊息鑑別碼 (Hash & MAC)",
    status: "ready_for_materials",
    badge: "資料完整性基石",
    description: "探討無金鑰雜湊函數之單向性（Preimage Resistance）與抗碰撞性（Collision Resistance），深入 Merkle-Damgård 結構與長度擴展攻擊，以及 HMAC 安全性證明。",
    key_topics: [
      "抗第一原像 (Preimage)、抗第二原像 (Second Preimage) 與抗碰撞 (Collision)",
      "Merkle-Damgård 結構抗碰撞性保持證明定理",
      "長度擴展攻擊 (Length Extension Attack) 與為什麼純 H(K || M) 不安全",
      "HMAC 雙重雜湊架構 (Nested MAC) 與安全性歸約",
      "CBC-MAC 與 CMAC 在可變長度訊息下的安全性修正"
    ],
    expected_materials: ["雜湊講義", "HMAC 構造證明", "長度擴展攻擊範例"]
  },
  {
    id: "final-mod-3",
    chapter: "Ch. 11",
    title: "數論基礎與單向陷門置換 (Number Theory & TDP)",
    status: "ready_for_materials",
    badge: "公鑰密碼數學核心",
    description: "公鑰密碼學之數論基石。歐幾里得演算法、模反元素、歐拉函數、費馬小定理、中國剩餘定理（CRT），以及離散對數問題（DLP）與 CDH / DDH 困難度假設。",
    key_topics: [
      "擴展歐幾里得演算法 (Extended Euclidean) 計算模反元素",
      "歐拉函數 φ(n)、費馬小定理 (Fermat's Little Theorem) 與尤拉定理",
      "中國剩餘定理 (Chinese Remainder Theorem, CRT) 快速運算",
      "循環群 (Cyclic Groups)、生成元 (Generator) 與子群階數 Lagrange 定理",
      "離散對數問題 (DLP)、計算 Diffie-Hellman (CDH) 與判定 Diffie-Hellman (DDH) 假定"
    ],
    expected_materials: ["數論講義", "模運算快速冪練習", "Diffie-Hellman 假定證明"]
  },
  {
    id: "final-mod-4",
    chapter: "Ch. 12",
    title: "公鑰加密體系 (Public-Key Encryption)",
    status: "ready_for_materials",
    badge: "非對稱加密典範",
    description: "非對稱金鑰體系的核心方案：Diffie-Hellman 金鑰交換、ElGamal 語意安全公鑰加密、RSA 加密體系與 OAEP 填充標準。",
    key_topics: [
      "Diffie-Hellman 金鑰交換協定與被動竊聽安全性 (基於 DDH)",
      "ElGamal 公鑰加密系統之 IND-CPA 安全性 (DDH 歸約證明)",
      "教科書 RSA (Textbook RSA) 的延展性破綻與小指數攻擊",
      "RSA-OAEP (Optimal Asymmetric Encryption Padding) 之 CCA2 安全性",
      "混合加密 (Hybrid Encryption / KEM-DEM 架構)"
    ],
    expected_materials: ["PKE 講義", "ElGamal CPA 歸約證明", "RSA 攻擊手冊"]
  },
  {
    id: "final-mod-5",
    chapter: "Ch. 13",
    title: "數位簽章與身份認證 (Digital Signatures)",
    status: "ready_for_materials",
    badge: "不可否認性保證",
    description: "數位簽章標準定義與不可偽造性（EUF-CMA）。涵蓋 RSA 簽章 (RSA-FDH)、Schnorr 簽章、DSA / ECDSA 以及盲簽章技術。",
    key_topics: [
      "EUF-CMA (Existential Unforgeability under Chosen-Message Attacks) 博弈模型",
      "Hash-and-Sign 範式與隨機預言機模型 (Random Oracle Model, ROM)",
      "RSA 全域雜湊簽章 (RSA-FDH) 安全性證明",
      "Schnorr 識別協定與 Fiat-Shamir 變換導出 Schnorr 簽章",
      "橢圓曲線數位簽章 (ECDSA) 與隨機 Nonce 洩漏致命後果"
    ],
    expected_materials: ["數位簽章投影片", "EUF-CMA 證明", "ECDSA 隨機數攻擊"]
  },
  {
    id: "final-mod-6",
    chapter: "Ch. 14",
    title: "後量子密碼學前瞻 (Post-Quantum Cryptography)",
    status: "ready_for_materials",
    badge: "抗量子終極防線",
    description: "應對量子電腦 Shor 演算法對 RSA / ECC 毀滅性威脅之後量子密碼學。以晶格密碼（Lattice-based）為核心，深入容錯學習（LWE / Ring-LWE）及 NIST 標準演算法（ML-KEM, ML-DSA）。",
    key_topics: [
      "量子計算威脅：Shor 演算法對 RSA / 離散對數之多項式時間破解原理",
      "Grover 演算法對對稱密鑰與雜湊之開根號加速影響",
      "晶格 (Lattice) 幾何結構與最短向量問題 (SVP) / 最近向量問題 (CVP)",
      "容錯學習問題 (Learning With Errors, LWE) 與 Ring-LWE 數學公式",
      "NIST 後量子密碼標準：ML-KEM (Kyber) 金鑰封裝與 ML-DSA (Dilithium) 數位簽章"
    ],
    expected_materials: ["後量子密碼講義", "LWE 數學原理", "NIST PQC 標準規範"]
  }
];
