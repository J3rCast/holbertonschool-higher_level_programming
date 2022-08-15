#!/usr/bin/node
import { argv } from 'node:process';

let i = 0;
let array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (i < 3) {
  console.log(array[i]);
  i++;
}
