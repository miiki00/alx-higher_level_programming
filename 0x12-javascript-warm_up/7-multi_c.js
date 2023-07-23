#!/usr/bin/node

const firstArg = process.argv[2];
const numFirstArg = Number(firstArg);

if (typeof (firstArg) === typeof (undefined)) {
  console.log('Missing number of occurrences');
} else if (numFirstArg) {
  for (let i = 0; i < numFirstArg; i++) {
    console.log('C is fun');
  }
}
