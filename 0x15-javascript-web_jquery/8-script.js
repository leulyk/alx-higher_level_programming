
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, (data, status) => {
  data.results.forEach((result) => {
    $('ul#list_movies').append('<li>' + result.title + '</li>');
  });
});
