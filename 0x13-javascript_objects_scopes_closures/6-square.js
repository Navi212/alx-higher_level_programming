#!/usr/bin/node

const Sq = require('./5-square.js');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      c = 'C';
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;
