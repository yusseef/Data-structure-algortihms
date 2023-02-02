#There are two ways to create a stack, first with list 

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.pop() #remove lasst element LIFO
#print(stack)

#second way is using deque from collections

from collections import deque #it creates stack with doubly linkedlist

stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.pop() #remove lasst element LIFO
print(stack.peek())
print(stack)