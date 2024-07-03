#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  },
  print: function () {
    console.log(`{ type: 'object', value: ${this.value}, incr: [Function: incr] }`);
  }
};

myObject.print();
myObject.incr();
myObject.print();
myObject.incr();
myObject.print();
myObject.incr();
myObject.print();
