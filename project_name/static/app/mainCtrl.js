(function () {
  'use strict';

  angular.module('{{ project_name }}')
    .controller('mainCtrl', mainCtrl);

  function mainCtrl($window, confirmModalService, logoutURL) {
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