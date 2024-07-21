def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def test_factorial():
    assert fact(5) == 120
    assert fact(4) == 24
    assert fact(3) == 6
    assert fact(2) == 2
    assert fact(1) == 1
    assert fact(0) == 1
    print('All test cases pass')

test_factorial()