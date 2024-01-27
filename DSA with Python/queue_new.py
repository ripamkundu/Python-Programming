class Node:
    def __init__(self,data):
        self.data=data
        self.ref1=None
class linked_Queue:
    def __init__(self):
        self.head=None
    def display(self):
        if(self.head==None):
            print("The linked list is emty")
        else:
            n=self.head
            print("The elements of the linked stack are:")
            while(n!=None):
                print(n.data,"-->",end="")
                n=n.ref
            print("None")
    def add_end(self,data):
        new_node=Node(data)
        if(self.head==None):
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            new_node.ref=n.ref
            n.ref=new_node
        print("%d is inserted successfully!"%(new_node.data))
    def del_beg(self):
        if(self.head==None):
            print("List is already empty")
            return
        print("%d is deleted successfully!"%(self.head.data))
        self.head=self.head.ref
if __name__=="__main__":
    ls=linked_Queue()
    while(1):
        print("\n 1. Insert an element into the queue")
        print("\n 2. Delete an element from the queue")
        print("\n 3. Display") 
        print("\n 4. Exit")
        ch=input("Enter your choice:")
        if(ch=='1'):
            a=int(input("element is inserted:"))
            ls.add_end(a)
        elif(ch=='2'):
            ls.del_beg()
        elif(ch=='3'):
            ls.display()
        elif(ch=='4'):
            break
        else:
            print("Wrong Input")
        
        
