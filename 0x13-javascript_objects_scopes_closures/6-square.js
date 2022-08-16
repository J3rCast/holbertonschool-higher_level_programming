#!/usr/bin/node
const Rectangle = require('./4-rectangle');

exports.Square = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      this.charToPrint = c;
    }
    this.print();
    this.charToPrint = 'X';
  }
};
