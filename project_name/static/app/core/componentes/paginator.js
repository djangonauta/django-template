(function () {
  'use strict';

  angular.module('{{ project_name }}').component('paginator', {
    templateUrl: ['paginatorTemplate', function (paginatorTemplate) { return paginatorTemplate;}],
    controllerAs: 'vm',
    bindings: {
      data: '=',
      loader: '=',
      pageSize: '=',
      search: '='
    }
  });
})();
