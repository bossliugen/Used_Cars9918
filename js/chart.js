/**
 * 台灣中古車時價分析互動式 Canvas 圖表引擎
 * 支援：高解析度 Retina 繪製、大改款年份垂直標記、高風險通病區間底色警示、多曲線切換與 Hover Tooltip
 */

class MarketTrendChart {
  constructor(canvasId, tooltipId) {
    this.canvas = document.getElementById(canvasId);
    this.tooltip = document.getElementById(tooltipId);
    this.ctx = this.canvas.getContext("2d");
    this.timeline = [];
    this.mode = "price"; // 'price' | 'residual'
    this.hoverIndex = -1;
    this.pointsMeta = [];

    this._bindEvents();
  }

  setData(timeline, mode = "price") {
    this.timeline = timeline || [];
    this.mode = mode;
    this.hoverIndex = -1;
    this.render();
  }

  _bindEvents() {
    window.addEventListener("resize", () => this.render());

    this.canvas.addEventListener("mousemove", (e) => {
      if (!this.pointsMeta.length) return;
      const rect = this.canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;

      let closestIdx = -1;
      let minDist = Infinity;
      this.pointsMeta.forEach((pt, idx) => {
        const d = Math.abs(pt.x - mx);
        if (d < minDist) {
          minDist = d;
          closestIdx = idx;
        }
      });

      if (closestIdx !== -1 && minDist < 48) {
        if (this.hoverIndex !== closestIdx) {
          this.hoverIndex = closestIdx;
          this.render();
        }
        this._showTooltip(this.pointsMeta[closestIdx], e.clientX - rect.left, e.clientY - rect.top, rect.width);
      } else if (this.hoverIndex !== -1) {
        this.hoverIndex = -1;
        this.tooltip.style.display = "none";
        this.render();
      }
    });

    this.canvas.addEventListener("mouseleave", () => {
      this.hoverIndex = -1;
      this.tooltip.style.display = "none";
      this.render();
    });
  }

  _showTooltip(ptMeta, mouseX, mouseY, containerWidth) {
    const d = ptMeta.data;
    const majorTag = d.is_major_change
      ? `<span style="color:#a78bfa;font-weight:700;"> ★ 大改款/新世代</span>`
      : "";
    const riskTag =
      d.alert_level === "high"
        ? `<div style="color:#f87171;font-size:0.75rem;margin-top:3px;">⚠ 高風險通病/殘值劇降區間</div>`
        : d.alert_level === "medium"
        ? `<div style="color:#fb923c;font-size:0.75rem;margin-top:3px;">● 需留意特定通病</div>`
        : "";

    this.tooltip.innerHTML = `
      <div style="font-weight:700;font-size:0.88rem;margin-bottom:4px;">
        ${d.year} 年式${majorTag}
      </div>
      <div style="color:#94a3b8;font-size:0.76rem;margin-bottom:6px;">${d.gen_name}</div>
      <div style="display:grid;grid-template-columns:1fr auto;gap:3px 14px;font-size:0.79rem;">
        <span style="color:#a78bfa;">當年新車 MSRP：</span><strong>${d.msrp.toFixed(1)} 萬</strong>
        <span style="color:#38bdf8;">認證車商均價：</span><strong>${d.dealer.toFixed(1)} 萬 (${d.residual_dealer_pct}%)</strong>
        <span style="color:#34d399;">非第三方自售實價：</span><strong>${d.private.toFixed(1)} 萬 (${d.residual_private_pct}%)</strong>
        <span style="color:#fb923c;">權威天書基準價：</span><strong>${d.book.toFixed(1)} 萬 (${d.residual_book_pct}%)</strong>
        <span style="color:#94a3b8;">車商 / 自售價差：</span><span>+${d.dealer_private_spread_wan.toFixed(1)} 萬 (${d.dealer_private_spread_pct}%)</span>
      </div>
      ${riskTag}
    `;

    this.tooltip.style.display = "block";
    const tipW = this.tooltip.offsetWidth || 230;
    const left = mouseX + 16 + tipW > containerWidth ? mouseX - tipW - 14 : mouseX + 14;
    const top = Math.max(10, mouseY - 40);
    this.tooltip.style.left = `${left}px`;
    this.tooltip.style.top = `${top}px`;
  }

