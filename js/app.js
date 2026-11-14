/**
 * 台灣中古車時價分析與世代通病資料庫 - 前端互動主程式
 */

const state = {
  db: null,
  selectedCarId: null,
  selectedGenId: null,
  selectedTrimIdx: 0,
  chartMode: "price", // 'price' | 'residual'
  searchQuery: "",
  chart: null,
};

async function initApp() {
  state.chart = new MarketTrendChart("trendCanvas", "chartTooltip");

  try {
    const resp = await fetch("data/cars_db.json");
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    state.db = await resp.json();
  } catch (err) {
    document.getElementById("mainContent").innerHTML = `
      <div class="card">
        <h2 style="color:#f87171;">無法載入資料庫 (data/cars_db.json)</h2>
        <p style="margin-top:8px;color:#94a3b8;">
          請使用專案根目錄的 <strong>啟動中古車分析網站.bat</strong> 來啟動本地伺服器，或將網站部署至 GitHub Pages。
        </p>
        <p style="margin-top:6px;font-size:0.85rem;color:#64748b;">錯誤訊息：${err.message}</p>
      </div>
    `;
    return;
  }

  renderHeaderStats();
  renderDataSources();

  if (state.db.cars.length > 0) {
    selectCar(state.db.cars[0].id);
  }

  bindGlobalEvents();
}

function bindGlobalEvents() {
  document.getElementById("carSearch").addEventListener("input", (e) => {
    state.searchQuery = e.target.value.trim().toLowerCase();
    renderSidebar();
  });

  document.getElementById("btnModePrice").addEventListener("click", () => {
    state.chartMode = "price";
    updateChartModeButtons();
    renderChart();
  });

  document.getElementById("btnModeResidual").addEventListener("click", () => {
    state.chartMode = "residual";
    updateChartModeButtons();
    renderChart();
  });

  ["calcYear", "calcMileage", "calcCondition"].forEach((id) => {
    document.getElementById(id).addEventListener("change", updateValuationCalculator);
    document.getElementById(id).addEventListener("input", updateValuationCalculator);
  });
}

function updateChartModeButtons() {
  document.getElementById("btnModePrice").classList.toggle("active", state.chartMode === "price");
  document.getElementById("btnModeResidual").classList.toggle("active", state.chartMode === "residual");

  const legend = document.getElementById("chartLegend");
  if (state.chartMode === "price") {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-dot" style="background:#a78bfa;"></span>當年新車 MSRP (虛線)</span>
      <span class="legend-item"><span class="legend-dot" style="background:#38bdf8;"></span>認證車商均價 (8891/SUM/ABC)</span>
      <span class="legend-item"><span class="legend-dot" style="background:#34d399;"></span>非第三方民間自售實價 (PTT/社團)</span>
      <span class="legend-item"><span class="legend-dot" style="background:#fb923c;"></span>權威車訊(天書)收購基準</span>
      <span class="legend-item"><span class="legend-dot" style="background:rgba(248,113,113,0.45);height:10px;"></span>高風險通病/殘值劇降區間</span>
    `;
  } else {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-dot" style="background:#38bdf8;"></span>車商殘值率 (%)</span>
      <span class="legend-item"><span class="legend-dot" style="background:#34d399;"></span>非第三方自售殘值率 (%)</span>
      <span class="legend-item"><span class="legend-dot" style="background:#fb923c;"></span>權威天書殘值率 (%)</span>
      <span class="legend-item"><span class="legend-dot" style="background:rgba(248,113,113,0.45);height:10px;"></span>高風險通病區間</span>
    `;
  }
}

function renderHeaderStats() {
  const m = state.db.meta;
  document.getElementById("headerStats").innerHTML = `
    <div class="stat-pill">收錄車系 <strong>${m.total_models}</strong></div>
    <div class="stat-pill">獨立世代 <strong>${m.total_generations}</strong></div>
    <div class="stat-pill">年份紀錄 <strong>${m.total_year_records}</strong></div>
    <div class="stat-pill">基準年 <strong>${m.reference_year}</strong></div>
  `;
}

