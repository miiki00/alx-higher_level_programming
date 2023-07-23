#!/usr/bin/node
let haveArgs = false;

process.argv.forEach((value, idx) => {
  if (idx === 2) {
    console.log(value);
    haveArgs = true;
  }
});
if (!(haveArgs)) {
  console.log('No arguments');
}
