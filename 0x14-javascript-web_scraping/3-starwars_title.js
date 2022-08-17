#!/usr/bin/node
const request = require('request');
const { argv } = require('process')
const link = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(link, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