function getCurrentCar() {
  return state.db.cars.find((c) => c.id === state.selectedCarId);
}

function getCurrentGen() {
  const car = getCurrentCar();
  if (!car) return null;
  return car.generations.find((g) => g.gen_id === state.selectedGenId) || car.generations[0];
}

function selectCar(carId) {
  state.selectedCarId = carId;
  const car = getCurrentCar();
  state.selectedGenId = car.generations[0].gen_id;
  state.selectedTrimIdx = 0;

  renderSidebar();
  renderCarHeader();
  renderGenTabs();
  renderGenDetails();
  updateChartModeButtons();
  renderChart();
  populateCalculatorYears();
  updateValuationCalculator();
  renderHistoryTable();
}

function selectGeneration(genId) {
  state.selectedGenId = genId;
  state.selectedTrimIdx = 0;
  renderGenTabs();
  renderGenDetails();
}

function renderSidebar() {
  const listEl = document.getElementById("carList");
  const filtered = state.db.cars.filter((c) => {
    const q = state.searchQuery;
    if (!q) return true;
    return (
      c.brand.toLowerCase().includes(q) ||
      c.model.toLowerCase().includes(q) ||
      c.model_zh.toLowerCase().includes(q) ||
      c.category.toLowerCase().includes(q)
    );
  });

  listEl.innerHTML = filtered
    .map((car) => {
      const hasHighRisk = car.generations.some((g) => g.depreciation_alert.level === "high");
      const badge = hasHighRisk
        ? `<span class="risk-dot high">含高風險世代</span>`
        : `<span class="risk-dot low">保值/穩健</span>`;
      const activeClass = car.id === state.selectedCarId ? "active" : "";
      return `
        <button class="car-item ${activeClass}" onclick="selectCar('${car.id}')">
          <div class="car-item-top">
            <span class="car-item-name">${car.brand} ${car.model}</span>
            ${badge}
          </div>
          <div class="car-item-cat">${car.model_zh} ・ ${car.generations.length} 個世代</div>
        </button>
      `;
    })
    .join("");
}

function renderCarHeader() {
  const car = getCurrentCar();
  document.getElementById("modelHeroTitle").innerHTML = `
    <span>${car.brand} ${car.model}</span>
    <span class="brand-badge">${car.category}</span>
  `;
  document.getElementById("modelSummary").textContent = car.summary;
}

function renderGenTabs() {
  const car = getCurrentCar();
  const container = document.getElementById("genTabs");
  container.innerHTML = car.generations
    .map((gen) => {
      const years = gen.years;
      const yearRange = `${years[0]} – ${years[years.length - 1]}`;
      const badge = gen.is_major_change
        ? `<span class="badge-major">大改款 ${gen.major_change_year}</span>`
        : `<span class="badge-facelift">小改款 ${gen.major_change_year}</span>`;
      const active = gen.gen_id === state.selectedGenId ? "active" : "";
      return `
        <button class="gen-tab ${active}" onclick="selectGeneration('${gen.gen_id}')">
          <div class="gen-tab-title">
            <span>${gen.gen_name}</span>
            ${badge}
          </div>
          <div class="gen-tab-years">年份：${yearRange} ・ 平均車商殘值 ${gen.avg_residual_dealer_pct}%</div>
        </button>
      `;
    })
    .join("");
}

function renderGenDetails() {
  const gen = getCurrentGen();
  const alert = gen.depreciation_alert;

  document.getElementById("genAlertArea").innerHTML = `
    <div class="major-change-box">
      <strong>【世代/大改款差異標註 (${gen.major_change_year}年)】</strong>
      ${gen.major_change_note}<br>
      <span style="color:#94a3b8;font-size:0.8rem;">底盤平台：${gen.platform} ｜ 產地：${gen.origin}</span>
    </div>
    <div class="alert-banner ${alert.level}">
      <h4>${alert.level === "high" ? "⚠ " : alert.level === "medium" ? "● " : "✓ "}${alert.title}</h4>
      <p>${alert.reason}</p>
    </div>
  `;

  renderTrimsAndSpecs(gen);
  renderCommonIssues(gen);
}

