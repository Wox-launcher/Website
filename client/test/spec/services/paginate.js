'use strict';

describe('Service: paginate', function () {

  // load the service's module
  beforeEach(module('woxApp'));

  // instantiate service
  var paginate;
  beforeEach(inject(function (_paginate_) {
    paginate = _paginate_;
  }));

  it('should do something', function () {
    expect(!!paginate).toBe(true);
  });

});
