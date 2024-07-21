def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

def test_insertion_sort():
    arr = [1, 3, 2, 4, 5]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1]
    insertion_sort(arr)
    assert arr == [1]

    arr = []
    insertion_sort(arr)
    assert arr == []

    print("All tests pass")

test_insertion_sort()