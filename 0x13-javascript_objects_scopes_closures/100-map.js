#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map((currElement, index) => {
  return currElement * index;
});
console.log(list);
console.log(map1);
