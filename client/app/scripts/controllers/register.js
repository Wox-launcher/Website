'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:RegisterCtrl
 * @description
 * # RegisterCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('RegisterCtrl', function ($scope, notify,api,$location) {
        $scope.register = function () {
            api.post('/auth/register/', {
                username: $scope.name,
                email: $scope.email,
                password: $scope.password
            })
                .success(function (data, status, headers, config) {
                    notify.success("Succeed. Login in now");
                    $location.path("/login");
                });
        };
    });
