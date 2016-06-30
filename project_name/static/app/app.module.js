(function () {
  'use strict';
  
  angular.module('{{ project_name }}', [
    'pascalprecht.translate',
    'ui.router',
    'ui.bootstrap',
    'ui.utils.masks',
    'ui.grid',
    'ui.grid.pagination',
    'ui.grid.resizeColumns',
    'ngResource',
    'cgBusy',
    'toastr'
  ]);
})();
