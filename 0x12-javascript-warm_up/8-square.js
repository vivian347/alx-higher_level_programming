#!/usr/bin/node

const size = Math.floor(process.argv[2]);

if (isNaN(size)) console.log('Missing size');
for (let r = 0; r < size; r++) {
  let row = '';
  for (let c = 0; c < size; c++) row += 'x';
  console.log(row);
}
