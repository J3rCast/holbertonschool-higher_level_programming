#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.charToPrint = 'X';
    }
  }

  print () {
    let width = '';
    let i = 0;
    while (i < this.width) {
      width += this.charToPrint;
      i++;
    }
    for (i = 0; i < this.height; i++) {
      console.log(width);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
