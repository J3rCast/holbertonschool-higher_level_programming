#!/usr/bin/node
const args = process.argv;
let i = 2, res = 0;
let list = [];
let len = args.length;

for (i = 2; i < len; i++) {
  list.push(parseInt(args[i]));
}

i = 2;
max = Math.max(...list);

if (!args[2] || !args[3]) console.log(0);
else {
  while (i < len) {
    if (args[i] < max && args[i] > args[i - 1]) res = args[i];
    i++;
  }
  console.log(parseInt(res));
}
