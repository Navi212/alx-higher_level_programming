$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get('url', function (res, status) {
    if (status == 'success') { $('#character').text(res.name); }
  });
});
