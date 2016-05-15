'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:ReleaseVersionCtrl
 * @description
 * # ReleaseVersionCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
  .controller('ReleaseVersionCtrl', function ($scope,release) {
        $scope.r = release;
  });
