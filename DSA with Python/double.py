#Write a function to delete an element of double linked list from specific position

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode
      newNode.prev = temp

  def pop_at(self, position):     
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1 and self.head != None):
      nodeToDelete = self.head
      self.head = self.head.next
      nodeToDelete = None
      if (self.head != None):
        self.head.prev = None
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None and temp.next != None):
        nodeToDelete = temp.next
        temp.next = temp.next.next
        if(temp.next.next != None):
          temp.next.next.prev = temp.next  
        nodeToDelete = None 
      else:
        print("\nThe node is already null.")

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")
            
MyList = LinkedList()
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()
MyList.pop_at(2)
MyList.PrintList()
MyList.pop_at(1)
MyList.PrintList() 