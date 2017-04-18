(function () {
  'use strict';

  angular.module('{{ project_name }}')
    .config(['$interpolateProvider', interpolateConfig])
    .config(['$resourceProvider', resourceConfig])
    .config(['$httpProvider', httpConfig])
    .config(['$compileProvider', compileConfig]);

  function interpolateConfig($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }

  function resourceConfig($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }

  function httpConfig($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }

  function compileConfig($compileProvider) {
    $compileProvider.debugInfoEnabled(false);
    $compileProvider.commentDirectivesEnabled(false);
    $compileProvider.cssClassDirectivesEnabled(false);
  }
})();
