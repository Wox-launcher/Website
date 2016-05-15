'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:ReleaseCreateCtrl
 * @description
 * # ReleaseCreateCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
.controller('ReleaseCreateCtrl', function ($scope,api,notify,$location) {
    $scope.submitRelease = function(){
        if ($scope.version == null) {
            notify.error("Version is required");
            return;
        }
        if ($scope.desc == null) {
            notify.error("Description is required");
            return;
        } 
        if ($scope.link1 == null) {
            notify.error("Download link is required");
            return;
        } 

        api.post("/release/",{
            "version": $scope.version, 
            "download_link":$scope.link1, 
            "download_link1": $scope.link2, 
            "download_link2": $scope.link3, 
            "description": $scope.desc 
        })
        .success(function (data, status, headers, config) {
            notify.success("Succeed.");
            $location.path("/release");
        });
    }; 
});
