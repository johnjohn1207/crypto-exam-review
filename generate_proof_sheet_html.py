# -*- coding: utf-8 -*-
"""
Generate proof_sheet.html (期中考必考形式證明精華一覽表).
"""
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="zh-TW" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>期中考必考形式證明精華一覽表 | 現代密碼學（範圍至 1-5 Section 1）</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                            900: '#312e81',
                        }
                    },
                    fontFamily: {
                        mono: ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
                        sans: ['"Inter"', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Noto Sans TC"', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- KaTeX CSS & JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

    <style>
        .katex { font-size: 1.05em; }
        .katex-display { margin: 0.8em 0; overflow-x: auto; overflow-y: hidden; padding-bottom: 4px; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
        .proof-code-block {
            font-family: "JetBrains Mono", monospace;
            white-space: pre-wrap;
            word-break: break-word;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-indigo-500 selection:text-white">

    <!-- 全域頂部導覽列 -->
    <header class="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row md:items-center justify-between py-2.5 md:py-0 md:h-16 gap-2.5 md:gap-4">
            <div class="flex items-center gap-3">
                <a href="index.html" class="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-600 to-indigo-600 flex items-center justify-center font-bold text-white shadow-md font-mono text-sm shrink-0">
                    Ψ
                </a>
                <div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight flex items-center gap-2">
                        現代與後量子密碼學導論
                        <span class="text-[10px] font-mono font-medium px-2 py-0.5 rounded-full bg-amber-950 text-amber-300 border border-amber-800 hidden sm:inline-block">
                            考試範圍：截至 1-5 Section 1
                        </span>
                    </h1>
                    <p class="text-[11px] text-slate-400 font-mono hidden md:block">Master Cryptographic Proofs Cheat Sheet</p>
                </div>
            </div>

            <!-- 跨頁整合導覽列 -->
            <nav id="site-nav" class="flex items-center gap-1.5 text-xs overflow-x-auto no-scrollbar py-0.5">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至互動實驗室">
                    <span>互動實驗室</span>
                </a>
                <a href="notes.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至講義筆記">
                    <span>講義筆記</span>
                </a>
                <a href="exam.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至考點變化題">
                    <span>考點與變化題</span>
                </a>
                <a href="homework_practice.html" class="px-2.5 py-1.5 rounded-lg border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center gap-1 shrink-0" title="切換至作業與練習全解">
                    <span>作業練習全解</span>
                </a>
                <a href="proof_sheet.html" class="px-2.5 py-1.5 rounded-lg border border-amber-500/60 bg-amber-950/80 text-amber-200 font-semibold transition flex items-center gap-1 shadow-sm shrink-0" title="當前頁面：必考形式證明一覽表">
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
                    <span>證明一覽表</span>
                </a>
                <a href="https://github.com/johnjohn1207/crypto-exam-review" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white transition flex items-center shrink-0 ml-1" title="在 GitHub 查看原始碼">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </a>
            </nav>
        </div>
    </header>

    <!-- 專題 Hero 橫幅 -->
    <section class="bg-gradient-to-b from-amber-950/30 via-slate-900 to-slate-950 border-b border-slate-800/80 px-4 py-8">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div class="space-y-2">
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-mono">
                    <span>📐 期中考必備武器庫</span>
                    <span class="text-slate-600">|</span>
                    <span>嚴格限定至 1-5 Section 1</span>
                    <span class="text-slate-600">|</span>
                    <span class="text-emerald-400 font-bold">27 題核心證明歸納</span>
                </div>
                <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                    期中考必考形式證明精華一覽表
                </h2>
                <p class="text-slate-400 text-sm max-w-3xl leading-relaxed">
                    本一覽表專門針對考試中佔分最高的形式化證明題（Formal Proofs）進行結構化整理。已依照出題範圍精確裁切至<strong>投影片 1-5 Section 1（Ch. 1, 2, 4, 5, 6, 7, 8）</strong>，並完全排除尚未教授之 Ch. 9（選擇密文攻擊 CCA、Padding Oracle、認證加密 AE）等補充題材，防止備考誤導。
                </p>
            </div>

            <!-- 數據統計看板 -->
            <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-2 lg:grid-cols-4 gap-2.5 shrink-0 text-center font-mono">
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">收錄證明題</div>
                    <div class="text-xl font-bold text-amber-400">27</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">考試邊界</div>
                    <div class="text-xl font-bold text-indigo-400">1.5 Sec 1</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">排除非範圍</div>
                    <div class="text-xl font-bold text-rose-400">100%</div>
                </div>
                <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-xl shadow-sm">
                    <div class="text-xs text-slate-400">形式化推導</div>
                    <div class="text-xl font-bold text-cyan-400">LaTeX</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 控制面板：章節篩選、證明技術分類、表格/卡片視角與即時搜尋 -->
    <section class="bg-slate-900/90 border-b border-slate-800 sticky top-16 z-40 px-4 py-3 shadow-md">
        <div class="max-w-7xl mx-auto flex flex-col gap-3">
            
            <!-- 第一排：章節過濾標籤與檢視視角模式切換 -->
            <div class="flex flex-wrap items-center justify-between gap-3">
                <!-- 章節標籤篩選 -->
                <div class="flex flex-wrap items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs">
                    <button onclick="setChapterFilter('all')" id="chap-all" class="chap-btn px-3 py-1.5 rounded-lg font-medium transition bg-amber-600 text-white shadow-sm">
                        全部章節證明 <span id="count-all" class="text-[10px] opacity-80">(27)</span>
                    </button>
                    <button onclick="setChapterFilter('ch1-2')" id="chap-ch1-2" class="chap-btn px-3 py-1.5 rounded-lg font-medium transition text-slate-400 hover:text-white">
                        Ch 1-2 完善保密與函式庫 <span id="count-ch1-2" class="text-[10px] opacity-80">(13)</span>
                    </button>
                    <button onclick="setChapterFilter('ch4-5')" id="chap-ch4-5" class="chap-btn px-3 py-1.5 rounded-lg font-medium transition text-slate-400 hover:text-white">
                        Ch 4-5 計算安全與 PRG <span id="count-ch4-5" class="text-[10px] opacity-80">(3)</span>
                    </button>
                    <button onclick="setChapterFilter('ch6-7')" id="chap-ch6-7" class="chap-btn px-3 py-1.5 rounded-lg font-medium transition text-slate-400 hover:text-white">
                        Ch 6-7 PRF/PRP 與 Feistel <span id="count-ch6-7" class="text-[10px] opacity-80">(6)</span>
                    </button>
                    <button onclick="setChapterFilter('ch8')" id="chap-ch8" class="chap-btn px-3 py-1.5 rounded-lg font-medium transition text-slate-400 hover:text-white">
                        Ch 8 選擇明文安全 CPA <span id="count-ch8" class="text-[10px] opacity-80">(5)</span>
                    </button>
                </div>

                <!-- 視角切換：矩陣速記對照表 vs 詳細證明卡片 -->
                <div class="flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs shrink-0">
                    <span class="text-slate-500 text-[11px] px-1.5 font-mono">展示模式:</span>
                    <button onclick="setViewLayout('table')" id="layout-table" class="layout-btn px-2.5 py-1 rounded-lg transition bg-amber-600 text-white font-medium" title="精華矩陣一覽表（快速橫向比較）">
                        📊 矩陣一覽表
                    </button>
                    <button onclick="setViewLayout('cards')" id="layout-cards" class="layout-btn px-2.5 py-1 rounded-lg transition text-slate-400 hover:text-white" title="詳細推導卡片（逐步展開推導式）">
                        🗂️ 詳細推導卡片
                    </button>
                </div>
            </div>

            <!-- 第二排：證明手法篩選與即時搜尋 -->
            <div class="flex flex-wrap items-center justify-between gap-3 pt-1 border-t border-slate-800/60">
                <!-- 證明技術標籤 -->
                <div class="flex items-center gap-1 text-xs overflow-x-auto no-scrollbar py-0.5">
                    <span class="text-slate-500 text-[11px] font-mono shrink-0 mr-1">手法過濾:</span>
                    <button onclick="setTechFilter('all')" id="tech-all" class="tech-btn px-2.5 py-1 rounded-md text-xs font-medium transition bg-slate-800 text-white shrink-0">
                        全部手法
                    </button>
                    <button onclick="setTechFilter('contradiction')" id="tech-contradiction" class="tech-btn px-2.5 py-1 rounded-md text-xs font-medium transition text-slate-400 hover:text-white shrink-0">
                        反證法與空間極限
                    </button>
                    <button onclick="setTechFilter('distinguisher')" id="tech-distinguisher" class="tech-btn px-2.5 py-1 rounded-md text-xs font-medium transition text-slate-400 hover:text-white shrink-0">
                        區分者歸約與優勢
                    </button>
                    <button onclick="setTechFilter('differential')" id="tech-differential" class="tech-btn px-2.5 py-1 rounded-md text-xs font-medium transition text-slate-400 hover:text-white shrink-0">
                        差分不變量破壞
                    </button>
                    <button onclick="setTechFilter('hybrid')" id="tech-hybrid" class="tech-btn px-2.5 py-1 rounded-md text-xs font-medium transition text-slate-400 hover:text-white shrink-0">
                        混淆論證技術
                    </button>
                </div>

                <!-- 搜尋框 -->
                <div class="relative w-full sm:w-64 shrink-0">
                    <input type="text" id="search-input" oninput="handleSearch(this.value)" placeholder="搜尋命題、手法、區分者、定理..."
                        class="w-full bg-slate-950 border border-slate-700/80 rounded-xl px-3 py-1.5 pl-8 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-500 transition">
                    <svg class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                    </svg>
                    <button id="clear-search" onclick="clearSearch()" class="hidden absolute right-2.5 top-2 text-slate-500 hover:text-slate-300 text-xs">✕</button>
                </div>
            </div>
        </div>
    </section>

    <!-- 結果資訊列 -->
    <div class="max-w-7xl mx-auto px-4 py-3 w-full flex items-center justify-between text-xs text-slate-400 border-b border-slate-800/40 font-mono">
        <div id="filter-summary">
            正在顯示：<span class="text-amber-400 font-semibold" id="current-filter-desc">全部章節證明</span>
        </div>
        <div>
            共檢索到 <span class="text-white font-bold text-sm" id="result-count">27</span> 題必考證明
        </div>
    </div>

    <!-- 主展示區塊 -->
    <main class="max-w-7xl mx-auto px-4 py-6 w-full flex-grow">
        <!-- 視角 1：精華矩陣一覽表 (Table View) -->
        <div id="table-view-container" class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/60 shadow-xl">
            <table class="w-full text-left text-xs border-collapse">
                <thead>
                    <tr class="bg-slate-950 border-b border-slate-800 text-slate-400 font-mono">
                        <th class="py-3.5 px-4 font-semibold w-16 text-center">編號</th>
                        <th class="py-3.5 px-4 font-semibold w-36">主題與題號來源</th>
                        <th class="py-3.5 px-4 font-semibold w-28">章節</th>
                        <th class="py-3.5 px-4 font-semibold w-36">核心證明手法</th>
                        <th class="py-3.5 px-4 font-semibold">目標命題 (Proposition)</th>
                        <th class="py-3.5 px-4 font-semibold">關鍵推導步驟 (Key Steps)</th>
                        <th class="py-3.5 px-4 font-semibold w-32 text-center">操作</th>
                    </tr>
                </thead>
                <tbody id="proof-table-body" class="divide-y divide-slate-800/80">
                    <!-- Dynamic rendering -->
                </tbody>
            </table>
        </div>

        <!-- 視角 2：詳細卡片模式 (Card View) -->
        <div id="cards-view-container" class="hidden space-y-6">
            <!-- Dynamic rendering -->
        </div>

        <!-- 空結果提示 -->
        <div id="empty-state" class="hidden text-center py-16 space-y-4">
            <div class="text-4xl text-slate-600">🔍</div>
            <div class="text-slate-400 text-base">沒有找到符合條件的形式證明</div>
            <p class="text-slate-500 text-xs">請嘗試重設搜尋關鍵字或切換章節/手法分類</p>
            <button onclick="resetAllFilters()" class="px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white rounded-xl text-xs transition">
                重設所有篩選條件
            </button>
        </div>
    </main>

    <!-- 頁尾 -->
    <footer class="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-500 font-mono">
        <div class="max-w-7xl mx-auto px-4 space-y-2">
            <p>現代與後量子密碼學導論・期中考必考形式證明精華一覽表（範圍至 1-5 Section 1）</p>
            <p class="text-[11px] text-slate-600">Introduction to Modern Cryptography by Katz & Lindell | The Joy of Cryptography by Mike Rosulek</p>
        </div>
    </footer>

    <!-- 浮動置頂按鈕 -->
    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" id="back-to-top" class="fixed bottom-6 right-6 p-3 rounded-full bg-slate-800/90 hover:bg-amber-600 text-slate-300 hover:text-white border border-slate-700 shadow-xl transition-all opacity-0 pointer-events-none z-50">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
    </button>

    <!-- 資料腳本 -->
    <script src="js/proof_sheet_data.js"></script>

    <!-- 頁面邏輯腳本 -->
    <script>
        let currentChapter = 'all';    // 'all' | 'ch1-2' | 'ch4-5' | 'ch6-7' | 'ch8'
        let currentTech = 'all';       // 'all' | 'contradiction' | 'distinguisher' | 'differential' | 'hybrid'
        let currentLayout = 'table';   // 'table' | 'cards'
        let currentSearchQuery = '';

        document.addEventListener('DOMContentLoaded', () => {
            renderContent();
            updateCounts();
            setupScrollListener();
        });

        function setupScrollListener() {
            const btn = document.getElementById('back-to-top');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    btn.classList.remove('opacity-0', 'pointer-events-none');
                } else {
                    btn.classList.add('opacity-0', 'pointer-events-none');
                }
            });
        }

        function getFilteredProofs() {
            return PROOF_SHEET_DATA.filter(item => {
                // 1. 章節過濾
                if (currentChapter !== 'all' && item.category !== currentChapter) {
                    return false;
                }
                // 2. 手法過濾
                if (currentTech !== 'all') {
                    const tech = (item.technique || '').toLowerCase();
                    if (currentTech === 'contradiction' && !tech.includes('反證') && !tech.includes('界限')) return false;
                    if (currentTech === 'distinguisher' && !tech.includes('區分') && !tech.includes('優勢') && !tech.includes('測試')) return false;
                    if (currentTech === 'differential' && !tech.includes('差分') && !tech.includes('消除')) return false;
                    if (currentTech === 'hybrid' && !tech.includes('混淆') && !tech.includes('hybrid')) return false;
                }
                // 3. 關鍵字搜尋
                if (currentSearchQuery.trim() !== '') {
                    const q = currentSearchQuery.toLowerCase();
                    const titleMatch = (item.title || '').toLowerCase().includes(q);
                    const sourceMatch = (item.source || '').toLowerCase().includes(q);
                    const techMatch = (item.technique || '').toLowerCase().includes(q);
                    const targetMatch = (item.target || '').toLowerCase().includes(q);
                    const stepsMatch = (item.steps || []).join(' ').toLowerCase().includes(q);
                    const pitfallMatch = (item.pitfall || '').toLowerCase().includes(q);
                    if (!titleMatch && !sourceMatch && !techMatch && !targetMatch && !stepsMatch && !pitfallMatch) {
                        return false;
                    }
                }
                return true;
            });
        }

        function renderContent() {
            const filtered = getFilteredProofs();
            document.getElementById('result-count').textContent = filtered.length;

            const emptyState = document.getElementById('empty-state');
            const tableContainer = document.getElementById('table-view-container');
            const cardsContainer = document.getElementById('cards-view-container');

            if (filtered.length === 0) {
                tableContainer.classList.add('hidden');
                cardsContainer.classList.add('hidden');
                emptyState.classList.remove('hidden');
                return;
            }

            emptyState.classList.add('hidden');

            if (currentLayout === 'table') {
                tableContainer.classList.remove('hidden');
                cardsContainer.classList.add('hidden');
                renderTableView(filtered);
            } else {
                tableContainer.classList.add('hidden');
                cardsContainer.classList.remove('hidden');
                renderCardsView(filtered);
            }

            // 觸發 KaTeX 渲染
            const container = currentLayout === 'table' ? tableContainer : cardsContainer;
            if (window.renderMathInElement) {
                renderMathInElement(container, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false
                });
            }
        }

        // 渲染表格視角
        function renderTableView(items) {
            const tbody = document.getElementById('proof-table-body');
            tbody.innerHTML = items.map((item, idx) => `
                <tr class="hover:bg-slate-800/40 transition">
                    <td class="py-3 px-4 text-center font-mono text-slate-400 font-bold">${idx + 1}</td>
                    <td class="py-3 px-4">
                        <div class="font-bold text-white text-xs">${item.title}</div>
                        <div class="text-[10px] text-amber-300 font-mono mt-0.5">${item.source}</div>
                    </td>
                    <td class="py-3 px-4 font-mono">
                        <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-slate-800 text-slate-300 border border-slate-700">${item.chapter}</span>
                    </td>
                    <td class="py-3 px-4">
                        <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-amber-500/10 text-amber-300 border border-amber-500/30 font-mono">${item.technique}</span>
                    </td>
                    <td class="py-3 px-4 text-slate-300 text-xs font-sans leading-relaxed">
                        ${escapeHtml(item.target)}
                    </td>
                    <td class="py-3 px-4 text-slate-300 text-xs font-sans leading-relaxed">
                        <ol class="list-decimal list-inside space-y-1">
                            ${item.steps.slice(0, 3).map(s => `<li>${escapeHtml(s)}</li>`).join('')}
                            ${item.steps.length > 3 ? `<li class="text-slate-500 font-mono text-[11px]">...（共 ${item.steps.length} 步驟）</li>` : ''}
                        </ol>
                    </td>
                    <td class="py-3 px-4 text-center">
                        <button onclick="copyProofText('${item.id}')" class="px-2.5 py-1 rounded-lg text-[11px] font-mono bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition border border-slate-700 whitespace-nowrap">
                            📋 複製證明
                        </button>
                    </td>
                </tr>
            `).join('');
        }

        // 渲染卡片視角
        function renderCardsView(items) {
            const container = document.getElementById('cards-view-container');
            container.innerHTML = items.map(item => `
                <article class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-lg space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-2.5 pb-3 border-b border-slate-800/80">
                        <div class="flex items-center gap-2">
                            <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/30 font-mono">⚡ 形式證明</span>
                            <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300 border border-slate-700">${item.chapter}</span>
                            <span class="text-xs text-slate-400 font-mono">來源：${item.source}</span>
                        </div>
                        <button onclick="copyProofText('${item.id}')" class="px-2.5 py-1 rounded-lg text-xs font-mono bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition border border-slate-700">
                            📋 複製證明
                        </button>
                    </div>

                    <h3 class="text-lg font-bold text-white flex items-center gap-2">
                        <span>${item.title}</span>
                    </h3>

                    <!-- 目標命題與核心手法 -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                        <div class="md:col-span-2 bg-indigo-950/20 border-l-4 border-indigo-500 p-3 rounded-r-xl text-xs sm:text-sm">
                            <div class="font-bold text-indigo-300 font-mono mb-1">🎯 目標命題 (Formal Proposition)</div>
                            <div class="text-slate-200">${escapeHtml(item.target)}</div>
                        </div>
                        <div class="bg-amber-950/20 border-l-4 border-amber-500 p-3 rounded-r-xl text-xs sm:text-sm">
                            <div class="font-bold text-amber-300 font-mono mb-1">🛠️ 核心證明手法</div>
                            <div class="text-amber-200">${escapeHtml(item.technique)}</div>
                        </div>
                    </div>

                    <!-- 關鍵推導步驟 -->
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-xs sm:text-sm shadow-inner space-y-2">
                        <div class="font-bold text-indigo-300 font-mono flex items-center justify-between">
                            <span>📐 嚴謹形式推導步驟 (Step-by-Step Formal Proof)</span>
                            <span class="text-[10px] text-slate-500">LaTeX Supported</span>
                        </div>
                        <div class="proof-code-block text-slate-200 leading-relaxed space-y-1.5">
                            ${item.steps.map(s => `<p>${escapeHtml(s)}</p>`).join('')}
                        </div>
                    </div>

                    <!-- 演算法或破譯準則 -->
                    ${item.algorithm ? `
                    <div class="bg-cyan-950/20 border-l-4 border-cyan-500 p-3 rounded-r-xl text-xs sm:text-sm">
                        <div class="font-bold text-cyan-300 font-mono mb-1">⚙️ 攻擊區分者演算法或判定準則</div>
                        <div class="text-cyan-100 font-mono whitespace-pre-wrap">${escapeHtml(item.algorithm)}</div>
                    </div>` : ''}

                    <!-- 致命陷阱 -->
                    ${item.pitfall ? `
                    <div class="bg-rose-950/20 border-l-4 border-rose-500 p-3 rounded-r-xl text-xs sm:text-sm">
                        <div class="font-bold text-rose-300 font-mono mb-1">⚠️ 考試致命扣分陷阱 (Fatal Pitfall)</div>
                        <div class="text-rose-200">${escapeHtml(item.pitfall)}</div>
                    </div>` : ''}
                </article>
            `).join('');
        }

        function escapeHtml(str) {
            if (!str) return '';
            return str
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;");
        }

        function setChapterFilter(chap) {
            currentChapter = chap;
            document.querySelectorAll('.chap-btn').forEach(btn => {
                btn.classList.remove('bg-amber-600', 'text-white', 'shadow-sm');
                btn.classList.add('text-slate-400');
            });
            const activeBtn = document.getElementById(`chap-${chap}`);
            if (activeBtn) {
                activeBtn.classList.add('bg-amber-600', 'text-white', 'shadow-sm');
                activeBtn.classList.remove('text-slate-400');
            }
            updateFilterSummary();
            renderContent();
        }

        function setTechFilter(tech) {
            currentTech = tech;
            document.querySelectorAll('.tech-btn').forEach(btn => {
                btn.classList.remove('bg-slate-800', 'text-white');
                btn.classList.add('text-slate-400');
            });
            const activeBtn = document.getElementById(`tech-${tech}`);
            if (activeBtn) {
                activeBtn.classList.add('bg-slate-800', 'text-white');
                activeBtn.classList.remove('text-slate-400');
            }
            updateFilterSummary();
            renderContent();
        }

        function setViewLayout(layout) {
            currentLayout = layout;
            document.querySelectorAll('.layout-btn').forEach(btn => {
                btn.classList.remove('bg-amber-600', 'text-white', 'font-medium');
                btn.classList.add('text-slate-400');
            });
            const activeBtn = document.getElementById(`layout-${layout}`);
            if (activeBtn) {
                activeBtn.classList.add('bg-amber-600', 'text-white', 'font-medium');
                activeBtn.classList.remove('text-slate-400');
            }
            renderContent();
        }

        function handleSearch(val) {
            currentSearchQuery = val;
            const clearBtn = document.getElementById('clear-search');
            if (val.trim() !== '') {
                clearBtn.classList.remove('hidden');
            } else {
                clearBtn.classList.add('hidden');
            }
            updateFilterSummary();
            renderContent();
        }

        function clearSearch() {
            document.getElementById('search-input').value = '';
            handleSearch('');
        }

        function copyProofText(id) {
            const item = PROOF_SHEET_DATA.find(x => x.id === id);
            if (!item) return;

            const textToCopy = `【${item.title}】(${item.chapter}・${item.source})\\n\\n[核心手法]\\n${item.technique}\\n\\n[目標命題]\\n${item.target}\\n\\n[推導步驟]\\n${item.steps.join('\\n')}\\n\\n[演算法/準則]\\n${item.algorithm}\\n\\n[致命陷阱]\\n${item.pitfall}`;
            navigator.clipboard.writeText(textToCopy).then(() => {
                alert(`已成功複製【${item.title}】的完整形式證明至剪貼簿！`);
            }).catch(err => {
                console.error("複製失敗:", err);
            });
        }

        function resetAllFilters() {
            currentChapter = 'all';
            currentTech = 'all';
            currentSearchQuery = '';
            document.getElementById('search-input').value = '';
            document.getElementById('clear-search').classList.add('hidden');

            setChapterFilter('all');
            setTechFilter('all');
            renderContent();
        }

        function updateFilterSummary() {
            let parts = [];
            if (currentChapter === 'all') parts.push('全部章節證明');
            else if (currentChapter === 'ch1-2') parts.push('Ch 1-2 完善保密');
            else if (currentChapter === 'ch4-5') parts.push('Ch 4-5 計算安全');
            else if (currentChapter === 'ch6-7') parts.push('Ch 6-7 PRF/PRP');
            else if (currentChapter === 'ch8') parts.push('Ch 8 CPA 安全');

            if (currentTech !== 'all') {
                if (currentTech === 'contradiction') parts.push('反證法/界限');
                if (currentTech === 'distinguisher') parts.push('區分者歸約');
                if (currentTech === 'differential') parts.push('差分不變量');
                if (currentTech === 'hybrid') parts.push('混淆論證');
            }

            if (currentSearchQuery.trim() !== '') {
                parts.push(`包含關鍵字 "${currentSearchQuery.trim()}"`);
            }

            document.getElementById('current-filter-desc').textContent = parts.join(' ・ ');
        }

        function updateCounts() {
            const counts = {
                all: PROOF_SHEET_DATA.length,
                ch1_2: PROOF_SHEET_DATA.filter(x => x.category === 'ch1-2').length,
                ch4_5: PROOF_SHEET_DATA.filter(x => x.category === 'ch4-5').length,
                ch6_7: PROOF_SHEET_DATA.filter(x => x.category === 'ch6-7').length,
                ch8: PROOF_SHEET_DATA.filter(x => x.category === 'ch8').length
            };

            document.getElementById('count-all').textContent = `(${counts.all})`;
            document.getElementById('count-ch1-2').textContent = `(${counts.ch1_2})`;
            document.getElementById('count-ch4-5').textContent = `(${counts.ch4_5})`;
            document.getElementById('count-ch6-7').textContent = `(${counts.ch6_7})`;
            document.getElementById('count-ch8').textContent = `(${counts.ch8})`;
        }
    </script>
</body>
</html>
"""

with open("proof_sheet.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Successfully created proof_sheet.html!")
