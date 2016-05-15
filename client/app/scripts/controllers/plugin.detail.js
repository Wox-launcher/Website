'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:PlugindetailCtrl
 * @description
 * # PlugindetailCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('PlugindetailCtrl', function ($scope, api, auth, plugin) {

        $scope.plugin = plugin;

        //sharethis button
        if(typeof stButtons !== "undefined") stButtons.makeButtons();

        $scope.likePlugin = function (plugin) {
            api.post("/plugin/" + plugin.id + "/like/").success(function (r) {
                plugin.liked_count = r.data.latest_like_count;
                plugin.liked_by_logined_user = !plugin.liked_by_logined_user;
            });
        };
    });
