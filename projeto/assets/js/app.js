App = function () {
  function configurarPasswordEye(seletor) {
    var eyeButton = document.querySelector(seletor);
    var icon = eyeButton.firstElementChild;

    eyeButton.addEventListener('click', function () {
      var input = eyeButton.parentElement.firstElementChild;

      if (input.getAttribute('type') === 'text') {
        eyeButton.setAttribute('title', 'Clique para visualizar a senha');
        input.setAttribute('type', 'password');
        icon.setAttribute('class', 'bi bi-eye');
      } else {
        eyeButton.setAttribute('title', 'Clique para esconder a senha');
        input.setAttribute('type', 'text');
        icon.setAttribute('class', 'bi bi-eye-slash');
      }
    });
  }

  function configurarSpinner(seletor) {
    document.querySelector(seletor).addEventListener('click', function () {
      this.setAttribute('disabled', 'disabled');
      var spinner = document.createElement('span');
      spinner.classList.add('spinner-border', 'spinner-border-sm');
      this.replaceChild(spinner, this.firstElementChild);
      this.parentElement.submit();
    })
  }

  return {
    configurarPasswordEye: configurarPasswordEye,
    configurarSpinner: configurarSpinner
  };
}();
