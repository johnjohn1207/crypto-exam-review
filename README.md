# 現代與後量子密碼學導論：複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對「現代與後量子密碼學導論」設計的雙模態線上複習與互動學習平台，完整收錄課程教材（Katz & Lindell、Mike Rosulek《The Joy of Cryptography》與劉子源教授講義）。

支援電腦、平板與手機跨裝置無縫瀏覽，具備沉浸式純閱讀與互動實作雙入口：

- **🚀 線上互動複習平台（推薦題庫與模擬）**：[https://johnjohn1207.github.io/crypto-exam-review/](https://johnjohn1207.github.io/crypto-exam-review/)
- **📖 密碼學精華筆記手冊（無干擾純閱讀）**：[https://johnjohn1207.github.io/crypto-exam-review/notes.html](https://johnjohn1207.github.io/crypto-exam-review/notes.html)

---

## 雙模態閱讀與切換說明

平台提供兩大獨立網頁，兩者頂部皆具備「一鍵快速切換」按鈕：

```
[線上互動平台 (index.html)] <====== 一鍵切換 ======> [精華筆記手冊 (notes.html)]
          \                                                   /
           \===============> [GitHub 原始碼庫] <==============/
```

1. **入口一：線上互動學習平台 (`index.html`)**
   - **8 大章節重點整理**：嚴格對應全部 6 份教材 PDF。
   - **四大互動演算實驗室（Playgrounds）**：
     - Two-Time Pad 攻擊模擬器（支援 Crib Dragging 與空白鍵探測）。
     - Feistel 網路單步輪變形展示器（Luby-Rackoff 輪數定理演示）。
     - Padding Oracle (PKCS#7) 逐位元組解密操作台。
     - IND-CPA 安全遊戲攻防演習棋盤（優勢度 Advantage 統計）。
   - **階梯式互動題目練習系統**：32 道精選深度題目，含逐步推導、混淆觀念剖析與錯題本。
   - **專業名詞速查辭典**：收錄 18+ 項核心密碼學原語與安全定義。

2. **入口二：密碼學精華筆記手冊 (`notes.html`)**
   - **純粹閱讀模式**：無答題與模擬器干擾，專注於長文閱讀與考前通讀。
   - **智慧型 Callout 卡片分層**：
     - 📜 核心理論 / 定理定義卡片（紫色標註）
     - ⚡ 攻防分析 / 漏洞運算卡片（琥珀色標註）
     - ⚠️ 考試易錯陷阱 / 防錯警告卡片（玫瑰紅標註）
   - **三種護眼閱讀主題**：深色模式（Dark）、羊皮紙紙張暖色（Sepia）、純白極簡（Light）。
   - **閱讀輔助工具**：A- / A+ 字級放大縮小、頂部吸頂閱讀進度條、全文即時檢索、一鍵列印 PDF。

---

## 涵蓋教材範圍（100% 全數整合）

1. `Introduction to Modern Cryptography - Historical Ciphers and Their Cryptanalysis` (Katz & Lindell Ch. 1)
2. `Introduction to Modern Cryptography - Perfectly Secret Encryption` (Katz & Lindell Ch. 2)
3. `1.2 The Provable Security Mindset.pdf` (劉子源教授講義)
4. `1.4 Pseudorandomness.pdf` (劉子源教授講義)
5. `1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf` (劉子源教授講義)
6. `Cyrptography.pdf` (The Joy of Cryptography by Mike Rosulek: Ch 0, 1, 2, 4, 5, 6, 7)

---

## 本機快速啟動

若要在本機離線閱讀或複習：
- 雙擊執行 `start_website.bat`：啟動互動複習平台。
- 雙擊執行 `start_notes.bat`：啟動精華筆記純閱讀手冊。

---

## 後續擴充指令

本專案具備完全資料驅動架構，若有新講義進來：
```powershell
# 自動掃描新 PDF 並生成草稿
python manage_content.py scan-pdfs

# 匯入新章節與題目
python manage_content.py add-module <file.json>
python manage_content.py add-quiz <file.json>

# 驗證資料結構完整性
python manage_content.py validate
```
