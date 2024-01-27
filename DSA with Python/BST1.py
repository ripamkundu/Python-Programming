class BST:
    def _init_(self,data):
        self.key=data
        self.left=None
        self.right=None
    
    def insert(self,data):
        if self.key==data:
            return
        if self.key==None:
            self.key==data
            return
        if self.key>data:
            if(self.left):
                self.left.insert(data)
            else:
                self.left=BST(data)
        else:
            if(self.right):
                self.right.insert(data)
            else:
                self.right=BST(data)
    def postorder(self,root):
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key,end=" ")  
    def cln(self,root):
        if(root==None):
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return(self.cln(root.left)+self.cln(root.right))     

    def gmin(self,root):
        if(root==None) or (root.left==None):
            return root
        else:
            return (self.gmin(root.left))     
                
    def delete_Node(self,root, val):
        if not root: 
            return root
        
        if root.key > val: 
            root.left =self.delete_Node(root.left, val)

        elif root.key < val: 
            root.right=self.delete_Node(root.right, val)
        
        else: 
        
            if not root.right:
                return root.left
        
            if not root.left:
                return root.right
    
            temp_val = root.right
            mini_val = temp_val.key
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.key
    
            root.right = self.delete_Node(root.right,root.key)           
        return root
    
root=int(input("Enter the root node value:"))
ls=[]
n=int(input("Enter the number of nodes you want to insert apart froms the root node:"))
print("Enter %d elements:"%n)
for i in range(n):
   ele=int(input())
   ls.append(ele)

obj=BST(root)
for i in ls:
    obj.insert(i)
print("\nThe tree elements in post order are:")
obj.postorder(obj)
print("\nThe total number of leaf nodes=",end=" ")
print(obj.cln(obj))
tr=obj.gmin(obj)
print("\nValue of the node that is minimun in the Binary Search Tree=",tr.key)   
d=int(input("\nEnter node to be deleted:")) 
result = obj.delete_Node(obj, d)
print("\nAfter deleting specified node:")
print(result.postorder(result))