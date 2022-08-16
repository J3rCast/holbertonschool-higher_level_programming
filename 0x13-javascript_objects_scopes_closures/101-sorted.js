#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

function newList (val) {
  const list1 = [val];
  return list1;
}

for (const [key, value] of Object.entries(dict)) {
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = newList(key);
  }
  console.log(key, value);
}
console.log(newDict);
