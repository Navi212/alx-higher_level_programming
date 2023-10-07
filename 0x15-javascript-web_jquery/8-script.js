$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (res, status) {
    if (status === 'success') {
      const titles = res.results;
      for (const items in titles) {
        $('UL#list_movies').append('<li>' + titles[items].title + '</li>');
      }
    }
  });
});
