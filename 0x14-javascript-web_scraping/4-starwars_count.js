#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    let count = 0;
    const info = JSON.parse(body);
    info.results.forEach(function (movie) {
      movie.characters.forEach(function (character) {
        if (character.search('/18/') !== -1) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
