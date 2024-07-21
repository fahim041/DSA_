def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def test_fibonacci():
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55
    print('All test cases pass')

test_fibonacci()