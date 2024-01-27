class Node:
   def __init__(self,data):
      self.data=data
      self.ref=None
      
class Linked_Stack:
   def __init__(self):
       self.head=None
   def print_ll(self):
       if(self.head==None):
          print("The linked list is empty")
       else:
          n=self.head
          print("The elements of the linked stack are:")
          while(n!=None):
             print(n.data,"-->",end=" ")
             n=n.ref 
          print("None")
   def add_beg(self,data):
       new_node=Node(data)
       new_node.ref=self.head
       self.head=new_node
       print("%d is inserted successfully!"%(new_node.data))
   def del_beg(self):
       if(self.head==None): 
          print("List is already empty")
          return
       print("%d is deleted successfully!"%(self.head.data))  
       self.head=self.head.ref 
  
llst=Linked_Stack() 
while(1):
   print("\n 1.push an element")
   print("\n 2.pop an element")
   print("\n 3. Display")
   print("\n 4. Exit")
   ch=input("Enter your choice:")
   if(ch=='1'):
      a=int(input("Enter element to be pushed:"))
      llst.add_beg(a)
   elif(ch=='2'):
      llst.del_beg()
   elif(ch=='3'):
      llst.print_ll()
   elif(ch=='4'):
      quit()
   else:
      print("Invalid choice.Try again!")
