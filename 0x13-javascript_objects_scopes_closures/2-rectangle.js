#!/usr/bin/node

class Rectangle {
  /**
   * Rectangle: A class that defines a rectangle object.
   *
   * This is a documentation for the constructor function.
   * @w: The width of the rectangle object.
   * @h: The height of height rectangle object.
   *
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
