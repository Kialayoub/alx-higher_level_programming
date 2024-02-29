#!/usr/bin/node
// Outputs two arguments passed to the script, formatted as "argument1 is argument2"


if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
