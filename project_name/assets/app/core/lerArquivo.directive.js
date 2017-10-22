(function () {
  'use strict';

  angular.module('{{ project_name }}').directive('lerArquivo', lerArquivo);

  function lerArquivo() {
    return {
      scope: {
        lerArquivo: '='
      },
      link: function (scope, element, attrs) {
        element.bind('change', function (changeEvent) {
          scope.$apply(function () {
            scope.lerArquivo = changeEvent.target.files[0];
          });
        });
      }
    }
  }
})();
