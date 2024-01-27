class Node:
    def _init_(self, data):
        self.info = data
        self.link = None
        
class Single_Linkedlist:
    def __init__(self, data):
        self.head = None
        self.last_node = None

    def create(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.link = Node(data)
            self.last_node = self.last_node.link
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.link
        return False

    '''
    def search(self, key):
        temp = self.head
        flag = 0
        if(self.head == None):
            while (temp is not None):
                if (temp.info == key):
                    flag = 1
                temp = temp.link
                if (flag == 0):
                    print("Element is not found")
                else:
                    print("Element is found")'''

    def display(self):
        temp = self.head
        while (temp is not None):
            print(temp.info, end=" ")
            temp = temp.link
            
if __name__ =="__main__":
    sl = Single_Linkedlist(0)
    while True:
        print("1.Create") 
        print("2.search")
        print("3.Display") 
        print("4. Exit")
        n=input("Enter your choie :")
        if(n==1):
            n = int(input("\n how many nodes you want to create:"))
            for i in range(n):
                data = int(input("Enter the value:"))
                sl.create(data)
        elif(n==2):
            a=int(input("Enter the element you want to search"))
            sl.search(a)
        elif(n==3):
            sl.display()
        elif(n==4):
            print("you have exited")
            break
        else:
            print("wrong choice")
    