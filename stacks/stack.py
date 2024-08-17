class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __len__(self):
        return self.length

    def peek(self):
        if self.length == 0:
            raise ValueError("Stack is empty")
        
        return self.top.value

    def push(self, value):
        new_node = Node(value, None)

        if self.top is None:
            self.bottom = new_node
            self.top = new_node
            self.length += 1
            return
        
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return

    def pop(self):
        if self.length == 0:
            raise ValueError("Stack is empty")
        
        if self.top.next is None:
            item = self.bottom.value
            self.bottom = None
            self.top = None
            self.length -= 1
            return item
        
        current = self.top
        self.top = self.top.next
        self.length -= 1
        return current.value

    def is_empty(self):
        return self.length == 0
    

my_stack = Stack()
print(my_stack.is_empty())
my_stack.push(2)
my_stack.push(10)
my_stack.push(30)
my_stack.push(5)
my_stack.push(6)
print(my_stack.is_empty())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(len(my_stack))
print(my_stack.peek())

# Doubly linked list implementation of stack
from collections import deque

stack = deque()
stack.append(2)
stack.append(10)
stack.append(30)
stack.append(5)
stack.append(6)
print(len(stack))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.count(2))


