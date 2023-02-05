$(function () {
  $('#password-eye').click(function () {
    const campoSenha = $(this).siblings('[id*=password],[id*=senha]')
    var tipo = campoSenha.attr('type') === 'text' ? 'password' : 'text';
    var titulo = `Clique para ${tipo === 'text' ? 'esconder' : 'mostrar'} a senha`;

    campoSenha.attr('type', tipo);
    $(this).attr('title', titulo);
  })
})
