'use strict';

describe('Controller: ThemeBuilderCtrl', function () {

  // load the controller's module
  beforeEach(module('woxApp'));

  var ThemeBuilderCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ThemeBuilderCtrl = $controller('ThemeBuilderCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
