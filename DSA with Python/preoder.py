class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        
    def Preorder(root):
        if root:
            print(str(root.val)+ "->", end =" ")
            preorder(root.left)
            preorder(root.right)
            
    def insert(node, key):
        if node is None:
            return Node(key)
        if key<node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
        return node
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.key),
        if self.right:
            self.right.PrintTree()
root = None
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 5)
root = insert(root, 10)
root = insert(root, 6)
root = insert(root, 18)
root = insert(root, 4)
root = insert(root, 27)

print("Per-order Traversal : ", end = " ")
preorder(root)
