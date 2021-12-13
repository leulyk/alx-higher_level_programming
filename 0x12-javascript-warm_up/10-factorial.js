#!/usr/bin/node

function factorial (num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
