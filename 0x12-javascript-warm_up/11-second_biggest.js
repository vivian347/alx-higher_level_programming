#!/usr/bin/node

const arr = process.argv.slice(2);
if (!arr[0] || !arr[2]) console.log(0);
else {
  const args = arr.map(Number);
  const first = Math.max.apply(null, args);
  args.splice(args.indexOf(first), 1);
  console.log(Math.max.apply(null, args));
}
