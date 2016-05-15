'use strict';

describe('Controller: ReleaseVersionCtrl', function () {

  // load the controller's module
  beforeEach(module('woxApp'));

  var ReleaseVersionCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReleaseVersionCtrl = $controller('ReleaseVersionCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
