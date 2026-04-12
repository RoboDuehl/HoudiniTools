class Node: 
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.value = key 

class BinaryTree: 
    def __init__(self): 
        self.root = None 

    def find_node(self, node, key): 
        if node is None or node.value == key: 
            return node 
        elif key < node.value: 
            return self.find_node(node.left, key) 
        else: 
            return self.find_node(node.right, key) 
