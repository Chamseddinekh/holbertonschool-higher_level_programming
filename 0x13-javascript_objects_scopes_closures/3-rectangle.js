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
};
