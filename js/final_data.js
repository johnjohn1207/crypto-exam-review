// Final Exam Lecture Modules Data
// Mapped to uploaded course slides: 1.5 (Sec 2-2.2), 1.7 (Sec 1-3), 1.8 (Sec 1-3)

const FINAL_EXAM_MODULES = [
  {
    id: "slide-1-5",
    chapter: "投影片 1.5",
    pages: "P.15 - P.85",
    title: "選擇密文攻擊 (CCA) 與認證加密 (AE)",
    page_url: "final_ch9_cca_ae.html",
    quiz_scope: "1.5",
    quiz_count: 38,
    summary: "解密預言機、CTR 延展性、Padding Oracle 逐字節盲解、MAC 三大組合範式與 AES-GCM。"
  },
  {
    id: "slide-1-7",
    chapter: "投影片 1.7",
    pages: "P.1 - P.49",
    title: "困難問題、Diffie-Hellman 與 RSA",
    page_url: "final_ch11_dh_hard_problems.html",
    quiz_scope: "1.7",
    quiz_count: 32,
    summary: "乘法循環群 ℤ*p、DLP、DH 協定與手算、DDH ≤ CDH ≤ DLP 歸約、MITM 攻擊與 RSA 退場原因。"
  },
  {
    id: "slide-1-8",
    chapter: "投影片 1.8",
    pages: "P.1 - P.61",
    title: "橢圓曲線與數位簽章（初學者白話版）",
    page_url: "final_1_8_ecc_signatures.html",
    quiz_scope: "1.8",
    quiz_count: 35,
    summary: "點加法與 ECDLP 手算、ECDH、ECDSA vs. Ed25519、PS3 破解、無效曲線／小子群攻擊與後量子混合加密。"
  }
];
