'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:ReleaseCtrl
 * @description
 * # ReleaseCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
  .controller('ReleaseCtrl', function ($scope,releases,auth,$location) {
        $scope.releases = releases;
        $scope.isSuperUser = auth.isSuperUser();


        $scope.createNewRelease = function(){
           $location.path("/release/create"); 
        };
  });
