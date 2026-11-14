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
  detailsOpen: false,
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
        <h2 style="color:#dc2626;">無法載入資料庫 (data/cars_db.json)</h2>
        <p style="margin-top:8px;color:#475569;">請雙擊 <strong>啟動中古車分析網站.bat</strong> 或透過 GitHub Pages 開啟。</p>
      </div>
    `;
    return;
  }

  state.brands = [...new Set(state.db.cars.map((c) => c.brand))];
  document.getElementById("headerMetaChip").textContent =
    `${state.brands.length} 品牌 ・ ${state.db.meta.total_models} 車系 ・ ${state.db.meta.total_year_records} 筆年式`;

  renderBrandControls();
  renderRankingTable();
  bindEvents();

  // 預設選 Ford Focus 2014（直接展示大改款與雙離合案例）或第一台
  const defaultCar = state.db.cars.find((c) => c.id === "ford-focus") || state.db.cars[0];
  selectBrand(defaultCar.brand, defaultCar.id);
}

function bindEvents() {
  document.getElementById("selectBrand").addEventListener("change", (e) => {
    selectBrand(e.target.value);
  });

  document.getElementById("selectModel").addEventListener("change", (e) => {
    selectCar(e.target.value);
  });

  document.getElementById("selectYear").addEventListener("change", (e) => {
    state.selectedYear = parseInt(e.target.value, 10);
    state.selectedTrimIdx = 0;
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
    document.getElementById(id).addEventListener("input", renderHeroAndKpis);
    document.getElementById(id).addEventListener("change", renderHeroAndKpis);
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

  document.getElementById("btnToggleDetails").addEventListener("click", () => {
    state.detailsOpen = !state.detailsOpen;
    const wrapper = document.getElementById("detailsWrapper");
    const btn = document.getElementById("btnToggleDetails");
    wrapper.classList.toggle("hidden", !state.detailsOpen);
    btn.textContent = state.detailsOpen ? "收合詳細資料 ▴" : "展開詳細資料 ▾";
    if (state.detailsOpen) renderDetailBody();
  });

  document.querySelectorAll(".detail-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.activeDetailTab = btn.dataset.tab;
      document.querySelectorAll(".detail-tab").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderDetailBody();
    });
  });

  document.getElementById("btnToggleRanking").addEventListener("click", () => {
    document.getElementById("rankingPanel").classList.toggle("open");
  });

  document.getElementById("btnCloseRanking").addEventListener("click", () => {
    document.getElementById("rankingPanel").classList.remove("open");
  });
}

function renderBrandControls() {
  const selBrand = document.getElementById("selectBrand");
  selBrand.innerHTML = state.brands.map((b) => `<option value="${b}">${b}</option>`).join("");

  const pillsEl = document.getElementById("brandPills");
  pillsEl.innerHTML = state.brands
    .map((b) => `<button class="brand-pill" data-brand="${b}" onclick="selectBrand('${b}')">${getBrandLogoSvg(b)}<span>${b}</span></button>`)
    .join("");
}

function selectBrand(brand, preferredCarId = null) {
  state.selectedBrand = brand;
  document.getElementById("selectBrand").value = brand;

  document.querySelectorAll(".brand-pill").forEach((p) => {
    p.classList.toggle("active", p.dataset.brand === brand);
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

  renderAllCarViews();
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
  renderHeroAndKpis();
  renderPhotoStrip();
  updateChartLegendAndButtons();
  renderChart();
  renderQuickSpecs();
  if (state.detailsOpen) renderDetailBody();
}

function renderHeroAndKpis() {
  const car = getCurrentCar();
  const pt = getSelectedPoint();
  const gen = getSelectedGen();
  const trim = gen.trims[state.selectedTrimIdx] || gen.trims[0];

  document.getElementById("heroTitle").innerHTML = `
    ${getBrandLogoSvg(car.brand, true)}
    <span>${car.brand} ${car.model} ・ ${pt.year} 年式</span>
    <span class="tag-blue">${gen.gen_name}</span>
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

  // 里程與車況微調係數
  const mileageWan = parseFloat(document.getElementById("inputMileage").value) || 0;
  const condFactor = parseFloat(document.getElementById("selectCondition").value) || 1.0;
  const expectedMileage = pt.age_years * 1.2;
  const mileageFactor = Math.max(0.85, Math.min(1.12, 1 - (mileageWan - expectedMileage) * 0.012));

  const dealerVal = (pt.dealer * mileageFactor * condFactor).toFixed(1);
  const privateVal = (pt.private * mileageFactor * condFactor).toFixed(1);
  const bookVal = (pt.book * mileageFactor * condFactor).toFixed(1);

  document.getElementById("mileageHint").textContent =
    `該年式合理參考里程：約 ${expectedMileage.toFixed(1)} 萬 km（當年新車價 ${pt.msrp.toFixed(1)} 萬）`;

  document.getElementById("kpiGrid").innerHTML = `
    <div class="kpi-box primary">
      <div class="kpi-label">認證車商合理售價 (8891/SUM/ABC)</div>
      <div class="kpi-value" style="color:var(--blue-dark);">${dealerVal} 萬</div>
      <div class="kpi-sub">殘值率 ${pt.residual_dealer_pct}% ・ 含整理與保固</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">非第三方民間自售實價 (PTT/社團)</div>
      <div class="kpi-value" style="color:var(--green);">${privateVal} 萬</div>
      <div class="kpi-sub">車商價差約 +${pt.dealer_private_spread_wan.toFixed(1)} 萬</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">權威車訊 (天書) 收購基準</div>
      <div class="kpi-value" style="color:var(--orange);">${bookVal} 萬</div>
      <div class="kpi-sub">銀行貸款與車商估收錨點</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">年度稅金 (牌照+燃料費)</div>
      <div class="kpi-value" style="color:var(--text-main);">${trim.annual_tax_ntd.toLocaleString()} 元</div>
      <div class="kpi-sub">${trim.displacement_cc} cc ・ 年均折舊 ${pt.avg_annual_depreciation_wan} 萬/年</div>
    </div>
  `;
}

