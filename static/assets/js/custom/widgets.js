"use strict";
var KTWidgets = {
    init: function() {
        var e, t, a, o, s, r, i, l, n, c, d, h;
        var $kt_charts_widget_3_chart  = $('#kt_charts_widget_3_chart');
        ! function() {
        }(), 
            
            function() {
                var e = document.getElementById("kt_charts_widget_2_chart"),
                    t = parseInt(KTUtil.css(e, "height")),
                    a = KTUtil.getCssVariableValue("--bs-gray-500"),
                    o = KTUtil.getCssVariableValue("--bs-gray-200"),
                    s = KTUtil.getCssVariableValue("--bs-danger"),
                    r = KTUtil.getCssVariableValue("--bs-info-300");
                e && new ApexCharts(e, {
                    series: [{
                        name: "Net Profit",
                        data: [44, 55, 57, 56, 61, 58]
                    }, {
                        name: "Revenue",
                        data: [76, 85, 101, 98, 87, 105]
                    }],
                    chart: {
                        fontFamily: "inherit",
                        type: "bar",
                        height: t,
                        toolbar: {
                            show: !1
                        }
                    },
                    plotOptions: {
                        bar: {
                            horizontal: !1,
                            columnWidth: ["70%"],
                            borderRadius: 4
                        }
                    },
                    legend: {
                        show: 1
                    },
                    dataLabels: {
                        enabled: !1
                    },
                    stroke: {
                        show: !0,
                        width: 2,
                        colors: ["transparent"]
                    },
                    xaxis: {
                        categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                        axisBorder: {
                            show: !1
                        },
                        axisTicks: {
                            show: !1
                        },
                        labels: {
                            style: {
                                colors: a,
                                fontSize: "12px"
                            }
                        }
                    },
                    yaxis: {
                        labels: {
                            style: {
                                colors: a,
                                fontSize: "12px"
                            }
                        }
                    },
                    fill: {
                        opacity: 1
                    },
                    states: {
                        normal: {
                            filter: {
                                type: "none",
                                value: 0
                            }
                        },
                        hover: {
                            filter: {
                                type: "none",
                                value: 0
                            }
                        },
                        active: {
                            allowMultipleDataPointsSelection: !1,
                            filter: {
                                type: "none",
                                value: 0
                            }
                        }
                    },
                    tooltip: {
                        style: {
                            fontSize: "12px"
                        },
                        y: {
                            formatter: function(e) {
                                return "$" + e + " thousands"
                            }
                        }
                    },
                    colors: [s, r],
                    grid: {
                        borderColor: o,
                        strokeDashArray: 4,
                        yaxis: {
                            lines: {
                                show: !0
                            }
                        }
                    }
                }).render();
            }(),

            $.ajax({
                url: $kt_charts_widget_3_chart.data("url"),
                success: 
                function(data) {
                    var e = document.getElementById("$kt_charts_widget_3_chart"),
                        t = parseInt(KTUtil.css(e, "height")),
                        a = KTUtil.getCssVariableValue("--bs-gray-500"),
                        o = KTUtil.getCssVariableValue("--bs-gray-200"),
                        s = KTUtil.getCssVariableValue("--bs-danger"),
                        r = KTUtil.getCssVariableValue("--bs-info-300");
                    // var ctx = $kt_charts_widget_3_chart[0].getContext("2d");
                    e && new ApexCharts(e, {
                        series: [
                        {
                            name: "total ekipamentu",
                            data: data.data
                        }],
                        chart: {
                            fontFamily: "inherit",
                            type: "bar",
                            height: t,
                            toolbar: {
                                show: !1
                            }
                        },
                        plotOptions: {
                            bar: {
                                horizontal: !1,
                                columnWidth: ["70%"],
                                borderRadius: 4
                            }
                        },
                        legend: {
                            show: 1
                        },
                        dataLabels: {
                            enabled: !1
                        },
                        stroke: {
                            show: !0,
                            width: 2,
                            colors: ["transparent"]
                        },
                        xaxis: {
                            categories: data.labels,
                            axisBorder: {
                                show: !1
                            },
                            axisTicks: {
                                show: !1
                            },
                            labels: {
                                style: {
                                    colors: a,
                                    fontSize: "12px"
                                }
                            }
                        },
                        yaxis: {
                            labels: {
                                style: {
                                    colors: a,
                                    fontSize: "12px"
                                }
                            }
                        },
                        fill: {
                            opacity: 1
                        },
                        states: {
                            normal: {
                                filter: {
                                    type: "none",
                                    value: 0
                                }
                            },
                            hover: {
                                filter: {
                                    type: "none",
                                    value: 0
                                }
                            },
                            active: {
                                allowMultipleDataPointsSelection: !1,
                                filter: {
                                    type: "none",
                                    value: 0
                                }
                            }
                        },
                        tooltip: {
                            style: {
                                fontSize: "12px"
                            },
                            y: {
                                formatter: function(e) {
                                    return "$" + e + " thousands"
                                }
                            }
                        },
                        colors: [s, r],
                        grid: {
                            borderColor: o,
                            strokeDashArray: 4,
                            yaxis: {
                                lines: {
                                    show: !0
                                }
                            }
                        }
                    }).render();
                }()
            });
    }
};
"undefined" != typeof module && (module.exports = KTWidgets), KTUtil.onDOMContentLoaded((function() {
    KTWidgets.init()
}));