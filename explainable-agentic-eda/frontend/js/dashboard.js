async function runEDA() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  if (!file) return alert("Select a file");

  const upload = await uploadDataset(file);
  const job = await runEDAJob(upload.dataset_id);
  const result = await getResults(job.job_id);

  renderDashboard(result);
}

function renderDashboard(data) {
    console.log("EDA RESULT:", data);
  // KPIs
  const kpis = document.getElementById("kpis");
  kpis.innerHTML = `
    <div class="kpi">Rows<br><strong>${data.agents.dataset_understanding.rows}</strong></div>
    <div class="kpi">Columns<br><strong>${data.agents.dataset_understanding.columns}</strong></div>
    <div class="kpi">Missing %<br><strong>${(data.agents.data_quality.missing_ratio*100).toFixed(2)}</strong></div>
  `;

  // Charts
  const charts = document.getElementById("charts");
  charts.innerHTML = "";
  data.charts.forEach((chart, i) => {
    const id = `chart_${i}`;
    charts.innerHTML += `<div id="${id}" class="chart"></div>`;
    renderHistogram(id, chart.echarts_option);
  });

  // Correlation
  renderCorrelation("correlation", data.correlation);

  // Insights
  const insights = document.getElementById("insights");
  insights.innerHTML = "";
  data.agents.insights.forEach(ins => {
    insights.innerHTML += `<div class="insight">${ins.message}</div>`;
  });

  // Debug
  document.getElementById("debug").textContent =
    JSON.stringify(data.agents, null, 2);
}
