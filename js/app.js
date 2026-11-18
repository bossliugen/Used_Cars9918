/**
 * 台灣中古車實價趨勢與世代資料庫 - 白底藍框簡約版主程式
 */

/**
 * 台灣中古車實價趨勢與世代資料庫 - 白底藍框簡約版主程式
 */

const BRAND_LOGOS = {
  Toyota: `<svg viewBox="0 0 36 24" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="18" cy="12" rx="15" ry="10"/><ellipse cx="18" cy="12" rx="4.5" ry="9.5"/><ellipse cx="18" cy="8.5" rx="11" ry="4"/></svg>`,
  Honda: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="2" width="24" height="20" rx="4"/><path d="M8.5 6v12M19.5 6v12M8.5 12h11"/></svg>`,
  Ford: `<svg viewBox="0 0 38 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="19" cy="10" rx="17" ry="8"/><text x="19" y="13.5" text-anchor="middle" font-size="8.5" font-style="italic" font-weight="700" fill="currentColor" stroke="none">Ford</text></svg>`,
  Mazda: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="14" cy="12" rx="12" ry="9.5"/><path d="M4.5 9.5L14 14.5l9.5-5"/></svg>`,
  Nissan: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="14" cy="12" r="9.5"/><rect x="2" y="9" width="24" height="6" rx="1.5" fill="white"/></svg>`,
  Volkswagen: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10.5"/><path d="M6.5 6.5L11 16l2-4.5L15 16l4.5-9.5M8.5 5l4.5 7 4.5-7"/></svg>`,
  Subaru: `<svg viewBox="0 0 32 22" fill="none" stroke="currentColor" stroke-width="1.7"><ellipse cx="16" cy="11" rx="14" ry="9"/><path d="M9 11l2.5-2.5L14 11l-2.5 2.5zM18 7l1.5-1.5L21 7l-1.5 1.5zM21 12l1.5-1.5L24 12l-1.5 1.5z" fill="currentColor" stroke="none"/></svg>`,
  Hyundai: `<svg viewBox="0 0 34 22" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="17" cy="11" rx="14.5" ry="9"/><path d="M11 16l3.5-10M19.5 16L23 6M12.5 11.5l9-1"/></svg>`,
  Lexus: `<svg viewBox="0 0 32 24" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="16" cy="12" rx="13.5" ry="9.5"/><path d="M13 6.5L10 15.5h11"/></svg>`,
  "Mercedes-Benz": `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10.5"/><path d="M13 2.5V13m0 0l-8.8 5.2M13 13l8.8 5.2"/></svg>`,
  BMW: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10.5"/><circle cx="13" cy="13" r="6.5"/><path d="M13 6.5v13M6.5 13h13"/></svg>`,
  Suzuki: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16.5 3.5L6.5 10l9 4-6 4.5 10 4 0-5.5-8.5-3.5 5.5-4z"/></svg>`,
  Mitsubishi: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M14 3L17.5 9.5L14 15L10.5 9.5Z"/><path d="M14 15L21.5 15L24.5 21L17 21Z"/><path d="M14 15L6.5 15L3.5 21L11 21Z"/></svg>`,
  Kia: `<svg viewBox="0 0 36 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="18" cy="10" rx="16" ry="8"/><path d="M9 13V7m0 3l3.5-3M9 10l3.5 3M17 7v6M21.5 13L24 7l2.5 6"/></svg>`,
  Skoda: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10.5"/><path d="M7 14c3-5 8-5 12-1-4 0-7 2-9 5z"/></svg>`,
  Volvo: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="14" r="8"/><path d="M17.5 8.5L22 4m0 0h-4.5M22 4v4.5"/></svg>`,
  Luxgen: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 5v14h11"/><path d="M13 5c3 4 4 8 2 14"/></svg>`,
  MG: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.7"><polygon points="8,3 20,3 25,8 25,16 20,21 8,21 3,16 3,8"/><text x="14" y="15" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor" stroke="none">MG</text></svg>`,
  Tesla: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 7c5-2 11-2 16 0M13 8v13M8 10h10"/></svg>`,
  Audi: `<svg viewBox="0 0 40 20" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="9" cy="10" r="5.5"/><circle cx="16.5" cy="10" r="5.5"/><circle cx="24" cy="10" r="5.5"/><circle cx="31.5" cy="10" r="5.5"/></svg>`,
  Porsche: `<svg viewBox="0 0 24 26" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 4h16v10c0 5-8 9-8 9s-8-4-8-9V4z"/><path d="M4 10h16M12 4v18"/></svg>`,
  MINI: `<svg viewBox="0 0 36 22" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 8h9M24 8h9M4 12h7M25 12h7"/><circle cx="18" cy="11" r="6"/></svg>`,
  Peugeot: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M7 20l3-11 4-4 5 4-2 5-5 1 2 5z"/></svg>`,
  Infiniti: `<svg viewBox="0 0 32 22" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="16" cy="11" rx="13" ry="8"/><path d="M11 18L16 8l5 10"/></svg>`,
  "Land Rover": `<svg viewBox="0 0 34 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="17" cy="10" rx="15" ry="7.5"/><text x="17" y="12.5" text-anchor="middle" font-size="6.5" font-weight="700" fill="currentColor" stroke="none">LR</text></svg>`,
  SsangYong: `<svg viewBox="0 0 32 22" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="16" cy="11" rx="13" ry="8"/><path d="M10 11c2-4 10-4 12 0-2 4-10 4-12 0z"/></svg>`,
  CMC: `<svg viewBox="0 0 30 22" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="24" height="14" rx="3"/><text x="15" y="14" text-anchor="middle" font-size="8" font-weight="700" fill="currentColor" stroke="none">CMC</text></svg>`,
  Citroen: `<svg viewBox="0 0 26 24" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 12l7-6 7 6M6 18l7-6 7 6"/></svg>`,
  Daihatsu: `<svg viewBox="0 0 28 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 6h9a6 6 0 0 1 0 12H6V6z"/></svg>`,
  Opel: `<svg viewBox="0 0 30 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="15" cy="12" r="8"/><path d="M4 12h13l-3 3h12"/></svg>`,
  Renault: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="13,3 22,13 13,23 4,13"/><polygon points="13,7 18,13 13,19 8,13"/></svg>`,
  Fiat: `<svg viewBox="0 0 32 22" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="26" height="14" rx="4"/><text x="16" y="14" text-anchor="middle" font-size="8" font-weight="700" fill="currentColor" stroke="none">FIAT</text></svg>`,
  "Alfa Romeo": `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10"/><path d="M13 3v20M3 13h10"/></svg>`,
  Saab: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="13" cy="13" r="10"/><text x="13" y="15.5" text-anchor="middle" font-size="7" font-weight="700" fill="currentColor" stroke="none">SAAB</text></svg>`,
  Jaguar: `<svg viewBox="0 0 34 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 14c6-5 16-6 26-2-6 1-11 2-15 5"/></svg>`,
  Smart: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16 7a6 6 0 1 0 0 12"/><polygon points="18,10 23,13 18,16"/></svg>`,
  Jeep: `<svg viewBox="0 0 34 20" fill="none" stroke="currentColor" stroke-width="1.8"><text x="17" y="14" text-anchor="middle" font-size="10" font-weight="700" fill="currentColor" stroke="none">Jeep</text></svg>`,
  Maserati: `<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 4v18M7 9v5c0 2 6 3 6 3s6-1 6-3V9"/></svg>`,
};