  render() {
    const parent = this.canvas.parentElement;
    if (!parent) return;

    const width = parent.clientWidth;
    const height = parent.clientHeight;
    const dpr = window.devicePixelRatio || 1;

    this.canvas.width = width * dpr;
    this.canvas.height = height * dpr;
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const ctx = this.ctx;
    ctx.clearRect(0, 0, width, height);

    if (!this.timeline.length) return;

    const pad = { top: 34, right: 26, bottom: 42, left: 54 };
    const plotW = width - pad.left - pad.right;
    const plotH = height - pad.top - pad.bottom;

    // 計算 Y 軸上下限
    let maxVal = 0;
    if (this.mode === "price") {
      this.timeline.forEach((d) => {
        maxVal = Math.max(maxVal, d.msrp, d.dealer, d.private, d.book);
      });
      maxVal = Math.ceil(maxVal / 20) * 20;
    } else {
      maxVal = 100;
    }
    const minVal = 0;

    const xAt = (i) => {
      if (this.timeline.length === 1) return pad.left + plotW / 2;
      return pad.left + (i / (this.timeline.length - 1)) * plotW;
    };
    const yAt = (v) => pad.top + plotH - ((v - minVal) / (maxVal - minVal)) * plotH;

    // 1. 高風險區間背景著色
    this.timeline.forEach((d, i) => {
      if (d.alert_level === "high") {
        const x = xAt(i);
        const step = this.timeline.length > 1 ? plotW / (this.timeline.length - 1) : plotW;
        const leftX = Math.max(pad.left, x - step / 2);
        const rightX = Math.min(pad.left + plotW, x + step / 2);
        ctx.fillStyle = "rgba(248, 113, 113, 0.11)";
        ctx.fillRect(leftX, pad.top, rightX - leftX, plotH);
      }
    });

    // 2. 水平格線與 Y 軸刻度
    const ticks = 5;
    ctx.font = "11px sans-serif";
    ctx.textAlign = "right";
    ctx.textBaseline = "middle";
    for (let t = 0; t <= ticks; t++) {
      const val = minVal + ((maxVal - minVal) * t) / ticks;
      const y = yAt(val);
      ctx.strokeStyle = "rgba(148, 163, 184, 0.14)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(pad.left, y);
      ctx.lineTo(pad.left + plotW, y);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      const label = this.mode === "price" ? `${Math.round(val)}萬` : `${Math.round(val)}%`;
      ctx.fillText(label, pad.left - 8, y);
    }

    // 3. 大改款年份垂直虛線與標籤
    this.timeline.forEach((d, i) => {
      if (d.is_major_change) {
        const x = xAt(i);
        ctx.save();
        ctx.strokeStyle = "rgba(167, 139, 250, 0.55)";
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(x, pad.top);
        ctx.lineTo(x, pad.top + plotH);
        ctx.stroke();
        ctx.restore();

        ctx.fillStyle = "#c4b5fd";
        ctx.font = "bold 11px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(`★ 大改款 ${d.year}`, x, pad.top - 14);
      }
    });

    // 4. X 軸年份標籤
    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    this.timeline.forEach((d, i) => {
      const x = xAt(i);
      // 避免標籤過度擁擠
      if (this.timeline.length <= 14 || i % 2 === 0 || d.is_major_change || i === this.timeline.length - 1) {
        ctx.fillText(String(d.year), x, pad.top + plotH + 10);
      }
    });

    // 5. 繪製折線函式
    const drawLine = (key, color, dashed = false, lineWidth = 2.5) => {
      ctx.save();
      ctx.strokeStyle = color;
      ctx.lineWidth = lineWidth;
      if (dashed) ctx.setLineDash([6, 4]);
      ctx.beginPath();
      this.timeline.forEach((d, i) => {
        const x = xAt(i);
        const y = yAt(d[key]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.stroke();
      ctx.restore();

      // 節點圓點
      this.timeline.forEach((d, i) => {
        const x = xAt(i);
        const y = yAt(d[key]);
        ctx.beginPath();
        ctx.arc(x, y, this.hoverIndex === i ? 5 : 3.2, 0, Math.PI * 2);
        ctx.fillStyle = color;
        ctx.fill();
      });
    };

    if (this.mode === "price") {
      drawLine("msrp", "#a78bfa", true, 1.8);
      drawLine("book", "#fb923c", true, 2.0);
      drawLine("private", "#34d399", false, 2.6);
      drawLine("dealer", "#38bdf8", false, 2.8);
    } else {
      drawLine("residual_book_pct", "#fb923c", true, 2.0);
      drawLine("residual_private_pct", "#34d399", false, 2.6);
      drawLine("residual_dealer_pct", "#38bdf8", false, 2.8);
    }

    // 6. Hover 垂直準線
    if (this.hoverIndex >= 0 && this.hoverIndex < this.timeline.length) {
      const hx = xAt(this.hoverIndex);
      ctx.save();
      ctx.strokeStyle = "rgba(241, 245, 249, 0.35)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(hx, pad.top);
      ctx.lineTo(hx, pad.top + plotH);
      ctx.stroke();
      ctx.restore();
    }

    // 更新點位供滑鼠偵測
    this.pointsMeta = this.timeline.map((d, i) => ({
      x: xAt(i),
      data: d,
    }));
  }
}
