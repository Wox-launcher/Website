'use strict';

/**
 * @ngdoc filter
 * @name woxApp.filter:apiurl
 * @function
 * @description
 * # apiurl
 * Filter in the woxApp.
 */
angular.module('woxApp')
  .filter('apiurl', function (api) {
    return function (input) {
      return api.baseUrl + "/media/" +input;
    };
  });
