$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(url, function (res, status) {
    if (status === 'success') {
      $('INPUT#btn_translate').click(function () {
        const val = $('INPUT#language_code').val();
        $.get('https://hellosalut.stefanbohacek.dev/?lang=' + val, function (res, status) {
          if (status === 'success') {
            $('DIV#hello').text(res.hello);
          }
        });
      });
    }
  });
});
