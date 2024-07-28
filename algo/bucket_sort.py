def bucket_sort(arr):
    counts = [0] * 6

    for n in arr:
        counts[n] += 1
    
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

def test_bucket_sort():
    arr = [1, 3, 2, 4, 5]
    arr = bucket_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    arr = bucket_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    arr = bucket_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1]
    arr = bucket_sort(arr)
    assert arr == [1]

    arr = []
    arr = bucket_sort(arr)
    assert arr == []

    print("All tests pass")

test_bucket_sort()