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

    def breadth_first_search(self):
        current_node = self.root
        list_nodes = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            list_nodes.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return list_nodes

    def breadth_first_search_recursive(self, queue, list_nodes):
        if len(queue) == 0:
            return list_nodes
        
        current_node = queue.pop(0)
        list_nodes.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, list_nodes)


binary_tree = BinarySearchTree()
binary_tree.insert(20)
binary_tree.insert(25)
binary_tree.insert(29)
binary_tree.insert(5)
binary_tree.insert(18)
binary_tree.insert(19)
binary_tree.insert(3)
binary_tree.breadth_first_search()
binary_tree.breadth_first_search_recursive([binary_tree.root], [])
binary_tree.remove(18)

