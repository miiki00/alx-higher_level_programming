#!/usr/bin/node

const prevSquare = require('./5-square');

class Square extends prevSquare {
  /**
   * Square - A class that defines a square object.
   *
   * This is a documentation for the constructor function.
   * @size: The widht and the height of the square.
   */

  /**
   * charPrint - an instance method that prints a Square instance.
   * @c: The character to print the square with. default is 'X'
   */
  charPrint (c = 'X') {
    let width = '';

    for (let i = 0; i < this.width; i++) {
      width += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }
}

module.exports = Square;
