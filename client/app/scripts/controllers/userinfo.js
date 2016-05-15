'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:UserinfoCtrl
 * @description
 * # UserinfoCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
.controller('UserinfoCtrl', function ($scope, api, $routeParams,notify,auth,$location,user) {

    $scope.user = user;
    $scope.activetab= "plugin";

    $scope.deletePlugin = function (plugin) {
        if (confirm("Are you sure you want to delete " + plugin.name + " ?")) {
            api.delete("/plugin/" + plugin.id + "/").success(function (data) {
                $scope.user.plugins.splice($scope.user.plugins.indexOf(plugin), 1);
            });
        }
    };

    $scope.likePlugin = function (plugin) {
        api.post("/plugin/" + plugin.id + "/like/").success(function (r) {
            plugin.liked_count = r.data.latest_like_count;
            plugin.liked_by_logined_user = !plugin.liked_by_logined_user;
        });
    };

    $scope.switchTabPane = function(tab){
        $scope.activetab = tab;
    };

    $scope.updatePwd = function(){
        if($scope.newpwd != $scope.newpwd2){
            notify.error("new password don't match with confirm password");
            return;
        }

        api.post("/auth/changepwd/",{
            "oldpwd": $scope.oldpwd,
            "newpwd": $scope.newpwd
        }).success(function (data) {
            notify.success("succeed, please re-login");
            auth.logout(); 
        });
    };
});
