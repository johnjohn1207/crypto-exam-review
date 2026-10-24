# 現代與後量子密碼學導論：複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對「現代與後量子密碼學導論」設計的三模態線上複習與互動學習平台，完整收錄課程教材（Katz & Lindell、Mike Rosulek《The Joy of Cryptography》與劉子源教授講義），並針對「作業一」與「練習一」建立專屬考點雙軌白話解析庫。

支援電腦、平板與手機跨裝置無縫瀏覽，具備沉浸式純閱讀、互動實作與考前雙軌刷題三大入口：

- **🚀 線上互動複習平台（推薦題庫與模擬）**：[https://johnjohn1207.github.io/crypto-exam-review/](https://johnjohn1207.github.io/crypto-exam-review/)
- **📖 密碼學精華筆記手冊（無干擾純閱讀）**：[https://johnjohn1207.github.io/crypto-exam-review/notes.html](https://johnjohn1207.github.io/crypto-exam-review/notes.html)
- **🎯 考點精華與題型變化分析平台（雙軌白話全解）**：[https://johnjohn1207.github.io/crypto-exam-review/exam.html](https://johnjohn1207.github.io/crypto-exam-review/exam.html)

---

## 三模態閱讀與切換說明

平台提供三大獨立網頁，頂部導覽列皆具備三向無縫快速切換功能：

```
[線上互動平台 (index.html)] <===> [精華筆記手冊 (notes.html)] <===> [考點變化題全解 (exam.html)]
          \                                                                 /
           \=======================> [GitHub 原始碼庫] <====================/
```

1. **入口一：線上互動學習平台 (`index.html`)**
   - **8 大章節重點整理**：嚴格對應全部教材 PDF。
   - **四大互動演算實驗室（Playgrounds）**：Two-Time Pad 攻擊、Feistel 網路演示、Padding Oracle 操作台、IND-CPA 攻防棋盤。
   - **階梯式互動題目練習系統**：32 道深度精選題目。
   - **專業名詞速查辭典**：收錄核心密碼學原語與安全定義。

2. **入口二：密碼學精華筆記手冊 (`notes.html`)**
   - **純粹閱讀模式**：無答題與模擬器干擾，專注於長文閱讀與考前通讀。
   - **智慧型 Callout 卡片分層**：理論定義、攻防分析、考試易錯陷阱。
   - **三種護眼閱讀主題**：深色模式（Dark）、羊皮紙紙張暖色（Sepia）、純白極簡（Light）。
   - **閱讀輔助工具**：字級調整、吸頂閱讀進度條、全文即時檢索、一鍵列印 PDF。

3. **入口三：密碼學考點精華與題型變化分析平台 (`exam.html`)**
   - **作業一與練習一 100% 全題解**：收錄作業一 10 小題 + 練習一 34 題 + 10 核心定理 + 6 大考題變形，共 60 筆完整模組。
   - **雙軌式解析體系**：
     - 【白話大腦模型】：直覺生活類比與代數破綻剖析。
     - 【嚴謹數學證明】：符合考試作答之 formal proof 與區分者演算法。
     - 【考場避坑指引】：點出失分盲點與得分關鍵。
   - **多維度控制台**：
     - 四大視角切換：雙軌並列、白話優先、證明優先、自我測驗遮罩模式。
     - 即時章節篩選器與關鍵字過濾引擎。

---

## 涵蓋教材範圍（100% 全數整合）

1. `Introduction to Modern Cryptography - Historical Ciphers and Their Cryptanalysis` (Katz & Lindell Ch. 1)
2. `Introduction to Modern Cryptography - Perfectly Secret Encryption` (Katz & Lindell Ch. 2)
3. `1.2 The Provable Security Mindset.pdf` (劉子源教授講義)
4. `1.4 Pseudorandomness.pdf` (劉子源教授講義)
5. `1.5 Chosen-Plaintext and Chosen-Ciphertext Attacks.pdf` (劉子源教授講義)
6. `Cyrptography.pdf` (The Joy of Cryptography by Mike Rosulek: Ch 0, 1, 2, 4, 5, 6, 7)
7. `作業一.pdf` (Homework 1 - 完善保密、不可區分性、PRG/PRF、CPA/CCA 認證加密)
8. `練習一.pdf` (Practice 1 - 選擇題 13 題 + 簡答題 13 題 + 課本習題 8 題，共 34 題)

---

## 本機快速啟動

若要在本機離線閱讀或複習：
- 雙擊執行 `start_website.bat`：啟動互動複習平台。
- 雙擊執行 `start_notes.bat`：啟動精華筆記純閱讀手冊。
- 雙擊執行 `start_exam.bat`：啟動考點精華與雙軌題型分析平台。

---

## 後續擴充指令

本專案具備完全資料驅動架構，若有新講義進來：
```powershell
# 自動掃描新 PDF 並生成草稿
python manage_content.py scan-pdfs

# 匯入新章節與題目
python manage_content.py add-module <file.json>
python manage_content.py add-quiz <file.json>

# 重新建置考試資料庫與頁面
python build_exam_data.py
python build_exam_html.py
python update_all_navs.py

# 驗證資料結構完整性
python manage_content.py validate
python test_exam_system.py
```
