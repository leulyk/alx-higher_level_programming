
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(() => {
  $.get(url, (data, status) => {
    $('div#hello').text(data.hello);
  });
});
