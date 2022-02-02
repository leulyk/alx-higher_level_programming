#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/people/18';

request(url, (error, response, body) => {
  if (!error) {
    const info = JSON.parse(body);
    console.log(info.films.length);
  }
});
