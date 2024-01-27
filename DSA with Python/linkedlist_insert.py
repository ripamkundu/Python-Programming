class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_data

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The Given Previous Node Must Linked List.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def Display(self):
        temp = self.head
        while(temp):
            print(str(temp.data)+ " " , end = " ")
            temp = temp.next

list = Linkedlist()
list.insert_at_end(10)
list.insert_at_beg(20)
list.insert_at_beg(30)
list.insert_at_end(40)
list.insert_after(list.head.next, 8)
print("Linked List :")
list.Display()
print()
