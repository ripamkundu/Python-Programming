class Node:
    def __init__(self,data):
        self.info = data
        self.prev = None
        self.next = None

class Double_linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def create(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self,data,after):
        new_node = Node(data)
        temp = self.head
        while(temp.info != after):
            temp = temp.next
        temp.next.prev = new_node
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_before(self,data,before):
        new_node = Node(data)
        temp = self.head
        while(temp.info != before):
            temp = temp.next
        temp.prev.next = new_node
        new_node.prev = temp.prev
        temp.prev = new_node
        new_node.next = temp

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
      
    def delete_from_beg(self):
        temp = self.head
        if temp is None:
            print("\nNothing to Delete..!")
        else:
            x = temp.info
            temp.next.prev = None
            self.head = self.head.next
            temp = None
            return x

    def display(self):
        temp = self.head
        if self.head is None:
            print("\nNothing to Display")
            return
        else:
            print("\nElements of the double linkedlist are :",end = " ")
            while(temp is not None):
                print(temp.info,end = " ")
                temp = temp.next
                
    def display_reverse(self):
        temp = self.tail
        if self.tail is None:
            print("\nNothing to Display")
        else:
            print("\nElements of the doublelinked list are : ",end = " ")
            while(temp is not None):
                print(temp.info,end = " ")
                temp = temp.prev
                             
if __name__=="__main__":
    dl=Double_linklist()
    while True:
        print("\nPlease Select Your Choice...! ") 
        print("1. create " ) 
        print("2. Insert At Begining ") 
        print("3. Insert After") 
        print("4. Insert Before") 
        print("5. Insert At End")
        print("6. Delete From Begining") 
        print("7. Display") 
        print("8. Display Reverse")
        print("9. Exit")
        print("\nEnter your choice :")
        n = int(input())
        if(n==1):
            print("How Many Node You Want to Insert.?")
            a = int(input())
            for i in range(a):
                data=int(input("Enter the value of data :"))
                dl.create(data)
        elif(n==2):
            print("Enter the value you want to insert the begging :")
            a = int(input())
            dl.insert_at_beg(a)
        elif(n==3):
            print("Enter the value you want to insert after :")
            a = int(input())
            dl.insert_after(a)
        elif(n==4):
            print("Enter the value you want to insert Before :")
            c = int(input())
            dl.insert_before(c)
        elif(n==5):
            print("Enter the value you want to insert the end position :")
            d = int(input())
            dl.insert_at_end(d)
        elif(n==6):
            print("Enter the value you want to delete :")
            e = int(input())
            dl.delete_from_beg(e)
        elif(n==7):
            dl.display()
        elif(n==8):
            dl.display_reverse()
        elif(n==9):
            exit()
        else:
            print("wrong choice....!")
            break
            
            
            





        
        
        
        
        
        
        
            
        
            
            
            
        
        
        
