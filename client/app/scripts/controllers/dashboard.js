'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:DashboardCtrl
 * @description
 * # DashboardCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
.controller('DashboardCtrl', function ($scope,api) {

    api.get("/dashboard/upgrade_request_today/").then(
        function success(r) {
            renderUpgradeRequestToday(r.data);
        }
    );

    api.get("/dashboard/upgrade_request_current_month/").then(
        function success(r) {
            renderUpgradeRequestMonth(r.data);
        }
    );
    api.get("/dashboard/summary/").then(
        function success(r) {
            $scope.summary = r.data;
        }
    );

    function renderUpgradeRequestToday(upgrade_request_today) {
        var myChart = echarts.init(document.getElementById('upgrade-request-today'));

        if (upgrade_request_today.length == 0) {
            upgrade_request_today = [];
            for (var j = 0; j < 25; j++) {
                upgrade_request_today.push({hour: j, count: 0});
            }
        }

        var xAxisData = [];
        var yAxisData = [];
        for (var i in upgrade_request_today) {
            xAxisData.push(upgrade_request_today[i].hour.toString() + "h");
            yAxisData.push(upgrade_request_today[i].count);
        }

        var option = {
            grid: {
                x: 60,
                y: 20,
                x2: 20,
                y2: 40
            },
            tooltip: {
                show: true
            },
            xAxis: [
                {
                type: 'category',
                data: xAxisData
            }
            ],
            yAxis: [
                {
                type: 'value'
            }
            ],
            series: [
                {
                "name": "Upgrade request today",
                "type": "line",
                "smooth": true,
                "data": yAxisData
            }
            ]
        };

        myChart.setOption(option);
    }

    function renderUpgradeRequestMonth(upgrade_request_month) {
        var myChart = echarts.init(document.getElementById('upgrade-request-month'));

        if (upgrade_request_month.length == 0) {
            upgrade_request_month = [];
            var now = new Date();
            var daysInCurrentMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0).getDate();
            for (var j = 0; j <= daysInCurrentMonth; j++) {
                upgrade_request_month.push({day: j, count: 0});
            }
        }

        var xAxisData = [];
        var yAxisData = [];
        for (var i in upgrade_request_month) {
            xAxisData.push(upgrade_request_month[i].day.toString() + "d");
            yAxisData.push(upgrade_request_month[i].count);
        }

        var option = {
            grid: {
                x: 60,
                y: 20,
                x2: 20,
                y2: 40
            },
            tooltip: {
                show: true
            },
            xAxis: [
                {
                type: 'category',
                data: xAxisData
            }
            ],
            yAxis: [
                {
                type: 'value'
            }
            ],
            series: [
                {
                "name": "Upgrade request this month",
                "type": "line",
                "smooth": true,
                "data": yAxisData
            }
            ]
        };

        myChart.setOption(option);
    }

});
