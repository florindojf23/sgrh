
// 	import Chart from 'chart.js/auto';
// import ChartDataLabels from 'chartjs-plugin-datalabels';

	fetch("{% url 'ChartFuncionarioPivotCASEXO' %}")
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('ChartFuncionarioPivotCASEXO').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: data.datasets
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top'
                    },
                    tooltip: {
                        enabled: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            },
            plugins: [
                {
                    id: 'valueLabelsPlugin',
                    afterDatasetsDraw(chart) {
                        const { ctx, data } = chart;
                        const fontSize = 12;
                        const fontColor = '#000';
                        const fontStyle = 'Arial';

                        // Set font settings
                        ctx.font = `${fontSize}px ${fontStyle}`;
                        ctx.fillStyle = fontColor;
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';

                        // Loop through datasets and their data
                        chart.data.datasets.forEach((dataset, datasetIndex) => {
                            const meta = chart.getDatasetMeta(datasetIndex);
                            meta.data.forEach((bar, index) => {
                                const value = dataset.data[index]; // Get the bar value
                                const x = bar.x; // Bar's x position
                                const y = bar.y; // Bar's y position

                                // Draw the value above the bar
                                ctx.fillText(value, x, y - 10); // Adjust -10 to control spacing
                            });
                        });
                    }
                }
            ]
        });
    })
    .catch(error => console.error('Error fetching chart data:', error));




    fetch("{% url 'ChartFuncionarioPivotTFSEXO' %}")
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('ChartFuncionarioPivotTFSEXO').getContext('2d');
        new Chart(ctx, {
            type: 'line',  // or 'line', 'pie', etc.
            data: {
                labels: data.labels,
                datasets: data.datasets
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            },
            plugins: [
                {
                    id: 'valueLabelsPlugin',
                    afterDatasetDraw(chart) {
                        const { ctx, data } = chart;

                        // Loop through datasets
                        data.datasets.forEach((dataset, datasetIndex) => {
                            const meta = chart.getDatasetMeta(datasetIndex);
                            meta.data.forEach((bar, index) => {
                                const value = dataset.data[index]; // Correct reference
                                const x = bar.x; // Center of the bar
                                const y = bar.y; // Top of the bar

                                // Draw the value
                                ctx.save();
                                ctx.font = '14px Arial';
                                ctx.fillStyle = '#333';
                                ctx.textAlign = 'center';
                                ctx.textBaseline = 'bottom';
                                ctx.fillText(value, x, y - 5); // Adjust position
                                ctx.restore();
                            });
                        });
                    }
                }
            ]
        });
    });

    fetch("{% url 'ChartFuncionarioPivotGISEXO' %}")
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('ChartFuncionarioPivotGISEXO').getContext('2d');
        new Chart(ctx, {
            type: 'bar',  // or 'line', 'pie', etc.
            data: {
                labels: data.labels,
                datasets: data.datasets
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });

    fetch("{% url 'ChartFuncionarioPivotLTSEXO' %}")
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('ChartFuncionarioPivotLTSEXO').getContext('2d');
        new Chart(ctx, {
            type: 'bar',  // or 'line', 'pie', etc.
            data: {
                labels: data.labels,
                datasets: data.datasets
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });

    


