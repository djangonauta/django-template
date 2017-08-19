(function () {
  'use strict';

  var app = angular.module('{{ project_name }}');

  app.config([
    '$stateProvider',
    '$urlRouterProvider',
    stateConfig
  ]);

  app.run(['$rootScope', '$state', run]);

  function run($rootScope, $state) {
    $rootScope.$state = $state;
  }

  function stateConfig($stateProvider,
                       $urlRouterProvider) {
  
    $urlRouterProvider.otherwise('/');

    $stateProvider.state('home', {
      url: '/',
      template: '<h4>Working</h4>'
    });
  }
})();
