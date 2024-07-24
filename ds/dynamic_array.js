class DynamicArray {
  constructor() {
    this.size = 2;
    this.length = 0;
    this.arr = new Array(2);
  }

  push(n) {
    if (this.size <= this.length) this.resize();
    this.arr[this.length] = n;
    this.length++;
  }

  resize() {
    this.size = 2 * this.size;
    let newArray = new Array(this.size);

    for (let i = 0; i < this.arr.length; i++) {
      newArray[i] = this.arr[i];
    }

    this.arr = newArray;
  }

  pop() {
    if (this.length <= 0) throw new Error('out of index');
    let index = this.length - 1;
    let val = this.arr[index];
    this.arr[index] = null;
    this.length -= 1;
    return val;
  }

  print() {
    if (this.length <= 0) throw new Error('out of index');
    for (let i = 0; i < this.arr.length; i++) {
      if (this.arr[i]) console.log(this.arr[i]);
    }
  }
}

function test_dynamic_array(){
    const assert = require('assert');
    
    let dynamicArray = new DynamicArray();
    dynamicArray.push(1);
    dynamicArray.push(2);
    dynamicArray.push(3);
    dynamicArray.push(4);
    dynamicArray.push(5);

    assert(dynamicArray.length === 5);
    assert(dynamicArray.size === 8);

    let val = dynamicArray.pop();

    assert(val === 5);
    assert(dynamicArray.length === 4);

    console.log('All test cases pass');
}

test_dynamic_array();