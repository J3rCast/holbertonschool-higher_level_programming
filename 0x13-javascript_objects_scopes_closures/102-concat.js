#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', function (err, data1) {
  if (err) {
    throw err;
  }
  fs.readFile(args[3], 'utf8', function (err, data2) {
    if (err) {
      throw err;
    }
    fs.appendFile(args[4], data1 + data2, (err) => {
      if (err) {
        throw err;
      }
    });
  });
});
