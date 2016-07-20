(function () {
  'use strict';

  angular.module('{{ project_name }}').controller('loginCtrl', ['$window', controller]);

  function controller($window) {
    var self = this;
    self.next = $window.location.href.split('next=')[1]
  }
})();
