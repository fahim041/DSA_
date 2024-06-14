class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
# test cases
def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.pop()
    stack.pop()

    assert stack.peek() == 3

    print('All test cases pass')

test_stack()