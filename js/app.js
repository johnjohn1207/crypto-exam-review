// ==========================================
// Cryptography Learning Platform - Main App
// ==========================================

const AppState = {
    currentTab: 'summaries', // 'summaries' | 'playgrounds' | 'quizzes' | 'glossary'
    currentModuleId: (typeof MODULES_DATA !== 'undefined' && MODULES_DATA.length > 0) ? MODULES_DATA[0].id : 'mod-joy-0',
    currentPlayground: 'ttp', // 'ttp' | 'feistel' | 'po' | 'sg'
    quizFilterModule: 'all',
    quizOnlyMistakes: false,
    userAnswers: {}, // { questionId: { selected: number, isCorrect: boolean } }
    readModules: new Set(),

    loadStorage() {
        try {
            const savedAnswers = localStorage.getItem('crypto_user_answers');
            if (savedAnswers) this.userAnswers = JSON.parse(savedAnswers);
            const savedReads = localStorage.getItem('crypto_read_modules');
            if (savedReads) this.readModules = new Set(JSON.parse(savedReads));
        } catch (e) {
            console.error('Failed to load storage', e);
        }
    },

    saveStorage() {
        try {
            localStorage.setItem('crypto_user_answers', JSON.stringify(this.userAnswers));
            localStorage.setItem('crypto_read_modules', JSON.stringify([...this.readModules]));
        } catch (e) {
            console.error('Failed to save storage', e);
        }
    }
};

// --- Math Rendering with KaTeX ---
function triggerKaTeX(containerId) {
    const el = containerId ? document.getElementById(containerId) : document.body;
    if (!el || typeof renderMathInElement === 'undefined') return;
    try {
        renderMathInElement(el, {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false }
            ],
            throwOnError: false
        });
    } catch (err) {
        console.warn('KaTeX render warning:', err);
    }
}

// --- Navigation Controller ---
function switchTab(tabId) {
    AppState.currentTab = tabId;

    // Update Tab Buttons UI
    document.querySelectorAll('.nav-tab-btn').forEach(btn => {
        const target = btn.dataset.tab;
        if (target === tabId) {
            btn.classList.add('border-cyan-500', 'text-cyan-400', 'bg-slate-800/80');
            btn.classList.remove('border-transparent', 'text-slate-400');
        } else {
            btn.classList.remove('border-cyan-500', 'text-cyan-400', 'bg-slate-800/80');
            btn.classList.add('border-transparent', 'text-slate-400');
        }
    });

    // Update Views
    document.querySelectorAll('.tab-view').forEach(view => {
        view.classList.add('hidden');
    });

    const activeView = document.getElementById(`view-${tabId}`);
    if (activeView) activeView.classList.remove('hidden');

    if (tabId === 'summaries') {
        renderSidebarModules();
        renderModuleContent();
    } else if (tabId === 'playgrounds') {
        renderPlaygroundsNav();
        if (window.initPlaygrounds) window.initPlaygrounds();
    } else if (tabId === 'quizzes') {
        renderQuizFilters();
        renderQuizList();
    } else if (tabId === 'glossary') {
        renderGlossary();
    }

    triggerKaTeX();
}

// ==========================================
// 1. Module Summaries Rendering
// ==========================================
function renderSidebarModules() {
    const container = document.getElementById('summaries-module-list');
    if (!container) return;

    container.innerHTML = MODULES_DATA.map(mod => {
        const isActive = mod.id === AppState.currentModuleId;
        const isRead = AppState.readModules.has(mod.id);
        return `
            <button onclick="selectModule('${mod.id}')"
                class="w-full text-left p-3 rounded-lg text-xs transition border flex items-center justify-between ${
                    isActive 
                    ? 'bg-cyan-950/40 border-cyan-500/50 text-cyan-200' 
                    : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
                }">
                <div class="flex items-center gap-2.5">
                    <span class="font-mono font-bold text-xs ${isActive ? 'text-cyan-400' : 'text-slate-500'}">${mod.number}</span>
                    <span class="font-medium">${mod.title}</span>
                </div>
                ${isRead ? '<span class="text-[10px] bg-emerald-950/60 text-emerald-400 px-1.5 py-0.5 rounded border border-emerald-800/50 font-sans">已研讀</span>' : ''}
            </button>
        `;
    }).join('');
}

