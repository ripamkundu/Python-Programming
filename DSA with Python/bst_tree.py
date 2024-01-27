class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      
class Tree:
   def insert(self, data):
    if self.data:
        if (data < self.data):
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
               
        else (data > self.data):
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
    else:
        self.data = data
                 
   def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res
      
    def Preorder(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.Preorder(root.left)
         res = res + self.Preorder(root.right)
      return res
      
   def Postorder(self, root):
    res = []
    if root:
        res = self.Postorder(root.left)
        res = res + self.Postorder(root.right)
        res.append(root.data)
    return res   

   def display(self):
      if self.left:
         self.left.display()
      print(self.data)
      if self.right:
         self.right.display()
         
ob = Tree()
n = int(input("How many Node you want to insert?"))
print("Enter Your" + str(n) + " Element " )
for i in range(n):
 data = int(input("Enter your data : ")
 root.append(data)
print("Inorder Traversal Is : ")
ob.inorder(data)
ob.display(data)

print("Pre-order Traversal Is : ")
ob.Preorder(data)
ob.display(data)

print("Post-order Traversal Is : ")
ob.Postorder(data)
ob.display(data)


 
