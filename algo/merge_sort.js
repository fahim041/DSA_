function mergeSort(arr){
    let length = arr.length;
    if(length <= 1){
        return arr;
    }

    let mid = Math.floor(length / 2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid, length));

    return merge(left, right);
};

function merge(left, right){
    let sortedArr = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while(leftIndex < left.length && rightIndex < right.length){
        if(left[leftIndex] < right[rightIndex]){
            sortedArr.push(left[leftIndex]);
            leftIndex++;
        } else {
            sortedArr.push(right[rightIndex]);
            rightIndex++;
        }
    }

    while(leftIndex < left.length){
        sortedArr.push(left[leftIndex]);
        leftIndex++;
    }

    while(rightIndex < right.length){
        sortedArr.push(right[rightIndex]);
        rightIndex++;
    }

    return sortedArr;
}

function test_merge_sort(){
    const assert = require('assert');

    let arr = mergeSort([1, 4, 2, 3, 5]);

    assert(arr[0] === 1);
    assert(arr[1] === 2);
    assert(arr[2] === 3);
    assert(arr[3] === 4);
    assert(arr[4] === 5);

    console.log('All test cases pass');
}

test_merge_sort();