function selectModule(modId) {
    AppState.currentModuleId = modId;
    AppState.readModules.add(modId);
    AppState.saveStorage();
    renderSidebarModules();
    renderModuleContent();
    triggerKaTeX('module-content-area');
    if (window.innerWidth < 1024) {
        document.getElementById('module-content-area')?.scrollIntoView({ behavior: 'smooth' });
    }
}

function renderModuleContent() {
    const container = document.getElementById('module-content-area');
    if (!container) return;

    const mod = MODULES_DATA.find(m => m.id === AppState.currentModuleId);
    if (!mod) return;

    container.innerHTML = `
        <div class="space-y-6">
            <!-- Header Header -->
            <div class="border-b border-slate-800 pb-4">
                <div class="flex flex-wrap items-center justify-between gap-2 mb-1">
                    <span class="text-xs font-mono font-bold px-2 py-0.5 bg-cyan-950 text-cyan-400 border border-cyan-800 rounded">
                        MODULE ${mod.number}
                    </span>
                    <span class="text-xs text-slate-500 font-sans">
                        教材來源： ${mod.source}
                    </span>
                </div>
                <h2 class="text-2xl font-bold text-white tracking-wide mt-2">${mod.title}</h2>
                <div class="text-sm text-cyan-300 font-mono mt-0.5">${mod.subtitle}</div>
                <p class="text-slate-300 text-sm mt-3 bg-slate-900/80 border border-slate-800 p-3.5 rounded-lg leading-relaxed">
                    ${mod.summary}
                </p>
            </div>

            <!-- Sections Detail -->
            <div class="space-y-6">
                ${mod.sections.map((sec, idx) => `
                    <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-5 shadow-lg">
                        <h3 class="text-base font-bold text-cyan-300 flex items-center gap-2 border-b border-slate-800/80 pb-2.5 mb-3.5">
                            <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                            ${sec.title}
                        </h3>
                        <div class="space-y-2.5 text-sm text-slate-300 leading-relaxed font-sans">
                            ${sec.content.map(p => {
                                // Parse Markdown bold **...**
                                let html = p.replace(/\*\*(.*?)\*\*/g, '<strong class="text-white font-semibold">$1</strong>');
                                // Bullet item
                                if (html.startsWith('- ')) {
                                    return `<div class="pl-4 relative before:content-['•'] before:absolute before:left-0 before:text-cyan-500">${html.substring(2)}</div>`;
                                }
                                return `<p>${html}</p>`;
                            }).join('')}
                        </div>
                    </div>
                `).join('')}
            </div>

            <!-- Next Module Prompt -->
            <div class="pt-4 flex justify-between items-center border-t border-slate-800">
                <button onclick="switchTab('quizzes'); setQuizFilter('${mod.id}');"
                    class="bg-indigo-600 hover:bg-indigo-500 text-white text-xs px-4 py-2 rounded-lg font-medium transition flex items-center gap-1.5 shadow">
                    <span>前往本章專屬題庫練習</span> →
                </button>
            </div>
        </div>
    `;

    triggerKaTeX('module-content-area');
}

