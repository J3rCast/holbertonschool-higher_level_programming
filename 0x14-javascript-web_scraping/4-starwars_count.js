#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(link)
  .then(res => {
    let movieCount = 0;
    for (let i = 0; i < res.data.count; i++) {
      if (Object.values(res.data.results[i].characters).includes(character)) {
        movieCount++;
      }
    }
    console.log(movieCount);
  }).catch(error => {
  });
