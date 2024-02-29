#!/usr/bin/node
// x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
