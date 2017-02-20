(function () {
  'use strict';

  angular.module('{{ project_name }}').factory('Core', ['$http', Core]);

  function Core($http) {
    return {
      setUpResource: setUpResource,
      updatePassword: updatePassword
    }

    /**
     * Função utilizada para configurar resources junto com o formato de paginação do django rest framework.
     */
    function setUpResource(Resource, response) {
      var objects = angular.fromJson(response);
      var results = [];
      angular.forEach(objects.results, function (object) {
        results.push(new Resource(object));
      });
      objects.results = results;
      return objects;
    }

    function updatePassword(data) {
      return $http.post('/rest_auth/password/change/', data);
    }
  }
})();
