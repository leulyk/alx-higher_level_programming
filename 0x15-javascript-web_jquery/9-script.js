
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.when(
  $.get(url, (data, status) => {
    $('div#hello').text(data.hello);
  })
);
