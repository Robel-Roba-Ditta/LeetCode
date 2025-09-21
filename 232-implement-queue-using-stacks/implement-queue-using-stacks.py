class MyQueue:
    def __init__(self):
        self.append_stack = []
        self.inverted_stack = []

    def push(self, x):
        self.append_stack.append(x)

    def pop(self):
        if not self.inverted_stack:
            while self.append_stack:
                self.inverted_stack.append(self.append_stack.pop())
        return self.inverted_stack.pop()

    def peek(self):
        if not self.inverted_stack:
            while self.append_stack:
                self.inverted_stack.append(self.append_stack.pop())
        return self.inverted_stack[-1]

    def empty(self):
        return not (self.append_stack or self.inverted_stack)