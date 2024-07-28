function quickSort(arr, s, e) {
  if (e - s + 1 <= 1) return arr;

  let pivot = arr[e];
  let left = s;

  for (let i = s; i < e; i++) {
    if (arr[i] < pivot) {
      let tmp = arr[i];
      arr[i] = arr[left];
      arr[left] = tmp;
      left++;
    }
  }

  arr[e] = arr[left];
  arr[left] = pivot;

  quickSort(arr, s, left - 1);
  quickSort(arr, left + 1, e);

  return arr;
}

function test_quick_sort() {
  const assert = require('assert');
  const list = [1, 4, 2, 3, 5];
  let arr = quickSort(list, 0, list.length - 1);

  assert(arr[0] === 1);
  assert(arr[1] === 2);
  assert(arr[2] === 3);
  assert(arr[3] === 4);
  assert(arr[4] === 5);

  console.log('All test cases pass');
}

test_quick_sort();