// ==========================================
// 2. Playgrounds Nav & Tab Switcher
// ==========================================
function renderPlaygroundsNav() {
    const container = document.getElementById('playground-tabs-bar');
    const contentArea = document.getElementById('playground-content-container');
    if (!container || !window.PLAYGROUNDS_REGISTRY) return;

    // Render Tab Buttons
    container.innerHTML = window.PLAYGROUNDS_REGISTRY.map(t => {
        const isActive = t.id === AppState.currentPlayground;
        return `
            <button onclick="selectPlayground('${t.id}')"
                class="px-3.5 py-2 text-xs font-medium rounded-lg transition border ${
                    isActive
                    ? 'bg-cyan-950 border-cyan-500 text-cyan-300 shadow'
                    : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }">
                ${t.title}
            </button>
        `;
    }).join('');

    // Render Dynamic Content Panels
    if (contentArea) {
        contentArea.innerHTML = window.PLAYGROUNDS_REGISTRY.map(t => `
            <div id="panel-${t.id}" class="playground-panel ${t.id === AppState.currentPlayground ? '' : 'hidden'}">
                <div id="${t.containerId}"></div>
            </div>
        `).join('');
    }
}

function selectPlayground(pgId) {
    AppState.currentPlayground = pgId;
    renderPlaygroundsNav();
    const activePg = window.PLAYGROUNDS_REGISTRY?.find(p => p.id === pgId);
    if (activePg && typeof activePg.init === 'function') {
        activePg.init();
    }
}

// ==========================================
// 3. Quiz Engine & Diagnostic Logic
// ==========================================
function renderQuizFilters() {
    const container = document.getElementById('quiz-filter-container');
    if (!container) return;

    // Calculate score & stats
    const totalQuestions = QUIZ_DATA.length;
    const answeredCount = Object.keys(AppState.userAnswers).length;
    let correctCount = 0;
    Object.values(AppState.userAnswers).forEach(a => {
        if (a.isCorrect) correctCount++;
    });

    const accuracy = answeredCount > 0 ? ((correctCount / answeredCount) * 100).toFixed(0) : 0;

    container.innerHTML = `
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-4">
            <!-- Stats Bar -->
            <div>
                <div class="flex justify-between items-center text-xs mb-1.5">
                    <span class="text-slate-400">總答題進度</span>
                    <span class="font-mono font-bold text-cyan-400">${answeredCount} / ${totalQuestions} (${accuracy}% 正確率)</span>
                </div>
                <div class="w-full bg-slate-950 h-2 rounded-full overflow-hidden border border-slate-800">
                    <div class="bg-gradient-to-r from-cyan-500 to-emerald-500 h-full transition-all duration-300"
                        style="width: ${(answeredCount / totalQuestions) * 100}%"></div>
                </div>
            </div>

            <!-- Module Filter Chips -->
            <div>
                <label class="block text-slate-400 text-xs font-semibold mb-2">章節範圍篩選</label>
                <div class="flex flex-wrap gap-1.5">
                    <button onclick="setQuizFilter('all')"
                        class="px-2.5 py-1 text-xs rounded border transition ${
                            AppState.quizFilterModule === 'all'
                            ? 'bg-cyan-900/60 border-cyan-500 text-cyan-200 font-bold'
                            : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
                        }">
                        全部章節 (24 題)
                    </button>
                    ${MODULES_DATA.map(m => `
                        <button onclick="setQuizFilter('${m.id}')"
                            class="px-2.5 py-1 text-xs rounded border transition ${
                                AppState.quizFilterModule === m.id
                                ? 'bg-cyan-900/60 border-cyan-500 text-cyan-200 font-bold'
                                : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
                            }">
                            ${m.number} ${m.title.substring(0, 4)}...
                        </button>
                    `).join('')}
                </div>
            </div>

            <!-- Mistakes Toggle -->
            <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                <button onclick="toggleMistakesOnly()"
                    class="text-xs px-3 py-1.5 rounded-lg border transition flex items-center gap-1.5 ${
                        AppState.quizOnlyMistakes
                        ? 'bg-rose-950 border-rose-500 text-rose-300 font-bold'
                        : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
                    }">
                    <span>只顯示答錯之題目 (錯題本)</span>
                </button>
                <button onclick="resetAllQuizProgress()" class="text-xs text-slate-500 hover:text-slate-300 transition">
                    清除作答紀錄
                </button>
            </div>
        </div>
    `;
}

