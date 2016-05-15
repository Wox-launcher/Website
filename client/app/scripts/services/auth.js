'use strict';

/**
 * @ngdoc service
 * @name woxApp.auth
 * @description
 * # auth
 * Factory in the woxApp.
 */
angular.module('woxApp')
.factory('auth', function ($rootScope,$cookieStore,$location,redirectUrlAfterLogin) {
    var user = null;

    function setRedirectUrl(){
        if($location.path().toLowerCase() != '/login') {
            redirectUrlAfterLogin.url = $location.path();
        }
        else{
            redirectUrlAfterLogin.url = '/';
        }
    }

    return{
        login: function(u){
            user = u;
            $cookieStore.put("user",user);
            $rootScope.logined = true;
            $rootScope.user = user;
        },
        logout: function(){
            setRedirectUrl();
            $location.path("/logout");
        },
        clearUser: function(){
            $cookieStore.remove("user");
            $rootScope.logined = false;
            $rootScope.user = null;
            user = null;
        },
        isAuth : function(){
            if(user == null){
                user = $cookieStore.get("user"); 
            }
            return user != null;
        },
        isSuperUser: function(){
            return user != null && user.isSuperUser;
        },
        getUser: function(){
            return user;
        },
        setRedirectUrlAfterLogin: function(){
           setRedirectUrl();
        }
    };
});
