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

            var leitor = new FileReader();
            leitor.onload = function () {
              scope.$apply(function () {
                scope.lerArquivo = leitor.result;
              });
            };
            leitor.readAsDataURL(scope.lerArquivo);
          });
        });
      }
    }
  }
})();
