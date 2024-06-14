class StaticArray:
    def __init__(self,size):
        if size <= 0:
            raise ValueError('Size must be greater than 0')
        self.size = size
        self.arr = [None] * size
        self.count = 0

    def __len__(self):
        return self.size

    def append(self, val):
        if self.count >= self.size:
            raise OverflowError('Array is full')
        self.arr[self.count] = val
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError('Array is empty')
        index = self.count - 1
        val = self.arr[index]
        self.arr[index] = None
        self.count -=1
        return val

    def insert(self, index, val):
        if not 0 <= index <= self.count:
            raise IndexError('Index is out of bound')
        if self.count >= self.size:
            raise OverflowError('Array is full')
        for i in range(self.count, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = val
        self.count += 1

    def remove(self, index):
        if not 0 <= index <= self.count:
            raise OverflowError('Index is out of bound')
        for i in range(index, self.count - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.count - 1] = None
        self.count -= 1

    def print(self):
        if self.count <= 0:
            raise IndexError('Array is empty')
        for i in self.arr:
            if i:
                print(i)

# test cases
def test_static_array():
    sa = StaticArray(5)
    sa.append(1)
    sa.append(2)
    sa.append(3)
    sa.append(4)
    sa.append(5)

    sa.pop()
    sa.insert(2, 3)
    sa.remove(1)

    assert len(sa.arr) == 5
    assert sa.count == 4
    assert sa.arr[1] == 3

    print('All test cases pass')

test_static_array()