'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:LogoutCtrl
 * @description
 * # LogoutCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
.controller('LogoutCtrl', function ($scope,api,auth,$location) {
    api.post('/auth/logout/').success(function(data) {
        auth.clearUser();
        $location.path("/login");
    }); 
});
