def binary_search(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = L + (R - L) // 2
        
        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1

def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert binary_search(arr, 5) == 2
    assert binary_search(arr, 19) == 9
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 20) == -1
    assert binary_search(arr, 10) == -1
    
    print('All test cases pass')

test_binary_search()