'use strict';

/**
 * @ngdoc function
 * @name woxApp.controller:PluginEditCtrl
 * @description
 * # PluginEditCtrl
 * Controller of the woxApp
 */
angular.module('woxApp')
    .controller('PluginEditCtrl', function ($scope, $upload, api, $cookies, notify, $location, $routeParams) {
        $scope.icon = null;
        $scope.preview = null;
        $scope.plugin = null;
        $scope.desc = "";
        $scope.github = "";

        api.get("/plugin/" + $routeParams.id + "/").success(function (data) {
            $scope.desc = data.long_description;
            $scope.github = data.github;
            $scope.icon = {"name": data.icon, "uploaded": true};
            $scope.preview = {"name": data.preview, "uploaded": true};
            $scope.plugin = {"name": data.plugin_file, "uploaded": true};
        });

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

        $scope.updatePlugin = function () {
            if ($scope.icon == null) {
                notify.error("Icon is required");
                return;
            }
            if ($scope.plugin == null) {
                notify.error("Plugin is required");
                return;
            }

            var files = [];
            var fileFormDataNames = [];

            if ($scope.icon != null && !$scope.icon.uploaded) {
                files.push($scope.icon);
                fileFormDataNames.push("icon");
            }

            //maybe delete preview
            if ($scope.preview == null) {
                $scope.preview = {"name": ""};
            }
            if (!$scope.preview.uploaded) {
                files.push($scope.preview);
                fileFormDataNames.push("preview");
            }

            if ($scope.plugin != null && !$scope.plugin.uploaded) {
                files.push($scope.plugin);
                fileFormDataNames.push("plugin_file");
            }

            $upload.upload({
                method: 'PATCH',
                url: api.baseUrl + "/plugin/" + $routeParams.id + "/",
                data: {
                    github: $scope.github,
                    long_description: $scope.desc
                },
                withCredentials: true,
                file: files,
                fileFormDataName: fileFormDataNames
            }).success(function (data, status, headers, config) {
                notify.success("Update succeed");
                $location.path("/plugin/" + data.id + "/");
            });
        };
    })
;
