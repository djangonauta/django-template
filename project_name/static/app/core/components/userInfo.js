(function () {
  'use strict';

  angular.module('{{ project_name }}').directive('userInfo', ['userInfoTemplate', userInfo]);

  function userInfo(userInfoTemplate) {
    return  {
      restrict: 'E',
      templateUrl: userInfoTemplate,
      controller: ['$window', 'confirmModalService', controller],
      controllerAs: 'vm',
      replace: true
    }
  }

  function controller($window, confirmModalService) {
    var self = this;
    self.logout = logout;

    function logout() {
      confirmModalService.openModal('Logout', 'Deseja sair da aplicação?', 'Sim', 'Cancelar').then(close, dismiss);

      function close() {
        $window.location = '/contas/logout/';
      }

      function dismiss() {}
    }
  }
})();
