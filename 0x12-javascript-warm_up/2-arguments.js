#!/usr/bin/node
// Displays a message based on the number of arguments provided

if (process.argv.length === 2) {
  console.log('No arguments');
} else if (process.argv.length === 3) {
  console.log('Single argument found');
} else {
  console.log('Multiple arguments found');
}

