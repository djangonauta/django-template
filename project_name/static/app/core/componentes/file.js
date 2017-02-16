(function () {
  'use strict';

  angular.module('{{ project_name }}').directive('fileread', fileread);

  function fileread() {
    return {
      scope: {
        fileread: '='
      },
      link: function (scope, element, attributes) {
        element.bind('change', function (changeEvent) {
          scope.$apply(function () {
            scope.fileread = changeEvent.target.files[0];
          });
        });
      }
    }
  }
})();
