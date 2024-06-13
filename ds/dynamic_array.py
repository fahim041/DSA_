class DynamicArray:
    def __init__(self):
        self.size = 2
        self.arr = [None] * self.size
        self.count = 0

    def append(self, val):
        if self.count == self.size:
            self.resize()
        self.arr[self.count] = val
        self.count += 1

    def resize(self):
        self.size = 2 * self.size
        newArr = [None] * self.size

        for i in range(self.count):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def pop(self):
        if self.count <= 0:
            raise BaseException('out of index')
        index = self.count - 1
        val = self.arr[index]
        self.arr[index] = None
        self.count -= 1
        return val

    def print(self):
        if self.count <= 0:
            raise BaseException('out of index')
        for i in range(self.count):
            if self.arr[i]:
                print(self.arr[i])