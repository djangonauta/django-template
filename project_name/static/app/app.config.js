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

    $httpProvider.interceptors.push(function($q, $window, loginURL) {
      return {
        responseError: function(rejection) {
          if (rejection.status === 401 || rejection.status === 403) {
            $window.location = loginURL + '?next=' + $window.location.pathname;
          }
          return $q.reject(rejection);
        }
      };
    });
  }
})();
