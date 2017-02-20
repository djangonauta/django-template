(function () {
  'use strict';

  angular.module('{{ project_name }}').directive('updatePassword', ['updatePasswordTemplate', updatePassword]);

  function updatePassword(updatePasswordTemplate) {
    return {
      restrict: 'E',
      templateUrl: updatePasswordTemplate,
      controllerAs: 'vm',
      controller: ['Core', 'toastr', controller]
    }

    function controller(Core, toastr) {
      var self = this;
      self.$onInit = onInit;
      self.updatePassword = updatePassword;

      function onInit() {
        self.data = {};
      }

      function updatePassword() {
        self.errors = {};
        self.updatePasswordPromise = Core.updatePassword(self.data);
        self.updatePasswordPromise.then(success).catch(error);

        function success() {
          self.data = {};
          toastr.success('Senha alterada com sucesso.');
        }

        function error(response) {
          self.errors = response.data;
        }
      }
    }
  }
})();
