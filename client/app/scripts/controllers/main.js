'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('MainCtrl', function ($scope, release) {
        $scope.release = release;

        //sharethis button
        if(typeof stButtons !== "undefined") stButtons.makeButtons();
    });
