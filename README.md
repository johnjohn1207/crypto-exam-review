# 現代與後量子密碼學導論 複習暨互動學習平台

> Introduction to Modern and Post-quantum Cryptography Review Portal

本專案為針對「現代與後量子密碼學導論」設計的線上互動複習平台，支援手機與電腦跨裝置瀏覽。

- **線上網址（GitHub Pages）**：[https://johnjohn1207.github.io/crypto-exam-review/](https://johnjohn1207.github.io/crypto-exam-review/)

---

## 核心功能模組

1. **章節重點整理 (Chapter Summaries)**
   - 涵蓋可證明安全（Provable Security）、One-Time Pad、偽隨機性（PRG / PRF）、選擇明文與選擇密文攻擊（CPA / CCA）等核心觀念。
   - 內建 KaTeX 完整支援數學符號與安全性定義公式渲染。

2. **互動實驗室 (Interactive Playgrounds)**
   - Two-Time Pad 攻擊模擬：實作金鑰重複使用下的明文還原推導。
   - Feistel 結構運作模擬：視覺化展示輪函數與置換解密過程。

3. **互動題目練習 (Interactive Quizzes)**
   - 多題型觀念自測，具備答題即時反饋、錯題篩選與解析回顧。
   - 作答進度由瀏覽器端 LocalStorage 自動儲存。

4. **專業名詞檢索 (Glossary)**
   - 快速索引密碼學重要專有名詞、中英對照與防錯提醒。

---

## 技術架構

- **前端技術**：HTML5, Tailwind CSS (CDN), KaTeX (Math Rendering), Vanilla JavaScript (ES6+)
- **佈署平台**：GitHub Pages (靜態網站託管，全自動 HTTPS)
- **跨平台響應**：針對行動裝置（Mobile）與桌面端（Desktop）完成介面排版最佳化