function renderTrimsAndSpecs(gen) {
  const trimTabsEl = document.getElementById("trimTabs");
  trimTabsEl.innerHTML = gen.trims
    .map((t, idx) => {
      const active = idx === state.selectedTrimIdx ? "active" : "";
      return `<button class="btn-toggle ${active}" onclick="selectTrim(${idx})">${t.trim_name}</button>`;
    })
    .join("");

  const trim = gen.trims[state.selectedTrimIdx] || gen.trims[0];
  const specs = [
    ["引擎型號/形式", trim.engine_code],
    ["排氣量", `${trim.displacement_cc} cc`],
    ["最大馬力", trim.horsepower],
    ["最大扭力", trim.torque],
    ["變速箱架構", trim.transmission],
    ["驅動方式", trim.drivetrain],
    ["懸吊系統", trim.suspension],
    ["平均油耗", trim.fuel_economy],
    ["車身尺碼 / 軸距", trim.dimensions],
    ["主被動安全配備", trim.safety],
    ["當年新車建議售價", `${trim.msrp_wan} 萬元`],
    ["所屬世代平台", gen.platform],
  ];

  document.getElementById("specsGrid").innerHTML = specs
    .map(
      ([k, v]) => `
      <div class="spec-item">
        <div class="spec-key">${k}</div>
        <div class="spec-val">${v}</div>
      </div>
    `
    )
    .join("");
}

function selectTrim(idx) {
  state.selectedTrimIdx = idx;
  renderTrimsAndSpecs(getCurrentGen());
}

function renderCommonIssues(gen) {
  const el = document.getElementById("issuesList");
  el.innerHTML = gen.common_issues
    .map((issue) => {
      const sevClass =
        issue.severity === "高風險" ? "high" : issue.severity === "中風險" ? "med" : "low";
      return `
        <div class="issue-card sev-${sevClass}">
          <div class="issue-top">
            <span class="issue-title">${issue.part}</span>
            <span class="sev-badge ${sevClass}">${issue.severity} ・ 好發：${issue.mileage_range}</span>
          </div>
          <div class="issue-meta">
            <div><strong>常見症狀：</strong>${issue.symptom}</div>
            <div><strong>預估維修費用：</strong><span style="color:#fbbf24;">${issue.repair_cost_ntd}</span></div>
            <div><strong>看車避坑建議：</strong><span style="color:#34d399;">${issue.advice}</span></div>
          </div>
        </div>
      `;
    })
    .join("");
}

function renderChart() {
  const car = getCurrentCar();
  state.chart.setData(car.timeline, state.chartMode);
}

function populateCalculatorYears() {
  const car = getCurrentCar();
  const sel = document.getElementById("calcYear");
  sel.innerHTML = car.timeline
    .map((pt, idx) => `<option value="${idx}">${pt.year} 年式 (${pt.gen_name})</option>`)
    .join("");
  // 預設選中間偏新的年份
  sel.value = Math.max(0, car.timeline.length - 3);
}

