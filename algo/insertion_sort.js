function insertionSort(arr){
    for(let i = 1; i < arr.length; i++){
        let j = i - 1;
        while(j >= 0 && arr[j] > arr[j + 1]){
            let tmp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = tmp;
            j--;
        }
    }
    return arr;
}

function test_insertion_sort(){
    const assert = require('assert');

    let arr = insertionSort([1, 4, 2, 3, 5]);

    assert(arr[0] === 1);
    assert(arr[1] === 2);
    assert(arr[2] === 3);
    assert(arr[3] === 4);
    assert(arr[4] === 5);

    console.log('All test cases pass');
}

test_insertion_sort();