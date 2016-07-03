'use strict';

/**
 * @ngdoc overview
 * @name woxApp
 * @description
 * # woxApp
 *
 * Main module of the application.
 */
angular
    .module('woxApp', [
        'woxAppConfig',
        'angular-loading-bar',
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'angularMoment',
        'angularFileUpload',
        'hc.marked',
        'colorpicker.module'
    ])
    .value('redirectUrlAfterLogin', { url: '/' })
    .config(function ($routeProvider, $locationProvider, $httpProvider, cfpLoadingBarProvider, env) {
        cfpLoadingBarProvider.includeSpinner = false;
        if (env == "prod") {
            $locationProvider.html5Mode(true);
        }

        $routeProvider
            .when('/', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl',
                title: 'Wox',
                resolve: {
                    release: function (api, $route) {
                        return api.get("/release/newest/").then(
                            function success(r) {
                                return r.data;
                            }
                        );
                    }
                }
            })
            .when('/about', {
                title: 'About',
                templateUrl: 'views/about.html',
                controller: 'AboutCtrl'
            })
            .when('/plugin', {
                title: 'Plugin',
                templateUrl: 'views/plugin.html',
                controller: 'PluginCtrl',
                resolve: {
                    plugins: function (api, $location, paginate) {
                        var page_size = $location.search().page_size || paginate;
                        return api.get("/plugin/?page_size=" + page_size).then(
                            function success(r) {
                                return r.data;
                            },
                            function error(r) {
                                return [];
                            }
                        );
                    },
                    allPluginCount: function (api) {
                        return api.get("/plugin/count/").then(
                            function success(r) {
                                return r.data.data.count;
                            },
                            function error(r) {
                                return 0;
                            }
                        );
                    }
                }
            })
            .when('/plugin/create', {
                title: 'Create Plugin',
                templateUrl: 'views/plugin.create.html',
                controller: 'CreatepluginCtrl',
                requiredLogin: true
            })
            .when('/plugin/:id/edit', {
                title: 'Edit Plugin',
                templateUrl: 'views/plugin.edit.html',
                controller: 'PluginEditCtrl',
                requiredLogin: true
            })
            .when('/plugin/:id', {
                title: 'Plugin Detail',
                templateUrl: 'views/plugin.detail.html',
                controller: 'PlugindetailCtrl',
                resolve: {
                    plugin: function (api, $route) {
                        return api.get("/plugin/" + $route.current.params.id + "/").then(
                            function success(r) {
                                return r.data;
                            }
                        );
                    }
                }
            })
            .when('/login', {
                title: 'Login',
                templateUrl: 'views/login.html',
                controller: 'LoginCtrl'
            })
            .when('/register', {
                title: 'Register',
                templateUrl: 'views/register.html',
                controller: 'RegisterCtrl'
            })
            .when('/logout', {
                title: 'Logout',
                templateUrl: 'views/logout.html',
                controller: 'LogoutCtrl'
            })
            .when('/u/:id', {
                title: 'Profile',
                templateUrl: 'views/userinfo.html',
                controller: 'UserinfoCtrl',
                resolve: {
                    user: function (api, $route) {
                        return api.get("/user/" + $route.current.params.id + "/").then(
                            function success(r) {
                                return r.data;
                            }
                        );
                    }
                }
            })
            .when('/theme/builder', {
                title: 'Theme Builder',
                templateUrl: 'views/theme.builder.html',
                controller: 'ThemeBuilderCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });

        $httpProvider.interceptors.push(function ($q, notify, $location, auth, $cookies) {

            function getErrorMsg(responseData) {
                if (typeof responseData.message !== "undefined") {
                    return responseData.message;
                }
                if (typeof responseData.message !== "detail") {
                    return responseData.detail;
                }
            }

            return {
                'request': function (config) {
                    //set csrf header when request any resource
                    config.headers["X-CSRFToken"] = $cookies.csrftoken;
                    return config;
                },
                'responseError': function (rejection) {
                    if (rejection.status == 401) {
                        //login required
                        auth.setRedirectUrlAfterLogin();
                        $location.path("/login");
                    }
                    else if (rejection.status == 500) {
                        notify.error("Server error");
                    }
                    else if (rejection.status >= 400) {
                        notify.error(getErrorMsg(rejection.data));
                    }
                    return $q.reject(rejection);
                }
            };
        });

    })
    .run(function (auth, $rootScope, $http, $cookies, $location, $route, api) {
        $http.defaults.withCredentials = true;
        $rootScope.location = $location;

        api.get("/auth/islogined/").success(function (data) {
            if (data.messsage == "success") {
                auth.login(data.data);
            }
        });

        $rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
            document.title  = current.$$route.title || "Wox";
        });

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            var nextPath = $location.path(),
                nextRoute = $route.routes[nextPath];
            if (nextRoute && nextRoute.requiredLogin && !auth.isAuth()) {
                $location.path("/login");
                $rootScope.$apply();
            }
        });
    });
