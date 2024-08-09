'use strict';

var App = function () {
  function passwordEye(element) {
    $(element).click(function () {
      var input = $(this).siblings(':first');
      var icon = $(':first', this);

      if (input.attr('type') === 'text') {
        $(this).attr('title', 'Clique para visualizar a senha');
        input.attr('type', 'password');
        icon.attr('class', 'bi bi-eye');
      } else {
        $(this).attr('title', 'Clique para esconder a senha');
        input.attr('type', 'text');
        icon.attr('class', 'bi bi-eye-slash');
      }
    });
  }

  function spinner(element) {
    $(element).click(function () {
      $(this).attr('disabled', 'disabled');
      var spinner = $('<span>', {'class': 'spinner-border spinner-border-sm'});
      $(':first', this).replaceWith(spinner);
      $(this).closest('form').submit();
    })
  }

  function addForm(totalFormsSelector, formSelector, destinoSelector) {
    var totalForms = parseInt($(totalFormsSelector).val()); // total de forms inicial (zero based)

    var form = $(formSelector).html();
    form = $(form.replace(/__prefix__/g, totalForms)); // constroe um form com índice igual ao total de forms

    $(totalFormsSelector).val(totalForms + 1); // incrementa o total de forms
    $(destinoSelector).append(form); // adiciona o form construído ao elemento de destino
    form.fadeIn('slow');
  }

  return {
    passwordEye: passwordEye,
    spinner: spinner,
    addForm: addForm
  };
}();

$(function () {
  $('[data-toggle="passwordEye"').each(function (index, element) {
    App.passwordEye(element);
  });

  $('[data-toggle="spinner"]').each(function (index, element) {
    App.spinner(element);
  });

  $('[data-toggle="addForm"]').each(function (index, element) {
    $(element).click(function () {
      App.addForm($(this).data('totalForms'), $(this).data('formVazio'), $(this).data('destino'));
    })
  });

  window.setTimeout(function () {
    $('[primeiro_campo]').focus(),
    500
  });
});