function getBrandLogoSvg(brand, large = false) {
  const svg = BRAND_LOGOS[brand] || `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/></svg>`;
  return `<span class="${large ? "brand-icon-lg" : "brand-icon"}">${svg}</span>`;
}

const state = {
  db: null,
  brands: [],
  selectedBrand: null,
  selectedCarId: null,
  selectedYear: null,
  selectedTrimIdx: 0,
  chartMode: "price",
  entryMode: "manual", // 'manual' | 'finder'
  lastEntryMode: "manual",
  inAnalysis: false,
  activeDetailTab: "specs", // 'specs' | 'issues' | 'gens' | 'history' | 'sources'
  chart: null,
};

async function initApp() {
  state.chart = new MarketTrendChart("trendCanvas", "chartTooltip");

  try {
    const resp = await fetch("data/cars_db.json");
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    state.db = await resp.json();
  } catch (err) {
    document.getElementById("mainContainer").innerHTML = `
      <div class="card">
        <h2 style="color:#991B1B;">無法載入資料庫 (data/cars_db.json)</h2>
        <p style="margin-top:8px;color:#57534E;">請雙擊 <strong>啟動中古車分析網站.bat</strong> 或透過 GitHub Pages 開啟。</p>
      </div>
    `;
    return;
  }

  state.brands = [...new Set(state.db.cars.map((c) => c.brand))].sort((a, b) =>
    a.localeCompare(b, "en", { sensitivity: "base" })
  );
  document.getElementById("headerMetaChip").textContent =
    `${state.brands.length} 品牌 ・ ${state.db.meta.total_models} 車系 ・ ${state.db.meta.total_year_records} 筆年式`;

  renderBrandControls();
  renderRankingTable();
  bindEvents();

  // 初始化預設選單值（僅預先填入下拉選單，不主動顯示車輛分析畫面）
  const defaultCar = state.db.cars.find((c) => c.id === "ford-focus") || state.db.cars[0];
  selectBrand(defaultCar.brand, defaultCar.id);
  renderSmartFinder();
}

function bindEvents() {
  const dropdown = document.getElementById("brandDropdown");
  const dropdownBtn = document.getElementById("brandDropdownBtn");

  dropdownBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("open");
  });

  document.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove("open");
    }
  });

  document.getElementById("selectModel").addEventListener("change", (e) => {
    selectCar(e.target.value);
  });

  document.getElementById("selectYear").addEventListener("change", (e) => {
    state.selectedYear = parseInt(e.target.value, 10);
    state.selectedTrimIdx = 0;
    populateTrimSelect();
    renderAllCarViews();
  });

  document.getElementById("selectTrim").addEventListener("change", (e) => {
    state.selectedTrimIdx = parseInt(e.target.value, 10) || 0;
    renderAllCarViews();
  });

  document.getElementById("quickSearch").addEventListener("input", (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (!q) return;
    const match = state.db.cars.find(
      (c) =>
        c.brand.toLowerCase().includes(q) ||
        c.model.toLowerCase().includes(q) ||
        c.model_zh.toLowerCase().includes(q)
    );
    if (match) {
      selectBrand(match.brand, match.id);
    }
  });

  ["inputMileage", "selectCondition"].forEach((id) => {
    document.getElementById(id).addEventListener("input", () => {
      renderHeroAndKpis();
      renderCostAndMaintenance();
    });
    document.getElementById(id).addEventListener("change", () => {
      renderHeroAndKpis();
      renderCostAndMaintenance();
    });
  });

  ["selectAnnualKm", "selectInsurancePlan"].forEach((id) => {
    document.getElementById(id).addEventListener("change", renderCostAndMaintenance);
  });

  document.getElementById("btnModePrice").addEventListener("click", () => {
    state.chartMode = "price";
    updateChartLegendAndButtons();
    renderChart();
  });

  document.getElementById("btnModeResidual").addEventListener("click", () => {
    state.chartMode = "residual";
    updateChartLegendAndButtons();
    renderChart();
  });

  document.querySelectorAll(".page-tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      switchPage(btn.dataset.page);
    });
  });

  document.querySelectorAll(".detail-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.activeDetailTab = btn.dataset.tab;
      document.querySelectorAll(".detail-tab").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderDetailBody();
    });
  });

  document.querySelectorAll(".entry-mode-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      switchEntryMode(btn.dataset.entry);
    });
  });

  document.getElementById("btnEnterAnalysis").addEventListener("click", () => {
    enterAnalysisScreen("manual");
  });

  document.getElementById("btnBackToEntry").addEventListener("click", () => {
    backToEntryScreen();
  });

  document.getElementById("analysisSelectYear").addEventListener("change", (e) => {
    state.selectedYear = parseInt(e.target.value, 10);
    document.getElementById("selectYear").value = String(state.selectedYear);
    state.selectedTrimIdx = 0;
    populateTrimSelect();
    renderAllCarViews();
  });

  document.getElementById("analysisSelectTrim").addEventListener("change", (e) => {
    state.selectedTrimIdx = parseInt(e.target.value, 10) || 0;
    document.getElementById("selectTrim").value = String(state.selectedTrimIdx);
    renderAllCarViews();
  });

  ["finderGoal", "finderBody", "finderMaxCc", "finderTransmission", "finderPowertrain", "finderSort"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("change", renderSmartFinder);
  });
  document.getElementById("finderPowertrain")?.addEventListener("change", (e) => {
    const maxCcEl = document.getElementById("finderMaxCc");
    if (!maxCcEl) return;
    if (e.target.value === "ev") {
      maxCcEl.value = maxCcEl.options[0]?.value ?? "9999";
      maxCcEl.disabled = true;
    } else {
      maxCcEl.disabled = false;
    }
  });
  ["finderBudgetMin", "finderBudgetMax", "finderHpMin", "finderHpMax", "finderYearMin", "finderYearMax"].forEach((id) => {
    document.getElementById(id).addEventListener("input", renderSmartFinder);
    document.getElementById(id).addEventListener("change", renderSmartFinder);
  });
}

function switchEntryMode(mode) {
  state.entryMode = mode;
  document.querySelectorAll(".entry-mode-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.entry === mode);
  });
  document.querySelectorAll(".entry-panel").forEach((p) => {
    p.classList.toggle("active", p.id === `entry-${mode}`);
  });
  if (mode === "finder") {
    renderSmartFinder();
  }
}

