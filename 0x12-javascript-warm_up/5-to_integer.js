#!/usr/bin/node

if (process.argv.length === 2 || isNaN(Number(process.argv[2])) === true) console.log('Not a number');
else console.log('My number: ' + Number(process.argv[2]));
