// Final Exam Curriculum Framework Data
// Strictly mapped to official course slide decks, sections, and page numbers

const FINAL_EXAM_MODULES = [
  {
    id: "slide-1-5",
    slide_file: "1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf",
    slide_title: "投影片 1.5（Sec 2 至 Sec 2.2 ｜ P.15 - P.85）",
    chapter: "投影片 1.5",
    title: "選擇密文攻擊 (CCA) 與認證加密 (AE)",
    status: "completed",
    badge: "已完成・精準對齊 P.15-85",
    page_url: "final_ch9_cca_ae.html",
    description: "嚴格對應原版投影片 1.5 從 Section 2 開始至 Section 2.2（第 15 頁至第 85 頁）。逐頁剖析解密預言機（P.18-19）、Null-Oracle 逐字節盲解（P.20-33）、真實格式預言機（P.34-37）、1-bit 延展性與拼裝密文（P.38-44）、MAC 與三大組合範式（P.45-61）、AES-GCM 與 AEAD 關聯資料（P.62-85）。",
    key_topics: [
      "【Sec 2 ｜ P.15-19】CCA 安全性定義與解密預言機（Decryption Oracle）",
      "【Sec 2 ｜ P.20-33】CTR 延展性與 Null-Oracle 逐字節盲解（複雜度 256×L）",
      "【Sec 2 ｜ P.34-37】真實世界格式預言機（PKCS#7 Padding Oracle、Timing、iMessage）",
      "【Sec 2 ｜ P.38-44】1-bit 延展性攻破 CCA（Advantage=1）與 Frankenstein 拼裝密文",
      "【Subsec 2.1 ｜ P.45-61】MAC、PRF as MAC、Encrypt-then-MAC 證明與三大組合對決",
      "【Subsec 2.2 ｜ P.62-85】認證加密 AE、AES-GCM (GHASH)、Nonce 重用災難、Replay 與 AD"
    ],
    expected_materials: ["投影片 1.5 原版 P.15-85 逐頁筆記", "13 題章節精選選擇題（附防呆解析）", "38 題完整線上模擬測驗"]
  },
  {
    id: "slide-1-7",
    slide_file: "1.7 Hard Problems and Diffie-Hellman.pdf",
    slide_title: "投影片 1.7（Sec 1 至 Sec 3 ｜ P.1 - P.49）",
    chapter: "投影片 1.7",
    title: "困難問題、群論與 Diffie-Hellman 金鑰交換",
    status: "completed",
    badge: "已完成・精準對齊 P.1-49",
    page_url: "final_ch11_dh_hard_problems.html",
    description: "嚴格對應原版投影片 1.7（第 1 頁至第 49 頁全覆蓋）。逐頁剖析計算非對稱性（P.2-8）、乘法循環群 ℤ*p 與生成元（P.9-15）、DLP 與課堂手算實戰 p=23, g=5（P.16-21）、DDH ≤ CDH ≤ DLP 難題層級歸約（P.22-25）、KDF 白化與前向保密（P.26-33）、MITM 中間人攻擊與四大 AKE 身分認證（P.34-42）、RSA 歷史與退場原因（P.43-48）。",
    key_topics: [
      "【Sec 1 ｜ P.2-8】計算非對稱性、單向陷阱函數與兩大古典問題（因數分解 vs 離散對數）",
      "【Sec 2 ｜ P.9-18】乘法循環群 ℤ*p 四大公理、生成元判定與離散對數問題 (DLP)",
      "【Sec 2 ｜ P.19-21】Diffie-Hellman 協定流程與手算實戰（p=23, g=5, a=6, b=15 推導 S=2）",
      "【Sec 2 ｜ P.22-25】DLP ≥ CDH ≥ DDH 難題層級歸約與二次剩餘檢驗破壞 DDH",
      "【Subsec 2.1 ｜ P.26-33】實務 DH、嚴禁直出 g^ab 當 AES 金鑰、KDF 白化與前向保密 (ECDHE)",
      "【Subsec 2.2 ｜ P.34-42】未認證 DH 之 MITM 攻擊、四大 AKE 協定對比（TLS/Signal/WhatsApp/SSH）",
      "【Sec 3 ｜ P.43-48】RSA 數學原理 ed≡1(mod φ(n))、對偶功能（加密+簽章）與現代淘汰退場原因"
    ],
    expected_materials: ["投影片 1.7 原版 P.1-49 逐頁筆記", "14 題章節精選選擇題（附防呆解析）", "32 題完整線上模擬測驗"]
  },
  {
    id: "quiz-center",
    slide_file: "期末考全選擇題題庫",
    slide_title: "期末全真選擇題測驗中心（70 題無死角全覆蓋）",
    chapter: "全真題庫",
    title: "期末全真選擇題特訓與隨機抽題模擬考",
    status: "completed",
    badge: "70 題庫・即刷即評",
    page_url: "final_quiz.html",
    description: "地毯式覆蓋投影片 1.5（Sec 2-2.2 ｜ P.15-85 共 38 題）與投影片 1.7（Sec 1-3 ｜ P.1-49 共 32 題）。支援單元一鍵篩選、即時防呆解析與考場常見陷阱提醒，並具備隨機抽題限時模擬考與評級成績單功能。",
    key_topics: [
      "支援投影片 1.5 (38 題) 與投影片 1.7 (32 題) 獨立範圍篩選",
      "考點覆蓋率 100%：手算同餘、群論判斷、攻擊次數計算、歸約鏈邏輯",
      "每題均附「官方原版推導」與「⚠️ 考場常見陷阱防呆」",
      "限時全真模擬考（可自訂 25 題、50 題或完整 70 題，自動計分與評級）"
    ],
    expected_materials: ["70 題高頻考點題庫", "即時刷題與錯題模式", "限時成績單結算系統"]
  },
  {
    id: "future-slot",
    slide_file: "待上傳期末後續投影片",
    slide_title: "後續授課教材預留槽位（如 1.8 數位簽章、後量子密碼學 PQC）",
    chapter: "後續進度",
    title: "期末後續進度教材即時注入槽位",
    status: "ready_for_materials",
    badge: "隨時待命中",
    description: "當授課教師釋出下一份投影片（例如數位簽章 Signatures、雜湊函數 Hash 深入、或後量子密碼學 PQC / Lattice / ML-KEM 等），上傳檔案後系統將立即精準對應投影片之 Section 與頁數，自動生成結構化閱讀筆記與選擇題！",
    key_topics: [
      "數位簽章 (Signatures)：EUF-CMA 安全模型、Schnorr 與 ECDSA",
      "後量子密碼學 (PQC)：Shor 演算法威脅、晶格密碼 (Lattice) 與 ML-KEM",
      "上傳新投影片即自動對齊 Section 與頁數建立導覽"
    ],
    expected_materials: ["待上傳後續投影片", "作業二題目", "期末總複習投影片"]
  }
];
