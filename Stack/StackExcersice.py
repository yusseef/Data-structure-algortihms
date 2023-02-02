#reverse string with stack
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


def reverse_string(string):
    stack = Stack()
    for ch in string:
        stack.push(ch)
    print(stack)
    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()
    return rstr


print(reverse_string('hello world'))