'use strict';

describe('Controller: DonateCtrl', function () {

  // load the controller's module
  beforeEach(module('woxApp'));

  var DonateCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    DonateCtrl = $controller('DonateCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
