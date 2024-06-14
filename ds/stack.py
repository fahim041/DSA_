class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self, val):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]