function setQuizFilter(modId) {
    AppState.quizFilterModule = modId;
    AppState.quizOnlyMistakes = false;
    renderQuizFilters();
    renderQuizList();
    triggerKaTeX('quiz-list-container');
}

function toggleMistakesOnly() {
    AppState.quizOnlyMistakes = !AppState.quizOnlyMistakes;
    renderQuizFilters();
    renderQuizList();
    triggerKaTeX('quiz-list-container');
}

function resetAllQuizProgress() {
    if (confirm('確定要清除所有測驗作答紀錄嗎？')) {
        AppState.userAnswers = {};
        AppState.saveStorage();
        renderQuizFilters();
        renderQuizList();
    }
}

function renderQuizList() {
    const container = document.getElementById('quiz-list-container');
    if (!container) return;

    let filtered = QUIZ_DATA.filter(q => {
        if (AppState.quizFilterModule !== 'all' && q.moduleId !== AppState.quizFilterModule) return false;
        if (AppState.quizOnlyMistakes) {
            const ans = AppState.userAnswers[q.id];
            return ans && !ans.isCorrect;
        }
        return true;
    });

    if (filtered.length === 0) {
        container.innerHTML = `
            <div class="p-8 text-center text-slate-500 bg-slate-900 border border-slate-800 rounded-xl">
                ${AppState.quizOnlyMistakes ? '太棒了！目前沒有任何錯誤題目需要複習。' : '查無符合條件的題目。'}
            </div>
        `;
        return;
    }

    container.innerHTML = filtered.map((q, idx) => {
        const userAnswer = AppState.userAnswers[q.id];
        const isAnswered = userAnswer !== undefined;
        const isCorrect = isAnswered && userAnswer.isCorrect;

        return `
            <div class="bg-slate-900 border rounded-xl p-5 transition space-y-4 shadow-lg ${
                !isAnswered 
                ? 'border-slate-800' 
                : isCorrect 
                    ? 'border-emerald-500/60 bg-slate-900/90' 
                    : 'border-rose-500/60 bg-slate-900/90'
            }">
                <!-- Question Header -->
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-800 text-cyan-300 border border-slate-700">
                            Q${idx + 1}
                        </span>
                        <span class="text-xs font-semibold px-2 py-0.5 rounded bg-indigo-950 text-indigo-300 border border-indigo-800">
                            ${q.category}
                        </span>
                    </div>
                    <div class="text-xs text-slate-500">
                        ${isAnswered ? (isCorrect ? '<span class="text-emerald-400 font-bold">✔ 答對</span>' : '<span class="text-rose-400 font-bold">✘ 答錯</span>') : '尚未作答'}
                    </div>
                </div>

                <!-- Question Text -->
                <div class="text-sm text-slate-100 font-medium leading-relaxed">
                    ${q.question}
                </div>

                <!-- Options -->
                <div class="space-y-2">
                    ${q.options.map((opt, optIdx) => {
                        let btnStyle = "bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-800/80";
                        if (isAnswered) {
                            if (optIdx === q.answer) {
                                btnStyle = "bg-emerald-950/80 border-emerald-500 text-emerald-200 font-semibold";
                            } else if (optIdx === userAnswer.selected) {
                                btnStyle = "bg-rose-950/80 border-rose-500 text-rose-200";
                            } else {
                                btnStyle = "bg-slate-950/40 border-slate-900 text-slate-600 opacity-60";
                            }
                        }
                        return `
                            <button onclick="handleOptionSelect('${q.id}', ${optIdx})"
                                ${isAnswered ? 'disabled' : ''}
                                class="w-full text-left p-3 rounded-lg border text-xs leading-relaxed transition flex items-start gap-3 ${btnStyle}">
                                <span class="font-mono font-bold text-xs uppercase px-1.5 py-0.5 rounded bg-slate-900 border border-slate-800 shrink-0">
                                    ${String.fromCharCode(65 + optIdx)}
                                </span>
                                <span>${opt}</span>
                            </button>
                        `;
                    }).join('')}
                </div>

                <!-- Explanation Section -->
                ${isAnswered ? `
                    <div class="mt-4 pt-3 border-t border-slate-800 space-y-2.5 text-xs">
                        <div class="p-3 bg-slate-950 rounded-lg border border-slate-800 text-slate-300 leading-relaxed">
                            <strong class="text-cyan-400 font-sans block mb-1">【詳細推導與解題邏輯】</strong>
                            ${q.explanation}
                        </div>
                        <div class="p-3 bg-amber-950/20 rounded-lg border border-amber-900/40 text-amber-200/90 leading-relaxed">
                            <strong class="text-amber-400 font-sans block mb-1">【常見混淆觀念剖析】</strong>
                            ${q.pitfalls}
                        </div>
                        <div class="text-[11px] text-slate-500 text-right">
                            出處標註：${q.reference}
                        </div>
                    </div>
                ` : ''}
            </div>
        `;
    }).join('');

    triggerKaTeX('quiz-list-container');
}

