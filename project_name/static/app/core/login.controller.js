(function () {
  'use strict';

  angular.module('{{ project_name }}').controller('loginCtrl', ['$window', controller]);

  function controller($window) {
    var self = this;
    if (!localStorage.login_redirect_url) {
      localStorage.login_redirect_url = $window.location.href.split('next=')[1]
    }
    self.next = localStorage.login_redirect_url;
  }
})();
