#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(findSecondBiggest(process.argv));
}

function findSecondBiggest (arr) {
  let first, second;

  if (parseInt(arr[2]) >= parseInt(arr[3])) {
    first = parseInt(arr[2]);
    second = parseInt(arr[3]);
  } else {
    first = parseInt(arr[3]);
    second = parseInt(arr[2]);
  }

  for (let i = 4; i < arr.length; ++i) {
    const current = parseInt(arr[i]);
    if (current > first) {
      second = first;
      first = current;
    } else if (current > second) {
      second = current;
    }
  }
  return second;
}
