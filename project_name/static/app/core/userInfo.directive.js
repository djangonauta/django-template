(function () {
  'use strict';

  angular.module('{{ project_name }}').directive('userInfo', ['userInfoTemplate', userInfo]);

  function userInfo(userInfoTemplate) {
    return  {
      restrict: 'E',
      templateUrl: userInfoTemplate,
      controller: ['$window', 'confirmModalService', 'logoutURL', controller],
      controllerAs: 'vm',
      replace: true,
      scope: {}
    }
  }

  function controller($window, confirmModalService, logoutURL) {
    var self = this;
    self.logout = logout;

    function logout() {
      confirmModalService.openModal('Logout', 'Deseja sair da aplicação?', 'Sim', 'Cancelar').then(success);
      function success() {
        $window.location = logoutURL;
      }
    }
  }
})();
