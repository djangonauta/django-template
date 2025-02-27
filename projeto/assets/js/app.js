'use strict';

const App = (function () {
  const passwordEye = function (element) {
    element.addEventListener('click', function () {
      const input = this.previousElementSibling;
      const icon = this.querySelector('i');

      if (input.type === 'text') {
        this.title = 'Clique para visualizar a senha';
        input.type = 'password';
        icon.className = 'bi bi-eye';
      } else {
        this.title = 'Clique para esconder a senha';
        input.type = 'text';
        icon.className = 'bi bi-eye-slash';
      }
    });
  };

  const spinner = function (element) {
    element.addEventListener('click', function () {
      this.disabled = true;
      const spinner = document.createElement('span');
      spinner.className = 'spinner-border spinner-border-sm';
      this.replaceChild(spinner, this.firstElementChild);
      this.closest('form').submit();
    });
  };

  const addForm = function (totalFormsSelector, formSelector, destinoSelector) {
    const totalForms = parseInt(document.querySelector(totalFormsSelector).value);
    const form = document.querySelector(formSelector).innerHTML.replace(/__prefix__/g, totalForms);
    document.querySelector(totalFormsSelector).value = totalForms + 1;
    const newForm = document.createElement('div');
    newForm.innerHTML = form;
    document.querySelector(destinoSelector).appendChild(newForm);
    newForm.style.opacity = 0;
    setTimeout(() => newForm.style.opacity = 1, 10);
  };

  return {
    passwordEye,
    spinner,
    addForm
  };
})();

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[data-password-eye]').forEach(function (element) {
    App.passwordEye(element);
  });

  document.querySelectorAll('[data-spinner]').forEach(function (element) {
    App.spinner(element);
  });

  document.querySelectorAll('[data-add-form]').forEach(function (element) {
    element.addEventListener('click', function () {
      App.addForm(
        this.dataset.totalForms,
        this.dataset.formVazio,
        this.dataset.destino
      );
    });
  });

  setTimeout(function () {
    document.querySelector('[primeiro_campo]').focus();
  }, 500);
});
