#!/usr/bin/node
const args = process.argv;
let square = '';
let width = 0;
if (isNaN(args[2])) console.log('Missing size');
else {
  for (let height = 0; height < args[2]; height++) {
    while (width < args[2]){
      square += 'x';
      width++;
    }
    console.log(square);
  }
}
