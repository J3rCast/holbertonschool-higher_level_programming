#!/usr/bin/node
const fs = require('fs');
const argv = require('process');

fs.readFile(argv[2], 'utf-8', (data, err) => {
  if (err) console.log(err);
  else console.log(data);
});
