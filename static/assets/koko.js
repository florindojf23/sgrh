"use strict";

var KTWidgets = {
    init: function () {
        // ... existing code ...

        // Fetch data from the API
        fetch('/api/c/g/equipments/condition/summary/')
            .then(response => response.json())
            .then(data => {
                // Assuming the API response has a structure like { "NetProfit": [44, 55, 57, 56, 61, 58], "Revenue": [76, 85, 101, 98, 87, 105] }
                var chartData = Object.keys(data).map(name => ({ name, data: data[name] }));

                // Create the chart using the fetched data
                var chartElement = document.getElementById("kt_charts_widget_2_chart");
                var chartHeight = parseInt(KTUtil.css(chartElement, "height"));
                var dangerColor = KTUtil.getCssVariableValue("--bs-danger");
                var infoColor = KTUtil.getCssVariableValue("--bs-info-300");

                new ApexCharts(chartElement, {
                    series: chartData,
                    // ... other chart options ...
                    colors: [dangerColor, infoColor],
                    // ... other chart options ...
                }).render();
            })
            .catch(error => console.error('Error fetching data:', error));
    }
};

"undefined" !== typeof module && (module.exports = KTWidgets);

KTUtil.onDOMContentLoaded(function () {
    KTWidgets.init();
});
