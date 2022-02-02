#!/usr/bin/node

/*
  A script that computes the number of tasks completed by user id
  from the URL https://jsonplaceholder.typicode.com/todos
*/

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const info = JSON.parse(body);
    const completedCount = [];
    info.forEach(function (entry) {
      if (completedCount[entry.userId] === undefined) {
        completedCount[entry.userId] = 0;
      }
      if (entry.completed === true) {
        completedCount[entry.userId]++;
      }
    });
    const result = {};
    for (let i = 1; i < completedCount.length; ++i) {
      if (completedCount[i] > 0) {
        result[i] = completedCount[i];
      }
    }
    console.log(result);
  }
});
