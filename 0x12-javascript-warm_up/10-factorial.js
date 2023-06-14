#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num < 0 || num === 0 || Number.isNaN(num)) {
    return 1;
  } else {
    return (factorial(num - 1) * num);
  }
}
console.log(factorial(num));
