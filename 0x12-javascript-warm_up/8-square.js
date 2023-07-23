#!/usr/bin/node

function strMul (str, num) {
  let strProd = '';
  for (let i = 0; i < num; i++) {
    strProd += str;
  }
  return (strProd);
}

const firstArg = process.argv[2];
const numFirstArg = Number(firstArg);

if (numFirstArg) {
  const width = strMul('X', numFirstArg);
  for (let i = 0; i < numFirstArg; i++) {
    console.log(width);
  }
} else {
  console.log('Missing size');
}
