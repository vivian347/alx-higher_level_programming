#!/usr/bin/node

const x = Number(process.argv[2]);
if (isNaN(x) === true || process.argv.length === 2) console.log('Missing number of occurences');
else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
