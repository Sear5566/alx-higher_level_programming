#!/usr/bin/node

const process = require('process');
const arg = process.argv[2];

if (arg) {
  console.log(arg);
}
else {
  console.log('No argument');
}
