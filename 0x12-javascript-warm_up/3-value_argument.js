#!/usr/bin/node

const pross = require('pross');
const arg = pross.argv[2];

if (arg) {
  console.log(arg);
}
else {
  console.log('No argument');
}
