'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:CreatepluginCtrl
 * @description
 * # CreatepluginCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('CreatepluginCtrl', function ($scope, $upload, api, $cookies, notify, $location) {

        $scope.icon = null;
        $scope.preview = null;
        $scope.plugin = null;
        $scope.desc = "";
        $scope.github = "";

        $scope.addIconFile = function ($files) {
            $scope.icon = $files[0];
        };

        $scope.removeIcon = function () {
            $scope.icon = null;
        };

        $scope.addPreviewFile = function ($files) {
            $scope.preview = $files[0];
        };

        $scope.removePreview = function () {
            $scope.preview = null;
        };

        $scope.addPluginFile = function ($files) {
            $scope.plugin = $files[0];
        };

        $scope.removePlugin = function () {
            $scope.plugin = null;
        };

        $scope.submitPlugin = function () {
            if ($scope.icon == null) {
                notify.error("Icon is required");
                return;
            }
            if ($scope.plugin == null) {
                notify.error("Plugin is required");
                return;
            }

            var files = [$scope.icon, $scope.plugin];
            var fileFormDataNames = ["icon", "plugin_file"];
            if ($scope.preview != null) {
                files.push($scope.preview);
                fileFormDataNames.push("preview");
            }

            $upload.upload({
                url: api.baseUrl + "/plugin/",
                headers: {"X-CSRFToken": $cookies.csrftoken},
                data: {
                    github: $scope.github,
                    long_description: $scope.desc
                },
                withCredentials: true,
                file: files,
                fileFormDataName: fileFormDataNames
            }).success(function (data, status, headers, config) {
                notify.success("Uploading succeed");
                $location.path("/plugin/" + data.id + "/");
            });
        };
    });
