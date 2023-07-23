#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2 || argv.length === 3) {
  console.log('0');
} else {
  let firstBig = Number(argv[2]);
  let secondBig = Number(argv[3]);

  if (firstBig < secondBig) {
    const temp = firstBig;
    firstBig = secondBig;
    secondBig = temp;
  }

  for (let i = 4; i < argv.length; i++) {
    const value = Number(argv[i]);
    if (firstBig < value) {
      secondBig = firstBig;
      firstBig = value;
    } else if (secondBig < value) {
      secondBig = value;
    }
  }

  console.log(secondBig);
}
