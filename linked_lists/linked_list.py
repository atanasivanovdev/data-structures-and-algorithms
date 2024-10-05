class Node():
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def append(self, value):
        node = Node(value, None, None)

        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def prepend(self, value):
        node = Node(value, None, None)

        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.length += 1

    def insert(self, value, index=0):
        if index > self.length or index < 0:
            raise IndexError("Index out of range")

        new_node = Node(value, None, None)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = self.head
            return
        
        if index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(index-1):
            current = current.next

        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

        if new_node.next == None:
            self.tail = new_node

    def remove(self, value):
        if self.head is None:
            raise ValueError("List is empty")

        current = self.head

        if current.value == value:
            if current.next is not None:
                current.next.prev = None

            self.head = current.next
            self.length -= 1

            if self.head is None:
                self.tail = None
            return

        while current is not None:
            if current.value == value:
                if current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1 
                return

            current = current.next

    def remove_first(self):
        if self.head is None:
            raise ValueError("List is empty")
        
        current = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return current

        self.head = current.next
        self.head.prev = None
        self.length -= 1

        return current

    def remove_last(self):
        if self.head is None:
            raise ValueError("List is empty")
        
        current = self.tail

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return current
        
        self.tail = current.prev
        self.tail.next = None
        self.length -= 1
        
        return current
    
    def delete_duplicates(self):
        if self.head is None:
            raise ValueError("List is empty")
        
        if self.head.next is None:
            return
        
        left, right = self.head, self.head.next
        while right is not None:
            if left.value != right.value:
                left.next = right
                left = right
                self.length -= 1
            right = right.next
        left.next = None

    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        
        prev = self.head
        current = self.head.next
        self.head.next = None

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.tail = self.head
        self.head = prev

    def remove_nth_node_from_end(self, n):
        if self.head is None:
            return
        
        slow = fast = self.head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            self.head = self.head.next
            return

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        

    def display(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.remove_nth_node_from_end(2)
linked_list.reverse()
linked_list.delete_duplicates()
linked_list.append(10)
linked_list.append(4)
linked_list.prepend(89)
linked_list.prepend(32)
linked_list.insert(16, 3)
linked_list.remove_first()
linked_list.remove_last()
linked_list.remove_last()
linked_list.remove_first()
linked_list.display()
