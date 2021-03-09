#!/usr/bin/node
// class Rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method called print() that prints the rectangle
  print () {
    let i = 0;
    for (i; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  // method called double() that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
