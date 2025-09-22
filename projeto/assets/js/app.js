'use strict';

// Definir o namespace global
window.AppUtils = {};

(function() {
  function passwordEye(element) {
    element.addEventListener('click', function () {
      const input = this.previousElementSibling;
      const icon = this.querySelector('i');

      if (input.type === 'text') {
        this.title = 'Clique para visualizar a senha';
        input.type = 'password';
        icon.className = 'fa-solid fa-eye';
      } else {
        this.title = 'Clique para esconder a senha';
        input.type = 'text';
        icon.className = 'fa-solid fa-eye-slash';
      }
    });
  };

  function spinner(element) {
    element.addEventListener('click', function () {
      this.disabled = true;
      const spinner = element.querySelector('i');
      spinner.className = 'fa-solid fa-spinner fa-spin';
      const spinnerOverlay = document.getElementById('spinner-overlay');
      if (spinnerOverlay) {
        spinnerOverlay.style.visibility = 'visible';
        spinnerOverlay.style.opacity = '1';
      }
      this.closest('form').submit();
    });
  };

  function addForm(totalFormsSelector, formSelector, destinoSelector) {
    const totalForms = parseInt(document.querySelector(totalFormsSelector).value);
    const form = document.querySelector(formSelector).innerHTML.replace(/__prefix__/g, totalForms);
    document.querySelector(totalFormsSelector).value = totalForms + 1;
    const newForm = document.createElement('div');
    newForm.innerHTML = form;
    document.querySelector(destinoSelector).appendChild(newForm);
    newForm.style.opacity = 0;
    setTimeout(() => newForm.style.opacity = 1, 10);
  };

  /**
   * Utilitário para gerenciar a exibição do spinner em requisições AJAX
   */
  const SpinnerManager = {
    /**
     * Exibe o spinner de carregamento
     */
    show: function() {
      const spinner = document.getElementById('spinner-overlay');
      if (spinner) {
        spinner.style.visibility = 'visible';
        spinner.style.opacity = '1';
      }
    },

    /**
     * Esconde o spinner de carregamento
     */
    hide: function() {
      const spinner = document.getElementById('spinner-overlay');
      if (spinner) {
        spinner.style.opacity = '0';
        // Aguardamos a transição para definir a visibilidade como hidden
        setTimeout(() => {
          spinner.style.visibility = 'hidden';
        }, 300); // Tempo em ms que corresponde à transição CSS
      }
    },

    /**
     * Wrapper para fetch que gerencia automaticamente o spinner
     * @param {string|Request} url - A URL ou objeto Request para o fetch
     * @param {Object} options - Opções para o fetch (opcional)
     * @returns {Promise} - Promise do fetch
     */
    fetchWithSpinner: function(url, options = {}) {
      this.show();

      return fetch(url, options)
        .then(response => {
          // Captura a resposta antes de esconder o spinner
          return response;
        })
        .catch(error => {
          console.log('Erro ao tentar executar chamada remota', error)
          // Re-throw do erro para ser tratado pelo caller
          throw error;
        })
        .finally(() => {
          // Sempre esconde o spinner, independente de sucesso ou erro
          this.hide();
        });
    }
  };

  // Expor as funções ao namespace global AppUtils
  window.AppUtils.passwordEye = passwordEye;
  window.AppUtils.spinner = spinner;
  window.AppUtils.addForm = addForm;
  window.AppUtils.SpinnerManager = SpinnerManager;
})();

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[data-password-eye]').forEach(function (element) {
    window.AppUtils.passwordEye(element);
  });

  document.querySelectorAll('[data-spinner]').forEach(function (element) {
    window.AppUtils.spinner(element);
  });

  document.querySelectorAll('[data-add-form]').forEach(function (element) {
    element.addEventListener('click', function () {
      window.AppUtils.addForm(
        this.dataset.totalForms,
        this.dataset.formVazio,
        this.dataset.destino
      );
    });
  });

  setTimeout(function () {
    const el = document.querySelector('[primeiro-campo]')
    if (el) {
      el.focus();
    }
  }, 300);
});
