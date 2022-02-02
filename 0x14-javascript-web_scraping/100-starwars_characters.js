#!/usr/bin/node

// Print all characters from a Star Wars movie fetched from an API
// Movie ID required as a command line argument

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const movieInfo = JSON.parse(body);
    movieInfo.characters.forEach(function (character) {
      request(character, (error, response, body) => {
        if (!error) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        }
      });
    });
  }
});
