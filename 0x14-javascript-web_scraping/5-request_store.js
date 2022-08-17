#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
const { argv } = require('process');
const link = argv[2];
const path = argv[3];

axios.get(link)
  .then(res => {
    console.log(res.body);
  });
