#!/usr/bin/node

function fact (num) {
  if (isNaN(num) || num === 0) return 1;
  else {
    return (num * fact(num - 1));
  }
}

console.log(fact(Number(process.argv[2])));
