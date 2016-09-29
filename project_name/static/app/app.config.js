(function () {
  'use strict';

  angular.module('{{ project_name }}')
    .config(['$interpolateProvider', interpolateConfig])
    .config(['$resourceProvider', resourceConfig])
    .config(['$httpProvider', httpConfig]);

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
})();
