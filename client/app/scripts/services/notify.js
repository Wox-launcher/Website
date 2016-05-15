'use strict';

/**
 * @ngdoc service
 * @name woxApp.notify
 * @description
 * # notify
 * Factory in the woxApp.
 */
angular.module('woxApp')
.factory('notify', function () {

    Messenger.options = {
        extraClasses: 'messenger-fixed messenger-on-top messenger-on-right',
        theme: 'flat'
    };

    return {
        error: function (msg) {
            Messenger().error({
                message: msg,
                showCloseButton: true,
                hideAfter: 5
            }); 
        },
        success: function (msg) {
            Messenger().success({
                message: msg,
                hideAfter: 3
            }); 
        }
    };
});
