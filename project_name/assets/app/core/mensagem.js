/**
 * Delete este arquivo.
 * 
 */
(function (global, factory) {
  global.Mensagem = factory();
})(this, function () { 'use strict';
  return {
    install: install
  }

  function install(Vue, options) {
    Vue.prototype.Mensagem = {
      obterMensagem: obterMensagem
    };

    function obterMensagem() {
      return 'Olá VueJs + Django';
    }
  }
});