function handleOptionSelect(qId, selectedIdx) {
    const q = QUIZ_DATA.find(item => item.id === qId);
    if (!q) return;

    const isCorrect = (selectedIdx === q.answer);
    AppState.userAnswers[qId] = {
        selected: selectedIdx,
        isCorrect: isCorrect
    };
    AppState.saveStorage();

    renderQuizFilters();
    renderQuizList();
    triggerKaTeX('quiz-list-container');
}

// ==========================================
// 4. Glossary Logic
// ==========================================
function renderGlossary() {
    const container = document.getElementById('glossary-content-area');
    if (!container) return;

    const searchKeyword = (document.getElementById('glossary-search-input')?.value || '').toLowerCase().trim();

    const filtered = GLOSSARY_DATA.filter(item => {
        if (!searchKeyword) return true;
        return item.term.toLowerCase().includes(searchKeyword) ||
               item.chinese.toLowerCase().includes(searchKeyword) ||
               item.category.toLowerCase().includes(searchKeyword) ||
               item.definition.toLowerCase().includes(searchKeyword);
    });

    container.innerHTML = `
        <div class="space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                <div class="relative w-full md:w-80">
                    <input type="text" id="glossary-search-input" value="${searchKeyword}" placeholder="搜尋術語（如 PRG, IND-CPA, OTP）..."
                        class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500">
                </div>
                <div class="text-xs text-slate-400">
                    收錄共 <span class="text-cyan-400 font-mono font-bold">${GLOSSARY_DATA.length}</span> 項密碼學核心定義
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                ${filtered.map(item => `
                    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow space-y-2">
                        <div class="flex items-center justify-between border-b border-slate-800/80 pb-2">
                            <div>
                                <h4 class="text-sm font-bold text-cyan-300 font-mono">${item.term}</h4>
                                <div class="text-xs text-slate-400 font-sans">${item.chinese}</div>
                            </div>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-400 font-medium">
                                ${item.category}
                            </span>
                        </div>
                        <p class="text-xs text-slate-300 leading-relaxed font-sans">
                            ${item.definition}
                        </p>
                        <div class="pt-2 text-[11px] text-amber-300/80 bg-amber-950/20 p-2 rounded border border-amber-900/30">
                            <strong>防錯備註：</strong>${item.pitfall}
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    document.getElementById('glossary-search-input')?.addEventListener('input', () => {
        renderGlossary();
        triggerKaTeX('glossary-content-area');
    });

    triggerKaTeX('glossary-content-area');
}

// Global initialization
document.addEventListener('DOMContentLoaded', () => {
    AppState.loadStorage();
    switchTab('summaries');
});
