(function () {
  'use strict';

  angular.module('{{ project_name }}')
    .directive('submit', submit);

  /**
   * Submete um formulário desativando o botão de submissão quando clicado.
   */
  function submit() {
    return {
      restrict: 'A',
      link: function (scope, element, attrs) {
        element.click(function (event) {
          element.attr('disabled', 'disabled');
          element.closest('form').submit();
        });
      }
    }
  }
})();
