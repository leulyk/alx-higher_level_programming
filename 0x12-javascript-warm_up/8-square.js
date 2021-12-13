#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let output = '';

if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  if (arg > 0) {
    for (let i = 1; i <= arg; ++i) {
      for (let j = 1; j <= arg; ++j) {
        output += 'X';
      }
      if (i !== arg) {
        output += '\n';
      }
    }
    console.log(output);
  }
}
