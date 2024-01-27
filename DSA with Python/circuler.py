class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class cicular:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.empty() is True:
            self.head = Node(val)
            self.head.next = self.head
            print("Head value created")
            return
        print("1. add a Node at the beginning")
        print("2. add a Node at the end")
        print("3. add a Node in the middle")
        print("Enter Your Choice :: ")
        opt = int(input())
        if opt == 1:
            a = Node(val)
            a.next = self.head
            n = self.head
            while n.next is not self.head:
                n = n.next
            n.next = a
            self.head = a
        elif opt == 2:
            i = self.head
            while i.next is not self.head:
                i = i.next
            i.next = Node(val)
            i.next.next = self.head
        elif opt == 3:
            pos = int(input("Enter the position ::"))
            i = 1
            n = self.head
            f = n.next
            flag = 0
            while f is not self.head:
                if i == pos:
                    flag = 1
                    break
                f = f.next
                n = n.next
                i = i + 1
            if flag == 1:
                n.next = Node(val)
                n.next.next = f
            else:
                print("Position not found")

    def delete(self):
        if self.empty() is True:
            print("Linked List empty")
            return
        elif self.head.next is self.head:
            self.head = None
            return
        print("1.Delete the beginning element ")
        print("2. Delete the last element")
        print("3. Delete elements in between")
        print("Enter Your CHoice ::")
        opt = int(input())
        if opt == 1:
            n = self.head
            while n.next is not self.head:
                n = n.next
            n.next = self.head.next
            self.head = self.head.next
        elif opt == 2:
            n = self.head
            while n.next.next is not self.head:
                n = n.next
            n.next = self.head
        else:
            print("1. Delete by position")
            print("2. Delete by Value")
            print("Enter Your Choice ::")
            op = int(input())
            if op == 1:
                pos = int(input("Enter the position ::"))
                i = 1
                n = self.head
                f = self.head.next
                flag = 0
                while f.next is not self.head:
                    if i == pos:
                        flag = 1
                        break
                    i = i + 1
                    n = n.next
                    f = f.next
                if flag == 1:
                    n.next = f.next
                else:
                    print("Position not found")
                    return
            else:
                val = int(input("Enter the value you want to delete ::"))
                n = self.head
                f = self.head.next
                flag = 0
                while f.next is not self.head:
                    if f.value == val:
                        flag = 1
                        break
                    f = f.next
                    n = n.next
                if flag == 1:
                    n.next = f.next
                else:
                    print("Value not found")
                    return
    def clear(self):
        self.head = None
        print("Linked List cleared")

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def display(self):
        if self.empty() is True:
            print("Linked List empty")
            return
        print("THE LINKED LIST")
        print(self.head.value, " <== HEAD")
        n = self.head.next
        while n is not self.head:
            print(n.value)
            n = n.next
        print("Linked List ends")
        
c = cicular()
while True:
    print("1. add an element")
    print("2. Delete an element")
    print("3. clear the Linked")
    print("4.Display")
    print("5. Exit")
    print("Enter Your Choice ::")
    option = int(input())
    if option == 1:
        value = int(input("Enter the value you want to add ::"))
        c.add(value)
        continue
    elif option == 2:
        c.delete()
        continue
    elif option == 3:
        c.clear()
        continue
    elif option == 4:
        c.display()
        continue
    elif option == 5:
        print("Good Bye")
        break
    elif option == 6:
        print(c.empty())
    else:
        print("Wrong option")