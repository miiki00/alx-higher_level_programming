#!/usr/bin/node

function factorial (num) {
  if (num.toString() === NaN.toString() || num === 1) {
    return (1);
  }

  return num * factorial(num - 1);
}

let firstArg = process.argv[2];
firstArg = Number(firstArg);

console.log(factorial(firstArg));
