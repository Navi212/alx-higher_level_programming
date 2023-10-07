$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (res, status) {
    if (status === 'success') {
      const val = res.hello;
      $('DIV#hello').text(val);
    }
  });
});
