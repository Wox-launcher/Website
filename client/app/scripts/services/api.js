'use strict';

/**
 * @ngdoc service
 * @name woxApp.api
 * @description
 * # api
 * Factory in the woxApp.
 */
angular.module('woxApp')
    .factory('api', function ($http, apiurl) {
        return {
            post: function (url, data) {
                return $http.post(apiurl + url, data);
            },
            get: function (url) {
                return $http.get(apiurl + url);
            },
            patch: function (url,data) {
                return $http.patch(apiurl + url,data);
            },
            delete: function (url) {
                return $http.delete(apiurl + url);
            },
            baseUrl: apiurl
        };
    });
