import custom_Queue
class Node:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None
class binary_tree:
    def __init__(self):
        self.root = Node()
        self.high = 0
    def preorder_Traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        print(node.data)
        if node.left is not None:
            self.preorder_Traversal(node.left)
        if node.right is not None:
            self.preorder_Traversal(node.right)
    
    def inorder_Traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.left is not None:
            self.inorder_Traversal(node.left)
        print(node.data)
        if node.right is not None:
            self.inorder_Traversal(node.right)
    def postorder_Traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.left is not None:
            self.postorder_Traversal(node.left)
        if node.right is not None:
            self.postorder_Traversal(node.right)
        print(node.data)
    def level_order(self):
        if(self.root == None):
            return
        else:
            queue = custom_Queue.Queue(100)
            queue.enqueue(self.root)
            while not queue.isEmpty():
                current = queue.dequeue()
                print(current.data)
                if current.left is not None:
                    queue.enqueue(current.left)
                if current.right is not None:
                    queue.enqueue(current.right)    
        return None
if main == '__main__':
    obj = binary_tree()
    obj.root.data = 1
    obj.root.left = Node()
    obj.root.left.data = 2
    obj.root.right = Node()
    obj.root.right.data = 3
    obj.root.left.left = Node()
    obj.root.left.left.data = 4
    obj.root.left.right = Node()
    obj.root.left.right.data = 5
    obj.root.right.left = Node()
    obj.root.right.left.data = 6
    obj.root.right.right = Node()
    obj.root.right.right.data = 7
    print("Preorder Traversal:")
    obj.preorder_Traversal()
    print("Inorder Traversal:")
    obj.inorder_Traversal()
    print("Postorder Traversal:")
    obj.postorder_Traversal()
    print("Level Order Traversal:")
    obj.level_order()   
    print("Binary Tree Traversal Completed")
else:
    print("This script is not meant to be run directly.")