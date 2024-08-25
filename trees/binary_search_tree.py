class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value, None, None)

        if not self.root:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left is None:
                    current_node.left = new_node
                    self.length += 1
                    return new_node
                current_node = current_node.left
            elif current_node.value < value:
                if current_node.right is None:
                    current_node.right = new_node
                    self.length += 1
                    return new_node
                current_node = current_node.right
            else:
                raise ValueError("Value is duplicated")

    def lookup(self, value):
        if self.length == 0:
            raise ValueError("Tree is empty")
        
        current_node = self.root
        while current_node is not None:
            if current_node.value > value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
            else:
                return current_node
        return False

    def remove(self, value):
        if self.length == 0:
            raise ValueError("Tree is empty")
        
        current_node = self.root
        previous_node = None
        while current_node is not None:
            if value > current_node.value:
                previous_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                previous_node = current_node
                current_node = current_node.left
            else:
                if current_node.left is None and current_node.right is None:
                    if previous_node is None:
                        self.root = None
                    elif current_node == previous_node.left:
                        previous_node.left = None
                    else:
                        previous_node.right = None
                    self.length -= 1

                elif current_node.left is None: 
                    if previous_node is None:
                        self.root = current_node.right
                    elif current_node == previous_node.left:
                        previous_node.left = current_node.right
                    else:
                        previous_node.right = current_node.right
                    self.length -= 1

                elif current_node.right is None:
                    if previous_node is None:
                        self.root = current_node.left
                    elif current_node == previous_node.left:
                        previous_node.left = current_node.left
                    else:
                        previous_node.right = current_node.left
                    self.length -= 1

                # Case 3: Node has two children
                else:
                    successor_parent = current_node
                    successor = current_node.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left

                    current_node.value = successor.value

                    # Delete the successor node
                    if successor_parent != current_node:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

                    self.length -= 1

                return current_node

        return current_node

    def print(self):
        def in_order_traversal(node):
            if node is not None:
                in_order_traversal(node.left)
                print(node.value, end=" ")
                in_order_traversal(node.right)

        in_order_traversal(self.root)

binary_tree = BinarySearchTree()
binary_tree.insert(20)
binary_tree.insert(25)
binary_tree.insert(29)
binary_tree.insert(5)
binary_tree.insert(18)
binary_tree.insert(19)
binary_tree.insert(3)
binary_tree.print()
print(binary_tree.lookup(100))
binary_tree.remove(18)
binary_tree.print()

