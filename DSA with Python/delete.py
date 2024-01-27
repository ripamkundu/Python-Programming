class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def deleteNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev 
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d " % (temp.data),end=" ")
            temp = temp.next
            
ob = LinkedList()
ob.push(7)
ob.push(1)
ob.push(3)
ob.push(2)
ob.push(8)
ob.push(21)
ob.push(10) 
ob.push(20)  
print ("Created Linked List: ")
ob.printList()
ob.deleteNode(4)
print ("\nLinked List after Deletion at position 4: ")
ob.printList()