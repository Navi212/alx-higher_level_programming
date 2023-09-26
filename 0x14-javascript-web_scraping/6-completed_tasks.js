#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dit = {};
    const jFile = JSON.parse(body);
    for (let i = 0; i < jFile.length; i++) {
      if (jFile[i].completed) {
        if (dit[jFile[i].userId] === undefined) {
          dit[jFile[i].userId] = 0;
        }
        dit[jFile[i].userId]++;
      }
    }
    console.log(dit);
  }
});
