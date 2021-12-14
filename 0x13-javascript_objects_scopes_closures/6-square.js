#!/usr/bin/node

const MainSquare = require('./5-square');

class Square extends MainSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 1; i <= this.width; ++i) {
        for (let j = 1; j <= this.width; ++j) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
}

module.exports = Square;
