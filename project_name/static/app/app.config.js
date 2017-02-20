(function () {
  'use strict';

  angular.module('{{ project_name }}')
    .config(['$interpolateProvider', interpolateConfig])
    .config(['$resourceProvider', resourceConfig]);

  function interpolateConfig($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }

  function resourceConfig($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }
})();
