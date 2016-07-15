(function () {
  'use strict';

  var app = angular.module('{{ project_name }}');
  app.config(['$stateProvider', '$urlRouterProvider', routeConfig]);
  app.run(function($rootScope, $state) {
    $rootScope.$state = $state;
  });

  function routeConfig($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider.state('index', {
      url: '/',
      template: '<h4>Working!</h4>'
    }).state('config', {
      url: '/config',
      template: '<h4>Config</h4>'
    });

    $stateProvider.state('parent', {
      url: '/parent',
      abstract: true,
      template: '<div ui-view></div>'
    }).state('parent.child1', {
      url: '/child1',
      template: '<div>Child1</div>'
    }).state('parent.child2', {
      url: '/child2',
      template: '<div>Child2</div>'
    });
  }
})();
