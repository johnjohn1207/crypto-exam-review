# 現代與後量子密碼學導論：複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對現代與後量子密碼學課程所設計的四合一整合複習平台，收錄課程教材（Katz & Lindell、Mike Rosulek《The Joy of Cryptography》及投影片教材），並整合「作業一」與「練習一」建立全面題庫與嚴謹形式證明庫。

本平台提供四個主要入口，所有頁面皆具備全域導覽互通機制：

1. **核心互動學習平台 (`index.html`)**：
   - 8 大主題章節重點整理與名詞檢索。
   - 互動展示實驗室（Two-Time Pad 攻擊實驗、Feistel 網絡視覺化、Padding Oracle 逐步破解、IND-CPA 遊戲模擬）。
   - 20 題標準自我評測系統。

2. **精華筆記手冊 (`notes.html`)**：
   - 無干擾閱讀模式、深度 Callout 知識點標註（概念定義、重要定理、考試防錯）。
   - 支援深色（Dark）、羊皮紙米黃（Sepia）與明亮白（Light）主題切換。

3. **考點精華與變化題分析平台 (`exam.html`)**：
   - 10 大關鍵公式與定理深度剖析。
   - 6 大高頻進階變化題型演練（合數階模乘、雙區塊重複、BEAST 攻擊原型、Padding Oracle 破譯）。
   - 支援雙軌對照模式與刷題自測檢驗。

4. **作業一與練習一 獨立題目詳解與證明全觀念專頁 (`homework_practice.html`)**：
   - **44 題完整收錄**：作業一（10 題）+ 練習一 Part A 選擇題（13 題）+ 練習一 Part B 簡答論述（13 題）+ 練習一 Part C 課本進階證明（8 題）。
   - **27 題形式化證明專區（⚡ 形式證明題）**：零省略數學證明、區分者演算法（Distinguisher）、優勢計算（Advantage）與歸約推導（Reduction）。
   - **四層式架構解析**：每題均包含「題目原意與中文翻譯」、「核心觀念與定義定理」、「白話直觀思維」、「形式化嚴謹證明」與「考試評分防錯陷阱」。
   - **多維度控制**：支援「純證明題一鍵篩選」、章節分類過濾（Ch 1-2, Ch 4-5, Ch 6-7, Ch 8-9）、視角模式切換（雙軌、證明優先、核心觀念、刷題自測）與即時搜尋。

---

## 本地快速啟動

若要在本機離線瀏覽任一頁面，可直接雙擊對應批次檔：
- `start_website.bat`：啟動互動複習平台主頁。
- `start_notes.bat`：啟動精華講義閱讀頁面。
- `start_exam.bat`：啟動考點與題型變化分析平台。
- `start_hw_practice.bat`：啟動作業一與練習一題目詳解與形式證明獨立專頁。

---

## 資料結構維護與建置腳本

本專案具備完整資料管道，各模組可獨立建置：

```powershell
# 建置作業與練習專屬資料與獨立頁面
python scratch/build_hw_practice_system.py
python scratch/generate_hw_practice_page.py

# 同步四頁全域頂部導覽列
python update_all_navs.py

# 執行全系統驗證測試
python test_exam_system.py
```
