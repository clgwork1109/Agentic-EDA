function renderHistogram(containerId, option) {
  const chart = echarts.init(document.getElementById(containerId));
  chart.setOption(option);
}

function renderCorrelation(containerId, correlation) {
  const chart = echarts.init(document.getElementById(containerId));

  chart.setOption({
    tooltip: {},
    xAxis: { type: "category", data: correlation.columns },
    yAxis: { type: "category", data: correlation.columns },
    visualMap: {
      min: -1,
      max: 1,
      calculable: true,
      orient: "horizontal",
      left: "center"
    },
    series: [{
      type: "heatmap",
      data: correlation.matrix
    }]
  });
}
