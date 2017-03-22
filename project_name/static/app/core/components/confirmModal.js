(function () {
  'use strict';

  angular.module('{{ project_name }}').factory('confirmModalService',
                                              ['$uibModal', 'confirmModalTemplate', confirmModalService]);

  /**
   * Modal de confirmação reutilizável. Ex:
   * var result = confirmModalService.openModal(
   *   'Título em modal-header', 'Mensagem em modal-body', 'Label do botão confirm', 'Label do botão cancel'
   * );
   * // success e error são handlers quando o usuário confirma ou, cancela o modal, respectivamente.
   * result.then(success, error);
   */
  function confirmModalService($uibModal, confirmModalTemplate) {
    return {
      openModal: openModal
    }

    /**
     * Retorna uma promessa ao caller.
     */
    function openModal(title, message, okLabel, cancelLabel) {
      return $uibModal.open({
        templateUrl: confirmModalTemplate,
        controller: ['$uibModalInstance', 'title', 'message', 'okLabel', 'cancelLabel', controller],
        controllerAs: 'vm',
        resolve: {
          title: function () { return title; },
          message: function () { return message; },
          okLabel: function () { return okLabel; },
          cancelLabel: function () { return cancelLabel; }
        },
        backdrop: 'static'
      }).result;

      /**
       * Gerencia o modal.
       */
      function controller($uibModalInstance, title, message, okLabel, cancelLabel) {
        var self = this;

        self.title = title;
        self.message = message;
        self.okLabel = okLabel;
        self.cancelLabel = cancelLabel;

        self.ok = ok;
        self.cancel = cancel;

        function ok() {
          $uibModalInstance.close();
        }

        function cancel() {
          $uibModalInstance.dismiss();
        }

      }
    }
  }
})();
