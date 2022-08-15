#!/usr/bin/node
import { argv } from 'node:process'

const string = argv[2] + ' is ' + argv[3]
console.log(string)
