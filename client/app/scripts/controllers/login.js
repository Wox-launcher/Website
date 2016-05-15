'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
.controller('LoginCtrl', function ($scope,$location,api,notify,auth,redirectUrlAfterLogin) {
    $scope.login = function(){
        api.post('/auth/login/', {
            username:$scope.name,
            password:$scope.password
        })
        .success(function(data, status, headers, config) {
            auth.login(data.data);
            $location.path(redirectUrlAfterLogin.url);
        });
    };
});
