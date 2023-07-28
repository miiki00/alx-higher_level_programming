#!/usr/bin/node

class Rectangle {
  /**
   * Rectangle - A class that defines a rectangle object.
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

  /**
   * print - an instance method that prints a Rectangle instance.
   */
  print () {
    const printItem = 'X';
    let width = '';

    for (let i = 0; i < this.width; i++) {
      width += printItem;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }

  /**
   * rotate - rotates the rectangle object(exchanges the width and the height).
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * double - doubles the size of the rectangle object (multiplies both the
   * the width and the height by 2).
   */
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
