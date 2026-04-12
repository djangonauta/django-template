'use strict';

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
  }

  function initPasswordEye(root = document) {
    root.querySelectorAll('[data-password-eye]').forEach(el => {
      if (el.dataset.passwordEyeInit) return;
      el.dataset.passwordEyeInit = true;
      passwordEye(el);
    });
  }

  function spinner(element) {
    element.addEventListener('click', function () {
      this.disabled = true;
      const spinner = element.querySelector('i');
      spinner.className = 'fa-solid fa-spinner fa-spin';
      this.closest('form').submit();
    });
  }

  function initSpinner(root = document) {
    root.querySelectorAll('[data-spinner]').forEach(el => {
      spinner(el);
    });
  }

  function addForm(totalFormsSelector, formSelector, destinoSelector) {
    const totalForms = parseInt(document.querySelector(totalFormsSelector).value);
    const form = document.querySelector(formSelector).innerHTML.replace(/__prefix__/g, totalForms);
    document.querySelector(totalFormsSelector).value = totalForms + 1;
    const newForm = document.createElement('div');
    newForm.innerHTML = form;
    document.querySelector(destinoSelector).appendChild(newForm);
    newForm.style.opacity = 0;
    setTimeout(() => newForm.style.opacity = 1, 10);
  }

  function initAddForm(root = document) {
    root.querySelectorAll('[data-add-form]').forEach(function (element) {
      element.addEventListener('click', function () {
        addForm(
          this.dataset.totalForms,
          this.dataset.formVazio,
          this.dataset.destino
        );
      });
    });
  }

  /**
   <select data-tom
      data-tom-url="/api/v1/usuarios/?search="
      data-tom-remove
      name="cliente_id">
    </select>
   */
  function initTomSelect(root = document) {
    root.querySelectorAll('[data-tom]').forEach(el => {
      if (el.tomselect) return;

      const config = {};
      const plugins = {};

      if (el.dataset.tomRemove !== undefined) {
        plugins.remove_button = { title: el.dataset.tomRemove || 'Remover' };
      }

      if (Object.keys(plugins).length) {
        config.plugins = plugins;
      }

      if (el.dataset.tomUrl) {
        config.valueField = el.dataset.tomValue || 'id';
        config.labelField = el.dataset.tomLabel || 'texto';
        config.searchField = el.dataset.tomSearch || 'texto';

        config.onItemAdd = function () {
          this.setTextboxValue('');
          this.refreshOptions(false);
        };

        config.load = function (query, callback) {
          let url = el.dataset.tomUrl;
          if (query) {
            url += encodeURIComponent(query);
          }
          fetch(url)
            .then(r => r.json())
            .then(json => callback(json.results || json))
            .catch(() => callback());
        };
      }
      new TomSelect(el, config);
    });
  }

  function initAll(root = document) {
    initPasswordEye(root);
    initSpinner(root);
    initAddForm(root);
    initTomSelect(root);
  }

  window.AppUtils = {
    initAll,
  }
})();

document.addEventListener('DOMContentLoaded', function () {
  window.AppUtils.initAll();

  setTimeout(function () {
    const el = document.querySelector('[data-primeiro-campo]');
    if (el) {
      el.tomselect ? el.tomselect.focus() : el.focus();
    }
  }, 300);
});

document.body.addEventListener('htmx:afterSwap', e => {
  window.AppUtils.initAll(e.detail.target);
});
