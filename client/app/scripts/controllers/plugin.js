'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:PluginCtrl
 * @description
 * # PluginCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('PluginCtrl', function ($scope, api, $location, plugins, allPluginCount, paginate) {

        var page_size = $location.search().page_size || paginate;
        $scope.plugins = plugins.results;
        $scope.allPluginCount = allPluginCount;
        $scope.search = "";
        $scope.currentPage = 1;
        $scope.totalPage = Math.ceil(plugins.count / page_size);

        $scope.likePlugin = function (plugin) {
            api.post("/plugin/" + plugin.id + "/like/").success(function (r) {
                plugin.liked_count = r.data.latest_like_count;
                plugin.liked_by_logined_user = !plugin.liked_by_logined_user;
            });
        };

        function getAllPlugins() {
            api.get("/plugin/?page=" + $scope.currentPage + "&page_size=" + page_size).success(function (data) {
                $scope.plugins = data.results;
                $scope.totalPage = Math.ceil(data.count / page_size);
            });
            $scope.allPluginCount = allPluginCount;
        }

        $scope.prevPage = function () {
            if ($scope.currentPage > 1) {
                $scope.currentPage--;
            }
            $scope.searchPlugin();
        };

        $scope.nextPage = function () {
            if ($scope.currentPage < $scope.totalPage) {
                $scope.currentPage++;
            }
            $scope.searchPlugin();
        };

        $scope.searchPlugin = function () {
            if ($scope.search == "") {
                getAllPlugins();
                return;
            }

            api.get("/plugin/search/" + $scope.search + "/").success(function (data) {
                $scope.currentPage = 1;
                $scope.totalPage = 1;
                $scope.plugins = data;
            });
        };

        $scope.uploadPlugin = function () {
            $location.path("/plugin/create");
        };
    });
