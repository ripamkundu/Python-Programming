class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
#Insert Node
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

#Delete Node
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

#Post Order      
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key) + "->", end=' ')
        

#Minimum Value       
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

#Count Total Number Of leaf Node
def count(self):
        if(root==None) or (root.left==None):
            return root
        else:
            return Node
            
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Post order traversal : ", end=' ')
postorder(root)
d=int(input("\nEnter node to be deleted :")) 
r = deleteNode(root, d)
print("\nAfter deleting specified node :")
postorder(root)

print("\nThe total number of leaf nodes : ")
count(Node)

print("\nValue of the node that is minimun in the Binary Search Tree : ")
minValueNode(root)
  
