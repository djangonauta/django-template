(function () {
  'use strict';

  angular.module('{{ project_name }}').controller('loginCtrl', ['$window', controller]);

  function controller($window) {
    var self = this;
    self.focus = 0;
    self.focus++;

    var login_redirect_url = $window.location.href.split('next=')[1];
    $window.localStorage.login_redirect_url = login_redirect_url || $window.localStorage.login_redirect_url;

    self.next = $window.localStorage.login_redirect_url;
  }
})();
