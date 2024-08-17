import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stacks.stack import Stack

class QueueStack:
    def __init__(self):
        self.first = Stack()
        self.last = Stack()
        self.length = 0

    def peek(self):
        if len(self.first) == 0:
            raise ValueError("Queue is empty")

        for _ in range(len(self.first)):
            self.last.push(self.first.pop())

        return self.last.peek()
    
    def enqueue(self, value):
        if self.length == 0:
            self.last.push(value)
        else:
            for _ in range(len(self.first)):
                self.last.push(self.first.pop())
        
            self.last.push(value)
        
        self.length += 1
        return
    
    def dequeue(self):
        if self.length == 0:
            raise ValueError("Queue is empty")

        for _ in range(len(self.last)):
            self.first.push(self.last.pop())

        self.length -= 1

        return self.first.pop()
    
my_queue = QueueStack()
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.enqueue(8)
print(my_queue.dequeue())
print(my_queue.dequeue())


