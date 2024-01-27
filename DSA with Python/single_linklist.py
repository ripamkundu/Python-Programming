class Node:
    def _init_(self,data):
        self.info = data
        self.link=None
        
class single_Linkedlist:
    def _init_(self):
        self.head=None
        self.Last_Node=None
        
    def create (self,item):
        if self.head is None:
            self.head = Node
            self.Last_node = self.head
        else:
            self.Last_Node.link = Node(item)
            self.Last_Node = self.Last_Node.link
            
    def display (self):
        temp = self.head
        if self.head is None:
            print("\n Linkedlist is empty nothing to display")
        else:
            print("Element of the Linkedlist are :")
            while (temp != None):
                print(temp.imfo,end = " ")
                temp = temp.link
if __name__ == "__ main __":
    s = single_Linkedlist()
    print ("\n How many node you want to create :")
    n = int(input())
    for i in range(n):
        data=int(input("\n Enter the value of node %d", (i+1))
        s.create(data)
        print("\nDisplay List")
        s.display()
        
        
        
Output : 
How many node you want to create :
5
Enter the value of node 10
Enter the value of node 20
Enter the value of node 30
Enter the value of node 40
Enter the value of node 50

Display List
Element of the Linkedlist are :
10 20 30 40 50
