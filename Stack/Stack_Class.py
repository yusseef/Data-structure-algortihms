from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, n):
        self.container.append(n)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)