function updateChartLegendAndButtons() {
  document.getElementById("btnModePrice").classList.toggle("active", state.chartMode === "price");
  document.getElementById("btnModeResidual").classList.toggle("active", state.chartMode === "residual");

  const legend = document.getElementById("chartLegend");
  if (state.chartMode === "price") {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-line" style="background:#94a3b8;"></span>當年新車 MSRP</span>
      <span class="legend-item"><span class="legend-line" style="background:#2563eb;"></span>認證車商均價</span>
      <span class="legend-item"><span class="legend-line" style="background:#10b981;"></span>非第三方民間自售實價</span>
      <span class="legend-item"><span class="legend-line" style="background:#f59e0b;"></span>權威天書基準</span>
    `;
  } else {
    legend.innerHTML = `
      <span class="legend-item"><span class="legend-line" style="background:#2563eb;"></span>車商殘值率 (%)</span>
      <span class="legend-item"><span class="legend-line" style="background:#10b981;"></span>民間自售殘值率 (%)</span>
      <span class="legend-item"><span class="legend-line" style="background:#f59e0b;"></span>天書殘值率 (%)</span>
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
          <img id="img-${g.gen_id}" class="gen-photo-thumb" alt="${car.brand} ${car.model} ${g.gen_name}" />
          <div class="gen-photo-body">
            <div class="gen-photo-name">${g.gen_name}</div>
            <div class="gen-photo-years">${yr}</div>
            <div class="gen-photo-credit" id="credit-${g.gen_id}">圖片來源：Wikimedia Commons 載入中...</div>
          </div>
        </div>
      `;
    })
    .join("");

  car.generations.forEach((g) => loadGenPhoto(g));
}

async function loadGenPhoto(gen) {
  const imgEl = document.getElementById(`img-${gen.gen_id}`);
  const creditEl = document.getElementById(`credit-${gen.gen_id}`);
  if (!imgEl || !creditEl) return;

  const query = gen.photo_query || gen.gen_name;
  const cacheKey = `wiki_photo_v1_${query}`;

  try {
    const cached = localStorage.getItem(cacheKey);
    if (cached) {
      const parsed = JSON.parse(cached);
      imgEl.src = parsed.url;
      creditEl.innerHTML = `出處：<a href="${parsed.pageUrl}" target="_blank" rel="noopener" onclick="event.stopPropagation()">Wikimedia (${parsed.license})</a>`;
      return;
    }

    const apiUrl = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch=${encodeURIComponent(
      query
    )}&gsrlimit=5&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=480&format=json&origin=*`;
    const resp = await fetch(apiUrl);
    const data = await resp.json();
    const pages = data?.query?.pages ? Object.values(data.query.pages) : [];

    // 過濾出真正的照片檔 (jpg/jpeg/png)
    const valid = pages.find((p) => {
      const title = (p.title || "").toLowerCase();
      return (title.endsWith(".jpg") || title.endsWith(".jpeg") || title.endsWith(".png")) && p.imageinfo?.[0]?.thumburl;
    });

    if (valid) {
      const info = valid.imageinfo[0];
      const license = info.extmetadata?.LicenseShortName?.value || "CC";
      const pageUrl = info.descriptionurl || `https://commons.wikimedia.org/wiki/${encodeURIComponent(valid.title)}`;
      const result = { url: info.thumburl, license, pageUrl };
      localStorage.setItem(cacheKey, JSON.stringify(result));
      imgEl.src = result.url;
      creditEl.innerHTML = `出處：<a href="${result.pageUrl}" target="_blank" rel="noopener" onclick="event.stopPropagation()">Wikimedia (${result.license})</a>`;
    } else {
      creditEl.textContent = "暫無外型圖（請點此切換世代）";
    }
  } catch (e) {
    creditEl.textContent = "圖片來源：Wikimedia Commons";
  }
}

function renderChart() {
  const car = getCurrentCar();
  state.chart.setData(car.timeline, state.chartMode, state.selectedYear);
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

function renderDetailBody() {
  const body = document.getElementById("detailBody");
  const car = getCurrentCar();
  const gen = getSelectedGen();

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
  renderHeroAndKpis();
  renderQuickSpecs();
  renderDetailBody();
}

function jumpToGen(genId) {
  const car = getCurrentCar();
  const gen = car.generations.find((g) => g.gen_id === genId);
  if (gen && gen.years.length) {
    state.selectedYear = gen.years[0];
    document.getElementById("selectYear").value = String(state.selectedYear);
    state.selectedTrimIdx = 0;
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
  document.getElementById("rankingPanel").classList.remove("open");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.addEventListener("DOMContentLoaded", initApp);