function updateValuationCalculator() {
  const car = getCurrentCar();
  if (!car || !car.timeline.length) return;

  const idx = parseInt(document.getElementById("calcYear").value, 10) || 0;
  const pt = car.timeline[idx] || car.timeline[0];
  const mileageWan = parseFloat(document.getElementById("calcMileage").value) || 0;
  const conditionFactor = parseFloat(document.getElementById("calcCondition").value) || 1.0;

  // 台灣市場基準：每年合理行駛約 1.2 萬公里
  const expectedMileage = pt.age_years * 1.2;
  const mileageDiff = mileageWan - expectedMileage;
  // 每多/少 1 萬公里約影響 ±1.2% 車價（上限 ±15%）
  const mileageFactor = Math.max(0.85, Math.min(1.12, 1 - mileageDiff * 0.012));

  const estDealer = (pt.dealer * mileageFactor * conditionFactor).toFixed(1);
  const estPrivate = (pt.private * mileageFactor * conditionFactor).toFixed(1);
  const estBook = (pt.book * mileageFactor * conditionFactor).toFixed(1);
  const estReserve = pt.alert_level === "high" ? "建議預留 3.5 ~ 6.0 萬" : pt.alert_level === "medium" ? "建議預留 1.5 ~ 3.0 萬" : "建議預留 0.5 ~ 1.5 萬";

  document.getElementById("calcResults").innerHTML = `
    <div class="metric-box">
      <div class="metric-label">預估認證車商合理售價</div>
      <div class="metric-value" style="color:var(--accent-blue);">${estDealer} 萬</div>
      <div class="metric-sub">含整備與聯盟保固參考</div>
    </div>
    <div class="metric-box">
      <div class="metric-label">預估非第三方民間自售實價</div>
      <div class="metric-value" style="color:var(--accent-green);">${estPrivate} 萬</div>
      <div class="metric-sub">車友/自售直接過戶水位</div>
    </div>
    <div class="metric-box">
      <div class="metric-label">權威車訊(天書)收購參考</div>
      <div class="metric-value" style="color:var(--accent-orange);">${estBook} 萬</div>
      <div class="metric-sub">銀行貸款/車商估收基準</div>
    </div>
    <div class="metric-box">
      <div class="metric-label">購後整修與通病預留金</div>
      <div class="metric-value" style="font-size:1.05rem;color:var(--accent-yellow);margin-top:8px;">${estReserve}</div>
      <div class="metric-sub">該年份合理里程基準：約 ${expectedMileage.toFixed(1)} 萬 km</div>
    </div>
  `;
}

function renderHistoryTable() {
  const car = getCurrentCar();
  const tbody = document.getElementById("historyTableBody");
  tbody.innerHTML = car.timeline
    .map((pt) => {
      const majorBadge = pt.is_major_change ? `<span class="badge-major">大改款</span>` : "";
      const riskBadge =
        pt.alert_level === "high"
          ? `<span class="sev-badge high">高風險</span>`
          : pt.alert_level === "medium"
          ? `<span class="sev-badge med">留意通病</span>`
          : `<span class="sev-badge low">穩健</span>`;
      return `
        <tr class="${pt.is_major_change ? "row-major" : ""}">
          <td><strong>${pt.year}</strong> ${majorBadge}</td>
          <td>${pt.gen_name}</td>
          <td>${pt.msrp.toFixed(1)} 萬</td>
          <td style="color:var(--accent-blue);font-weight:700;">${pt.dealer.toFixed(1)} 萬</td>
          <td style="color:var(--accent-green);font-weight:700;">${pt.private.toFixed(1)} 萬</td>
          <td style="color:var(--accent-orange);">${pt.book.toFixed(1)} 萬</td>
          <td>+${pt.dealer_private_spread_wan.toFixed(1)} 萬 (${pt.dealer_private_spread_pct}%)</td>
          <td>${pt.residual_dealer_pct}% / ${pt.residual_private_pct}%</td>
          <td>${pt.avg_annual_depreciation_wan} 萬/年</td>
          <td>${riskBadge}</td>
        </tr>
      `;
    })
    .join("");
}

function renderDataSources() {
  const el = document.getElementById("sourcesGrid");
  el.innerHTML = state.db.data_sources
    .map(
      (s) => `
      <div class="source-card">
        <h4>${s.name}</h4>
        <div class="source-type">${s.type} ・ 公信力：${s.credibility}</div>
        <p>${s.description}</p>
      </div>
    `
    )
    .join("");
}

document.addEventListener("DOMContentLoaded", initApp);
