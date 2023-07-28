#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  /**
   * function that prints the passed argument and the index.
   * @item: the item to be printed.
   */

  console.log(`${count++}: ${item}`);
};