function enterAnalysisScreen(sourceMode = "manual") {
  state.lastEntryMode = sourceMode;
  state.inAnalysis = true;
  document.getElementById("entryScreen").classList.add("hidden");
  document.getElementById("analysisScreen").classList.remove("hidden");
  syncAnalysisQuickSelectors();
  renderAllCarViews();
  switchPage("overview");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function backToEntryScreen() {
  state.inAnalysis = false;
  document.getElementById("analysisScreen").classList.add("hidden");
  document.getElementById("entryScreen").classList.remove("hidden");
  switchEntryMode(state.lastEntryMode || "manual");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function syncAnalysisQuickSelectors() {
  const mainYear = document.getElementById("selectYear");
  const mainTrim = document.getElementById("selectTrim");
  const anaYear = document.getElementById("analysisSelectYear");
  const anaTrim = document.getElementById("analysisSelectTrim");
  if (mainYear && anaYear) {
    anaYear.innerHTML = mainYear.innerHTML;
    anaYear.value = String(state.selectedYear);
  }
  if (mainTrim && anaTrim) {
    anaTrim.innerHTML = mainTrim.innerHTML;
    anaTrim.value = String(state.selectedTrimIdx);
  }
}

function switchPage(pageKey) {
  document.querySelectorAll(".page-tab-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.page === pageKey);
  });
  document.querySelectorAll(".page-panel").forEach((p) => {
    p.classList.toggle("active", p.id === `page-${pageKey}`);
  });
  if (pageKey === "chart") {
    requestAnimationFrame(() => renderChart());
  }
}

const BRAND_ZH_MAP = {
  "Aston Martin": "奧斯頓·馬丁",
  "Audi": "奧迪",
  "Bentley": "賓利",
  "BMW": "寶馬",
  "Citroen": "雪鐵龍",
  "Citroën": "雪鐵龍",
  "Daihatsu": "大發",
  "Ferrari": "法拉利",
  "Fiat": "飛雅特",
  "Ford": "福特",
  "Honda": "本田",
  "Hyundai": "現代",
  "Infiniti": "極致",
  "Jaguar": "捷豹",
  "Jeep": "吉普",
  "Kia": "起亞",
  "Lamborghini": "藍寶堅尼",
  "Land Rover": "荒原路華",
  "Lexus": "凌志",
  "Luxgen": "納智捷",
  "Maserati": "瑪莎拉蒂",
  "Mazda": "馬自達",
  "McLaren": "麥拉倫",
  "Mercedes-Benz": "賓士",
  "MG": "名爵",
  "MINI": "迷你",
  "Mini": "迷你",
  "Mitsubishi": "三菱",
  "Nissan": "日產",
  "Opel": "歐寶",
  "Peugeot": "寶獅",
  "Porsche": "保時捷",
  "Proton": "寶騰",
  "Renault": "雷諾",
  "Saab": "紳寶",
  "Skoda": "斯柯達",
  "Škoda": "斯柯達",
  "Smart": "司馬特",
  "SsangYong": "雙龍",
  "Subaru": "速霸陸",
  "Suzuki": "鈴木",
  "Tesla": "特斯拉",
  "Toyota": "豐田",
  "Volkswagen": "福斯",
  "Volvo": "富豪"
};

function formatBrandLabel(brand) {
  const clean = String(brand || "").trim();
  const zh = BRAND_ZH_MAP[clean];
  return zh ? `${clean} ${zh}` : clean;
}

function renderBrandControls() {
  const menu = document.getElementById("brandDropdownMenu");
  menu.innerHTML = state.brands
    .map(
      (b) => `
      <button type="button" class="custom-dropdown-item" data-brand="${b}" onclick="pickBrandFromMenu('${b}')">
        ${getBrandLogoSvg(b)}
        <span>${formatBrandLabel(b)}</span>
      </button>
    `
    )
    .join("");
}

function pickBrandFromMenu(brand) {
  document.getElementById("brandDropdown").classList.remove("open");
  selectBrand(brand);
}

function selectBrand(brand, preferredCarId = null) {
  state.selectedBrand = brand;
  document.getElementById("brandDropdownLabel").innerHTML = `${getBrandLogoSvg(brand)}<span>${brand}</span>`;
  document.querySelectorAll(".custom-dropdown-item").forEach((item) => {
    item.classList.toggle("active", item.dataset.brand === brand);
  });

  const brandCars = state.db.cars.filter((c) => c.brand === brand);
  const selModel = document.getElementById("selectModel");
  selModel.innerHTML = brandCars
    .map((c) => `<option value="${c.id}">${c.model} (${c.category})</option>`)
    .join("");

  const targetCarId = preferredCarId && brandCars.some((c) => c.id === preferredCarId)
    ? preferredCarId
    : brandCars[0].id;

  selectCar(targetCarId);
}

function selectCar(carId) {
  state.selectedCarId = carId;
  document.getElementById("selectModel").value = carId;
  state.selectedTrimIdx = 0;

  const car = getCurrentCar();
  const selYear = document.getElementById("selectYear");
  selYear.innerHTML = [...car.timeline]
    .reverse()
    .map((pt) => {
      const majorTxt = pt.is_major_change ? " ★大改款" : "";
      return `<option value="${pt.year}">${pt.year} 年式 (${pt.gen_name})${majorTxt}</option>`;
    })
    .join("");

  // 預設選中間偏實用的年份（或最新前3年）
  const defaultPt = car.timeline[Math.max(0, car.timeline.length - 3)];
  state.selectedYear = defaultPt.year;
  selYear.value = String(state.selectedYear);

  populateTrimSelect();
  renderAllCarViews();
}

function populateTrimSelect() {
  const gen = getSelectedGen();
  const selTrim = document.getElementById("selectTrim");
  const badge = document.getElementById("trimCountBadge");
  const hint = document.getElementById("trimHint");

  if (!gen || !gen.trims || !gen.trims.length) return;
  if (state.selectedTrimIdx >= gen.trims.length) {
    state.selectedTrimIdx = 0;
  }

  selTrim.innerHTML = gen.trims
    .map((t, idx) => `<option value="${idx}">${t.trim_name}</option>`)
    .join("");
  selTrim.value = String(state.selectedTrimIdx);

  if (gen.trims.length > 1) {
    badge.textContent = `${gen.trims.length} 種規格`;
    badge.style.display = "inline-block";
    hint.innerHTML = `<span>⚠</span><span>此世代有 <strong>${gen.trims.length}</strong> 種不同版本規格（例如引擎/油電/性能版差異），請務必確認版本以免誤判行情與稅金！</span>`;
    hint.classList.add("visible");
  } else {
    badge.style.display = "none";
    hint.classList.remove("visible");
  }
}

function getSelectedTrim() {
  const gen = getSelectedGen();
  return gen.trims[state.selectedTrimIdx] || gen.trims[0];
}

function getVariantRatio() {
  const gen = getSelectedGen();
  const baseTrim = gen.trims[0];
  const curTrim = getSelectedTrim();
  if (!baseTrim || !curTrim || !baseTrim.msrp_wan || !curTrim.msrp_wan) return 1.0;
  return curTrim.msrp_wan / baseTrim.msrp_wan;
}

function triggerAnim(elId) {
  const el = document.getElementById(elId);
  if (!el) return;
  el.classList.remove("anim-enter");
  void el.offsetWidth;
  el.classList.add("anim-enter");
}

function getCurrentCar() {
  return state.db.cars.find((c) => c.id === state.selectedCarId);
}

function getSelectedPoint() {
  const car = getCurrentCar();
  return car.timeline.find((pt) => pt.year === state.selectedYear) || car.timeline[0];
}

function getSelectedGen() {
  const car = getCurrentCar();
  const pt = getSelectedPoint();
  return car.generations.find((g) => g.gen_id === pt.gen_id) || car.generations[0];
}

function renderAllCarViews() {
  if (!state.inAnalysis) return;
  syncAnalysisQuickSelectors();
  renderHeroAndKpis();
  renderPhotoStrip();
  updateChartLegendAndButtons();
  renderChart();
  renderQuickSpecs();
  renderCostAndMaintenance();
  renderDetailBody();

  ["kpiGrid", "quickSpecsGrid", "costEstimationGrid", "detailBody"].forEach(triggerAnim);
}

function renderHeroAndKpis() {
  const car = getCurrentCar();
  const pt = getSelectedPoint();
  const gen = getSelectedGen();
  const trim = getSelectedTrim();
  const ratio = getVariantRatio();

  document.getElementById("heroTitle").innerHTML = `
    ${getBrandLogoSvg(car.brand, true)}
    <span>${car.brand} ${car.model} ・ ${pt.year} 年式</span>
    <span class="tag-blue">${gen.gen_name}</span>
    <span class="tag-blue" style="background:var(--sage-soft);border-color:#C8DDD0;color:var(--blue-primary);">${trim.trim_name}</span>
  `;
  document.getElementById("heroSub").textContent = car.summary;

  const riskBadge =
    pt.alert_level === "high"
      ? `<span class="tag-risk-high">⚠ 高風險通病 / 殘值劇降區間</span>`
      : pt.alert_level === "medium"
      ? `<span class="tag-risk-med">● 需留意特定通病</span>`
      : `<span class="tag-risk-low">✓ 市場保值穩健</span>`;
  const majorBadge = pt.is_major_change ? `<span class="tag-major">★ 大改款年份</span>` : "";
  document.getElementById("heroBadges").innerHTML = `${majorBadge}${riskBadge}`;

  // 里程、車況與版本價差微調係數
  const mileageWan = parseFloat(document.getElementById("inputMileage").value) || 0;
  const condFactor = parseFloat(document.getElementById("selectCondition").value) || 1.0;
  const expectedMileage = pt.age_years * 1.2;
  const mileageFactor = Math.max(0.85, Math.min(1.12, 1 - (mileageWan - expectedMileage) * 0.012));

  const effMsrp = pt.msrp * ratio;
  const dealerVal = (pt.dealer * ratio * mileageFactor * condFactor).toFixed(1);
  const privateVal = (pt.private * ratio * mileageFactor * condFactor).toFixed(1);
  const bookVal = (pt.book * ratio * mileageFactor * condFactor).toFixed(1);

  document.getElementById("mileageHint").textContent =
    `該年式合理參考里程：約 ${expectedMileage.toFixed(1)} 萬 km（此版本當年新車價約 ${effMsrp.toFixed(1)} 萬）`;

  document.getElementById("kpiGrid").innerHTML = `
    <div class="kpi-box primary">
      <div class="kpi-label">認證車商合理售價 (8891/SUM/ABC)</div>
      <div class="kpi-value" style="color:var(--blue-dark);">${dealerVal} 萬</div>
      <div class="kpi-sub">殘值率 ${pt.residual_dealer_pct}% ・ 含整理與保固</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">非第三方民間自售實價 (PTT/社團)</div>
      <div class="kpi-value" style="color:var(--green);">${privateVal} 萬</div>
      <div class="kpi-sub">車商價差約 +${(pt.dealer_private_spread_wan * ratio).toFixed(1)} 萬</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">權威車訊 (天書) 收購基準</div>
      <div class="kpi-value" style="color:var(--orange);">${bookVal} 萬</div>
      <div class="kpi-sub">銀行貸款與車商估收錨點</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">年度稅金 (牌照+燃料費)</div>
      <div class="kpi-value" style="color:var(--text-main);">${trim.annual_tax_ntd.toLocaleString()} 元</div>
      <div class="kpi-sub">${trim.displacement_cc} cc ・ 年均折舊 ${(pt.avg_annual_depreciation_wan * ratio).toFixed(2)} 萬/年</div>
    </div>
  `;
}

function updateChartLegendAndButtons() {
  document.getElementById("btnModePrice").classList.toggle("active", state.chartMode === "price");
  document.getElementById("btnModeResidual").classList.toggle("active", state.chartMode === "residual");

  const legend = document.getElementById("chartLegend");
  if (state.chartMode === "price") {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-line" style="background:#A8A29E;"></span>當年新車 MSRP</span>
      <span class="legend-item"><span class="legend-line" style="background:#1B4332;"></span>認證車商均價</span>
      <span class="legend-item"><span class="legend-line" style="background:#40916C;"></span>非第三方民間自售實價</span>
      <span class="legend-item"><span class="legend-line" style="background:#B45309;"></span>權威天書基準</span>
    `;
  } else {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-line" style="background:#1B4332;"></span>車商殘值率 (%)</span>
      <span class="legend-item"><span class="legend-line" style="background:#40916C;"></span>民間自售殘值率 (%)</span>
      <span class="legend-item"><span class="legend-line" style="background:#B45309;"></span>天書殘值率 (%)</span>
    `;
  }
}

function renderPhotoStrip() {
  const car = getCurrentCar();
  const currentGen = getSelectedGen();
  const stripEl = document.getElementById("photoStrip");

  stripEl.innerHTML = car.generations
    .map((g) => {
      const yr = `${g.years[0]}–${g.years[g.years.length - 1]}`;
      const active = g.gen_id === currentGen.gen_id ? "active" : "";
      return `
        <div class="gen-photo-card ${active}" onclick="jumpToGen('${g.gen_id}')">
          <div class="gen-photo-wrap">
            <img id="img-${g.gen_id}" class="gen-photo-thumb" alt="${car.brand} ${car.model} ${g.gen_name}" />
          </div>
          <div class="gen-photo-body">
            <div class="gen-photo-name">${g.gen_name}</div>
            <div class="gen-photo-years">${yr}</div>
            <div class="gen-photo-credit" id="credit-${g.gen_id}">載入圖片中...</div>
          </div>
        </div>
      `;
    })
    .join("");

  car.generations.forEach((g) => loadGenPhoto(g));
}

function loadGenPhoto(gen) {
  const imgEl = document.getElementById(`img-${gen.gen_id}`);
  const creditEl = document.getElementById(`credit-${gen.gen_id}`);
  if (!imgEl || !creditEl) return;

  // 優先使用本地去背白底圖 (assets/cars/<gen_id>.jpg)，若尚未補圖則顯示佔位圖
  const localUrl = `assets/cars/${gen.gen_id}.jpg`;
  imgEl.onload = () => {
    if (!imgEl.src.endsWith("placeholder.svg")) {
      creditEl.textContent = "去背白底圖 (實拍 / 原廠圖庫)";
    }
  };
  imgEl.onerror = () => {
    imgEl.onerror = null;
    imgEl.src = "assets/cars/placeholder.svg";
    creditEl.textContent = `待補實車去背照 (${gen.gen_id}.jpg)`;
  };
  imgEl.src = localUrl;
}

function renderChart() {
  const car = getCurrentCar();
  const gen = getSelectedGen();
  const ratio = getVariantRatio();
  const scaledTimeline = car.timeline.map((pt) => {
    if (pt.gen_id !== gen.gen_id || ratio === 1.0) return pt;
    return {
      ...pt,
      msrp: +(pt.msrp * ratio).toFixed(1),
      dealer: +(pt.dealer * ratio).toFixed(1),
      private: +(pt.private * ratio).toFixed(1),
      book: +(pt.book * ratio).toFixed(1),
    };
  });
  state.chart.setData(scaledTimeline, state.chartMode, state.selectedYear);
}

function renderQuickSpecs() {
  const gen = getSelectedGen();
  const trim = gen.trims[state.selectedTrimIdx] || gen.trims[0];
  const items = [
    ["引擎型式", trim.engine_code],
    ["排氣量 / 馬力", `${trim.displacement_cc} cc ・ ${trim.horsepower}`],
    ["變速箱架構", trim.transmission],
    ["底盤懸吊", trim.suspension],
    ["平均油耗", trim.fuel_economy],
    ["安全配備", trim.safety],
  ];

  document.getElementById("quickSpecsGrid").innerHTML = items
    .map(
      ([k, v]) => `
      <div class="qspec-item">
        <div class="qspec-k">${k}</div>
        <div class="qspec-v">${v}</div>
      </div>
    `
    )
    .join("");
}

function parseFuelKmL(str) {
  const m = String(str || "").match(/([\d.]+)/);
  return m ? parseFloat(m[1]) : 14.0;
}

function renderCostAndMaintenance() {
  const car = getCurrentCar();
  const pt = getSelectedPoint();
  const gen = getSelectedGen();
  const trim = getSelectedTrim();
  const ratio = getVariantRatio();

  const annualKm = parseInt(document.getElementById("selectAnnualKm").value, 10) || 12000;
  const insPlan = document.getElementById("selectInsurancePlan").value || "bing";
  const mileageWan = parseFloat(document.getElementById("inputMileage").value) || 8.0;

  // 1. 年度稅金 + 油錢 + 保養 + 保險
  const tax = trim.annual_tax_ntd;
  const kmPerL = parseFuelKmL(trim.fuel_economy);
  const fuelPrice = 30.5; // 95無鉛參考價
  const annualFuel = Math.round((annualKm / kmPerL) * fuelPrice);

  const isLuxury = ["Lexus", "Mercedes-Benz", "BMW"].includes(car.brand);
  const isEuro = ["Volkswagen"].includes(car.brand);
  const isImportJp = ["Mazda", "Subaru", "Suzuki"].includes(car.brand);
  const baseMaint = car.brand === "Lexus" ? 13000 : isLuxury ? 26000 : isEuro ? 15000 : isImportJp ? 11000 : 8500;

  // 保險估算
  const mandatoryIns = 1400;
  const thirdPartyIns = isLuxury ? 9500 : 7500;
  let bodyIns = 0;
  let bodyInsLabel = "未投保車體險";
  if (insPlan === "bing") {
    bodyIns = Math.max(4500, Math.round(pt.dealer * ratio * 10000 * (isLuxury ? 0.028 : 0.022)));
    bodyInsLabel = "丙式車碰車險（依殘值估算）";
  } else if (insPlan === "yi") {
    bodyIns = Math.max(12000, Math.round(pt.dealer * ratio * 10000 * (isLuxury ? 0.052 : 0.042)));
    bodyInsLabel = "乙式全險（依殘值估算）";
  }
  const totalIns = mandatoryIns + thirdPartyIns + bodyIns;
  const totalAnnual = tax + annualFuel + baseMaint + totalIns;
  const monthlyAvg = Math.round(totalAnnual / 12);

  // 2. 依車齡與里程估算「買後需維修與整備品項」
  const age = pt.age_years;
  const maintItems = [];

  if (age >= 3 || mileageWan >= 5) {
    maintItems.push({
      name: "全車油水大保養 (機油/變速箱油/煞車油/水箱精)",
      cost: isLuxury ? "12,000 ~ 20,000 元" : "6,000 ~ 11,000 元",
      min: isLuxury ? 12000 : 6000,
      max: isLuxury ? 20000 : 11000,
      note: "買中古車建議交車即更換重置保養週期",
    });
  }
  if (age >= 4 || mileageWan >= 6) {
    maintItems.push({
      name: "輪胎四條 + 電瓶檢測更換",
      cost: isLuxury ? "20,000 ~ 32,000 元" : "12,000 ~ 18,000 元",
      min: isLuxury ? 20000 : 12000,
      max: isLuxury ? 32000 : 18000,
      note: "依胎紋年份判斷（超過4年建議更換）",
    });
  }
  if (age >= 7 || mileageWan >= 10) {
    maintItems.push({
      name: "避震器 / 引擎腳 / 三角架鐵套等底盤橡膠件",
      cost: isLuxury ? "25,000 ~ 45,000 元" : "12,000 ~ 24,000 元",
      min: isLuxury ? 25000 : 12000,
      max: isLuxury ? 45000 : 24000,
      note: `車齡 ${age} 年橡膠件多已硬化，影響舒適與異音`,
    });
  }
  if (age >= 10 || mileageWan >= 14) {
    maintItems.push({
      name: "冷氣壓縮機 / 發電機 / 水箱冷卻水管路預防整理",
      cost: isLuxury ? "25,000 ~ 45,000 元" : "10,000 ~ 22,000 元",
      min: isLuxury ? 25000 : 10000,
      max: isLuxury ? 45000 : 22000,
      note: "高齡老車顧路主因，建議預先檢查",
    });
  }
  if (trim.engine_code.includes("Hybrid") || trim.engine_code.includes("e:HEV")) {
    if (age >= 8 || mileageWan >= 15) {
      maintItems.push({
        name: "油電大電池健康度檢查 / 預留更換風險",
        cost: "45,000 ~ 65,000 元",
        min: 45000,
        max: 65000,
        note: "高里程油電車過保後需留意電池壽命",
      });
    }
  }

  // 加上該世代專屬通病提醒
  const issueSummaries = gen.common_issues.map(
    (iss) => `
    <div class="cost-row">
      <span class="cost-row-name"><strong>[世代通病]</strong> ${iss.part}</span>
      <span class="cost-row-val" style="color:var(--red);">${iss.repair_cost_ntd}</span>
    </div>`
  );

  const minSum = maintItems.reduce((acc, it) => acc + it.min, 0);
  const maxSum = maintItems.reduce((acc, it) => acc + it.max, 0);
  const riskExtra = pt.alert_level === "high" ? 30000 : pt.alert_level === "medium" ? 15000 : 0;

  document.getElementById("costEstimationGrid").innerHTML = `
    <div class="cost-panel">
      <div class="cost-panel-title">
        <span>年度養車成本與保險估算</span>
        <span class="tag-blue">${pt.year} 年式 ・ 年跑 ${(annualKm / 10000).toFixed(1)} 萬 km</span>
      </div>
      <div class="cost-list">
        <div class="cost-row">
          <span class="cost-row-name">年度稅金（牌照稅 + 燃料費）</span>
          <span class="cost-row-val">${tax.toLocaleString()} 元</span>
        </div>
        <div class="cost-row">
          <span class="cost-row-name">預估油錢（平均油耗 ${kmPerL} km/L）</span>
          <span class="cost-row-val">${annualFuel.toLocaleString()} 元</span>
        </div>
        <div class="cost-row">
          <span class="cost-row-name">基礎保養與耗材攤提（機油/濾芯/基本耗材）</span>
          <span class="cost-row-val">${baseMaint.toLocaleString()} 元</span>
        </div>
        <div class="cost-row">
          <span class="cost-row-name">強制險 + 第三人責任超額險</span>
          <span class="cost-row-val">${(mandatoryIns + thirdPartyIns).toLocaleString()} 元</span>
        </div>
        <div class="cost-row">
          <span class="cost-row-name">${bodyInsLabel}</span>
          <span class="cost-row-val">${bodyIns.toLocaleString()} 元</span>
        </div>
      </div>
      <div class="cost-total-box">
        <div>
          <div style="font-size:0.78rem;color:var(--text-sub);font-weight:700;">預估每年養車總開銷</div>
          <div style="font-size:0.74rem;color:var(--text-muted);">平均每月約 ${monthlyAvg.toLocaleString()} 元</div>
        </div>
        <div style="font-size:1.3rem;font-weight:800;color:var(--blue-dark);">${totalAnnual.toLocaleString()} 元/年</div>
      </div>
    </div>

    <div class="cost-panel">
      <div class="cost-panel-title">
        <span>依車齡/里程需維修品項估算</span>
        <span class="tag-blue">車齡 ${age} 年 ・ ${mileageWan} 萬 km</span>
      </div>
      <div class="cost-list">
        ${maintItems
          .map(
            (it) => `
          <div class="cost-row">
            <span class="cost-row-name">${it.name}<br><small style="color:var(--text-muted);">${it.note}</small></span>
            <span class="cost-row-val">${it.cost}</span>
          </div>`
          )
          .join("")}
        ${issueSummaries.join("")}
      </div>
      <div class="cost-total-box">
        <div>
          <div style="font-size:0.78rem;color:var(--text-sub);font-weight:700;">建議額外預留「買後整備維修金」</div>
          <div style="font-size:0.74rem;color:var(--text-muted);">實際費用視前車主已更換項目而定</div>
        </div>
        <div style="font-size:1.15rem;font-weight:800;color:var(--orange);">${((minSum + riskExtra) / 10000).toFixed(1)} ~ ${((maxSum + riskExtra) / 10000).toFixed(1)} 萬</div>
      </div>
    </div>
  `;
}

function renderDetailBody() {
  const body = document.getElementById("detailBody");
  const car = getCurrentCar();
  const gen = getSelectedGen();

  const ytDesc = document.getElementById("detailYoutubeDesc");
  if (ytDesc && car && gen) {
    ytDesc.textContent = `延伸觀看 ${car.brand} ${car.model}（${gen.gen_name}）實車拆解、中古折舊與養車實測影片`;
  }

  if (state.activeDetailTab === "specs") {
    const trimBtns = gen.trims
      .map(
        (t, i) =>
          `<button class="mode-pill ${i === state.selectedTrimIdx ? "active" : ""}" onclick="switchTrim(${i})">${t.trim_name}</button>`
      )
      .join("");
    const trim = gen.trims[state.selectedTrimIdx] || gen.trims[0];
    const rows = [
      ["動力編成", trim.trim_name],
      ["引擎代號/形式", trim.engine_code],
      ["排氣量", `${trim.displacement_cc} cc`],
      ["最大馬力", trim.horsepower],
      ["最大扭力", trim.torque],
      ["變速箱", trim.transmission],
      ["驅動方式", trim.drivetrain],
      ["前後懸吊", trim.suspension],
      ["平均油耗", trim.fuel_economy],
      ["車身尺碼 / 軸距", trim.dimensions],
      ["安全配備", trim.safety],
      ["產地 / 底盤平台", `${gen.origin} / ${gen.platform}`],
    ];
    body.innerHTML = `
      <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;">${trimBtns}</div>
      <div class="specs-full-grid">
        ${rows
          .map(
            ([k, v]) => `
          <div class="spec-cell">
            <div class="spec-cell-k">${k}</div>
            <div class="spec-cell-v">${v}</div>
          </div>`
          )
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "issues") {
    const alert = gen.depreciation_alert;
    body.innerHTML = `
      <div style="margin-bottom:12px;padding:12px 14px;border-radius:10px;border:1px solid var(--border-blue);background:var(--bg-soft);">
        <strong>${gen.gen_name} 殘值與通病總評：</strong>${alert.title} — ${alert.reason}
      </div>
      <div class="issues-stack">
        ${gen.common_issues
          .map((iss) => {
            const cls = iss.severity === "高風險" ? "high" : iss.severity === "中風險" ? "med" : "low";
            return `
            <div class="issue-row ${cls}">
              <div class="issue-row-top">
                <span>${iss.part}</span>
                <span class="tag-blue">${iss.severity} ・ 好發 ${iss.mileage_range}</span>
              </div>
              <div class="issue-row-meta">
                <div><strong>症狀：</strong>${iss.symptom}</div>
                <div><strong>預估維修費：</strong><span style="color:var(--orange);font-weight:700;">${iss.repair_cost_ntd}</span></div>
                <div><strong>避坑建議：</strong><span style="color:var(--green);font-weight:700;">${iss.advice}</span></div>
              </div>
            </div>`;
          })
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "gens") {
    body.innerHTML = `
      <div class="gen-list">
        ${car.generations
          .map((g) => {
            const yr = `${g.years[0]}–${g.years[g.years.length - 1]}`;
            const active = g.gen_id === gen.gen_id ? "active" : "";
            return `
            <div class="gen-card ${active}" onclick="jumpToGen('${g.gen_id}')">
              <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:6px;">
                <strong>${g.gen_name}</strong>
                <span class="tag-major">${g.is_major_change ? "大改款" : "小改款"} ${g.major_change_year}</span>
              </div>
              <div style="font-size:0.8rem;color:var(--blue-dark);margin-bottom:6px;">年份：${yr} ・ 平均車商殘值 ${g.avg_residual_dealer_pct}%</div>
              <div style="font-size:0.82rem;color:var(--text-sub);">${g.major_change_note}</div>
            </div>`;
          })
          .join("")}
      </div>
    `;
  } else if (state.activeDetailTab === "history") {
    body.innerHTML = `
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>年份</th>
              <th>世代</th>
              <th>新車價</th>
              <th>認證車商價</th>
              <th>民間自售價</th>
              <th>權威天書價</th>
              <th>殘值率(商/私)</th>
              <th>年均折舊</th>
            </tr>
          </thead>
          <tbody>
            ${car.timeline
              .map(
                (pt) => `
              <tr class="${pt.year === state.selectedYear ? "row-selected" : ""}">
                <td><strong>${pt.year}</strong> ${pt.is_major_change ? '<span class="tag-major">大改款</span>' : ""}</td>
                <td>${pt.gen_name}</td>
                <td>${pt.msrp.toFixed(1)} 萬</td>
                <td style="color:var(--blue-dark);font-weight:700;">${pt.dealer.toFixed(1)} 萬</td>
                <td style="color:var(--green);font-weight:700;">${pt.private.toFixed(1)} 萬</td>
                <td style="color:var(--orange);">${pt.book.toFixed(1)} 萬</td>
                <td>${pt.residual_dealer_pct}% / ${pt.residual_private_pct}%</td>
                <td>${pt.avg_annual_depreciation_wan} 萬/年</td>
              </tr>`
              )
              .join("")}
          </tbody>
        </table>
      </div>
    `;
  } else if (state.activeDetailTab === "sources") {
    body.innerHTML = `
      <div class="gen-list">
        ${state.db.data_sources
          .map(
            (s) => `
          <div class="gen-card">
            <strong style="color:var(--blue-dark);">${s.name}</strong>
            <div style="font-size:0.78rem;color:var(--green);margin:3px 0 6px;">${s.type} ・ ${s.credibility}</div>
            <div style="font-size:0.82rem;color:var(--text-sub);">${s.description}</div>
          </div>`
          )
          .join("")}
      </div>
    `;
  }
}

function switchTrim(idx) {
  state.selectedTrimIdx = idx;
  const selTrim = document.getElementById("selectTrim");
  if (selTrim) selTrim.value = String(idx);
  renderAllCarViews();
}

function jumpToGen(genId) {
  const car = getCurrentCar();
  const gen = car.generations.find((g) => g.gen_id === genId);
  if (gen && gen.years.length) {
    state.selectedYear = gen.years[0];
    document.getElementById("selectYear").value = String(state.selectedYear);
    state.selectedTrimIdx = 0;
    populateTrimSelect();
    renderAllCarViews();
  }
}

function renderRankingTable() {
  const ranked = state.db.cars
    .map((c) => {
      const latestGen = c.generations[c.generations.length - 1];
      const hasHigh = c.generations.some((g) => g.depreciation_alert.level === "high");
      return {
        id: c.id,
        brand: c.brand,
        model: c.model,
        category: c.category,
        latestGenName: latestGen.gen_name,
        avgRes: latestGen.avg_residual_dealer_pct,
        hasHigh,
      };
    })
    .sort((a, b) => b.avgRes - a.avgRes);

  document.getElementById("rankingTableBody").innerHTML = ranked
    .map(
      (r, i) => `
      <tr>
        <td><strong>#${i + 1}</strong></td>
        <td><strong>${r.brand} ${r.model}</strong></td>
        <td>${r.category}</td>
        <td>${r.latestGenName}</td>
        <td style="color:var(--blue-dark);font-weight:800;">${r.avgRes}%</td>
        <td>${r.hasHigh ? '<span class="tag-risk-high">含高風險世代</span>' : '<span class="tag-risk-low">保值穩健</span>'}</td>
        <td><button class="mode-pill" onclick="pickFromRanking('${r.brand}','${r.id}')">查看分析</button></td>
      </tr>
    `
    )
    .join("");
}

function pickFromRanking(brand, carId) {
  selectBrand(brand, carId);
  enterAnalysisScreen("ranking");
}

function parseMaxHp(hpStr) {
  const str = String(hpStr || "");
  // 優先擷取 ps / hp / 匹 前方的馬力數值，避免抓到轉速 (如 6,000 rpm) 或年份 (如 2022+)
  const hpMatches = [...str.matchAll(/(\d+(?:\.\d+)?)\s*(?:ps|hp|匹)/gi)];
  if (hpMatches.length) {
    return Math.max(...hpMatches.map((m) => parseFloat(m[1])));
  }
  const nums = str.match(/(\d+(?:\.\d+)?)/g);
  if (!nums) return 0;
  return Math.max(...nums.map((n) => parseFloat(n)));
}

function matchBodyCategory(category, filterVal) {
  if (filterVal === "all") return true;
  if (filterVal === "小車") return /小車|掀背|小型|迷你/.test(category) && !/休旅|SUV|越野/.test(category);
  if (filterVal === "房車") return /房車|轎跑/.test(category) && !/休旅/.test(category);
  if (filterVal === "休旅") return /休旅|跑旅|轎旅|SUV|MPV|CUV|越野/.test(category);
  if (filterVal === "跑車旅行") return /敞篷|跑車|旅行車|獵跑/.test(category);
  if (filterVal === "皮卡商用") return /皮卡|Pickup|商用|商旅|露營/.test(category);
  return true;
}

function getTrimTransmissionType(trim) {
  const rawTrans = String(trim.transmission || "").trim();
  const isManual = /(?:^|\b|\d)MT\b|手排|manual/i.test(rawTrans) && !/AMT|自手排/i.test(rawTrans);
  return isManual ? "manual" : "auto";
}

function getTrimPowertrainType(car, trim) {
  const cc = Number(trim.displacement_cc ?? -1);
  const signature = `${car.category || ""} ${trim.engine_code || ""} ${trim.trim_name || ""}`;
  if (/\b(BEV|EV)\b|純電|電動車|電動馬達|Single-Speed|單速/i.test(signature) || (cc === 0 && !/hybrid|油電/i.test(signature))) {
    return "ev";
  }
  if (/hybrid|油電|PHEV|HEV|MHEV|e:HEV|THS|48V|輕油電/i.test(signature)) {
    return "hybrid";
  }
  return "ice";
}

function renderSmartFinder() {
  const goal = document.getElementById("finderGoal").value;
  const body = document.getElementById("finderBody").value;
  const maxCc = parseInt(document.getElementById("finderMaxCc").value, 10) || 9999;
  const transFilter = document.getElementById("finderTransmission")?.value || "all";
  const powerFilter = document.getElementById("finderPowertrain")?.value || "all";

  const minBudget = parseFloat(document.getElementById("finderBudgetMin").value);
  const maxBudget = parseFloat(document.getElementById("finderBudgetMax").value);
  const bMin = Number.isFinite(minBudget) ? minBudget : 0;
  const bMax = Number.isFinite(maxBudget) ? maxBudget : Infinity;

  const minHp = parseFloat(document.getElementById("finderHpMin").value);
  const maxHp = parseFloat(document.getElementById("finderHpMax").value);
  const hMin = Number.isFinite(minHp) ? minHp : 0;
  const hMax = Number.isFinite(maxHp) ? maxHp : Infinity;

  const minYear = parseInt(document.getElementById("finderYearMin").value, 10);
  const maxYear = parseInt(document.getElementById("finderYearMax").value, 10);
  const yMin = Number.isFinite(minYear) ? minYear : 2000;
  const yMax = Number.isFinite(maxYear) ? maxYear : 2026;

  const matches = [];

  state.db.cars.forEach((car) => {
    if (!matchBodyCategory(car.category, body)) return;

    car.generations.forEach((gen) => {
      const baseMsrp = gen.trims?.[0]?.msrp_wan || 1;
      if (goal === "no-high-risk" && gen.depreciation_alert.level === "high") return;
      if (goal === "safe-value" && (gen.depreciation_alert.level !== "low" || gen.avg_residual_dealer_pct < 42)) return;

      (gen.trims || []).forEach((trim, trimIdx) => {
        const trimTransType = getTrimTransmissionType(trim);
        const trimPowerType = getTrimPowertrainType(car, trim);
        if (transFilter !== "all" && trimTransType !== transFilter) return;
        if (powerFilter !== "all" && trimPowerType !== powerFilter) return;

        const hp = parseMaxHp(trim.horsepower);
        const parsedCc = parseInt(trim.displacement_cc, 10);
        const cc = Number.isFinite(parsedCc) ? parsedCc : 1800;
        if (hp < hMin || hp > hMax) return;
        if (trimPowerType !== "ev" && cc > maxCc) return;
        if (goal === "easy-own" && (cc > 1800 || gen.depreciation_alert.level === "high")) return;

        if (goal === "handling") {
          const isHandling =
            /多連桿|雙A臂|運動|Sport|GTI|ST|後驅|FR|手排|敞篷|跑車|渦輪/.test(
              `${car.category} ${trim.trim_name} ${trim.suspension} ${trim.transmission} ${trim.drivetrain}`
            );
          if (!isHandling) return;
        }
        if (goal === "comfort") {
          const isComfort =
            /房車|休旅|SUV|MPV|CVT|自排|油電|Hybrid|e:HEV/.test(
              `${car.category} ${trim.trim_name} ${trim.transmission}`
            ) && !/純手排|跑車/.test(`${car.category} ${trim.transmission}`);
          if (!isComfort) return;
        }

        const ratio = trim.msrp_wan ? trim.msrp_wan / baseMsrp : 1.0;

        // 找出該世代+版本中，符合年份與預算範圍的最新年份代表
        const validPts = (gen.year_points || []).filter((pt) => {
          const effPrice = +(pt.dealer * ratio).toFixed(1);
          if (effPrice < bMin || effPrice > bMax) return false;
          if (pt.year < yMin || pt.year > yMax) return false;
          return true;
        });

        if (validPts.length) {
          const bestPt = validPts[validPts.length - 1];
          matches.push({
            car,
            gen,
            trim,
            trimIdx,
            year: bestPt.year,
            price: +(bestPt.dealer * ratio).toFixed(1),
            residual: bestPt.residual_dealer_pct,
            hp,
            cc,
            tax: trim.annual_tax_ntd,
          });
        }
      });
    });
  });

  const sortMode = document.getElementById("finderSort")?.value || "default";
  matches.sort((a, b) => {
    switch (sortMode) {
      case "year-desc":
        return b.year - a.year || b.residual - a.residual;
      case "year-asc":
        return a.year - b.year || b.residual - a.residual;
      case "price-asc":
        return a.price - b.price || b.year - a.year;
      case "price-desc":
        return b.price - a.price || b.year - a.year;
      case "hp-desc":
        return b.hp - a.hp || b.year - a.year;
      case "hp-asc":
        return a.hp - b.hp || b.year - a.year;
      case "cc-asc":
        return a.cc - b.cc || b.year - a.year;
      case "cc-desc":
        return b.cc - a.cc || b.year - a.year;
      default:
        return b.year - a.year || b.residual - a.residual;
    }
  });

  document.getElementById("finderResultCount").textContent =
    `共找到 ${matches.length} 筆符合條件的世代與版本組合（點擊任一卡片直接進入分析）`;

  const grid = document.getElementById("finderResultsGrid");
  if (!matches.length) {
    grid.innerHTML = `<div style="color:var(--text-sub);font-size:0.88rem;padding:14px 0;">目前條件較嚴格，建議稍微放寬預算、馬力或年份範圍。</div>`;
    return;
  }

  grid.innerHTML = matches
    .slice(0, 60)
    .map((m) => {
      const refKm = Math.max(1.0, (2026 - m.year) * 1.2).toFixed(1);
      const isVerified = m.gen.depreciation_alert.level === "low";
      const powerText = m.cc === 0 ? `${m.hp} ps · 純電` : `${m.hp} ps · ${m.cc} cc`;
      return `
      <button type="button" class="finder-card" onclick="pickFromFinder('${m.car.brand}','${m.car.id}',${m.year},${m.trimIdx})">
        <div class="finder-card-photo">
          ${isVerified ? `<span class="finder-verified-pill">實價已查驗</span>` : ""}
          <img src="assets/cars/${m.gen.gen_id}.jpg" alt="${m.car.brand} ${m.car.model}" loading="lazy" onerror="this.onerror=null;this.src='assets/cars/placeholder.svg';" />
        </div>
        <div class="finder-card-top">
          <div>
            <div class="finder-card-title">${m.car.brand} ${m.car.model} · ${m.trim.trim_name}</div>
          </div>
          <div class="finder-card-price">${m.price.toFixed(1)} 萬</div>
        </div>
        <div class="finder-card-metrics">
          <div class="finder-metric-item">
            <span class="finder-metric-label">年份</span>
            <span>${m.year} 年式</span>
          </div>
          <div class="finder-metric-item">
            <span class="finder-metric-label">參考里程</span>
            <span>約 ${refKm} 萬 km</span>
          </div>
          <div class="finder-metric-item">
            <span class="finder-metric-label">動力規格</span>
            <span>${powerText}</span>
          </div>
        </div>
      </button>
    `;
    })
    .join("");
}

function pickFromFinder(brand, carId, year, trimIdx) {
  selectBrand(brand, carId);
  state.selectedYear = year;
  document.getElementById("selectYear").value = String(year);
  populateTrimSelect();
  state.selectedTrimIdx = trimIdx;
  document.getElementById("selectTrim").value = String(trimIdx);
  enterAnalysisScreen("finder");
}

document.addEventListener("DOMContentLoaded", initApp);
