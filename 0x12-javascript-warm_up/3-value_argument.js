#!/usr/bin/node
// Outputs the first argument passed to the script

if (process.argv[2] === undefined) {
  console.log('No argument provided');
} else {
  console.log(process.argv[2]);
}

