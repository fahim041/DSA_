def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
    
    arr[e], arr[left] = arr[left], pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)

    return arr

def test_quick_sort():
    arr = [1, 3, 2, 4, 5]
    arr = quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    arr = quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    arr = quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1]
    arr = quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1]

    arr = []
    arr = quick_sort(arr, 0, len(arr) - 1)
    assert arr == []

    print("All tests pass")

test_quick_sort()
