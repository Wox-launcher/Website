'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
