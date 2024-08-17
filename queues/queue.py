class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __len__(self):
        return self.length

    def peek(self):
        if self.length == 0:
            raise ValueError("Queue is empty")
        
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return

    def dequeue(self):
        if self.length == 0:
            raise ValueError("Queue is empty")
        
        if self.first == self.last:
            self.last = None

        current = self.first
        self.first = current.next
        self.length -= 1
        return current.value

    def is_empty(self):
        return self.length == 0
    
my_queue = Queue()
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

# Doubly linked list queue implementation
from collections import deque

queue = deque()
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())



