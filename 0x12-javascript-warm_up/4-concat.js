#!/usr/bin/node
import { argv } from 'node:process';

let string = argv[2] + ' is ' + argv[3];
console.log(string);
