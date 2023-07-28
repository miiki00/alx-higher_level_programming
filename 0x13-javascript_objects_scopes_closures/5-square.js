#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /**
   * Square - A class that defines a square object.
   *
   * This is a documentation for the constructor function.
   * @size: The widht and the height of the square.
   */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
