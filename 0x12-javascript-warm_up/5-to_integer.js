#!/usr/bin/node

let firstArg = process.argv[2];
firstArg = Number(firstArg);
if (firstArg.toString() === NaN.toString()) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArg}`);
}
