from cgi import print_arguments


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return popped
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def display(self):
        if self.head is None:
            print("Nothing to Display.")
            return
        else:
            print("Stack List : ", stack)
a_stack = stack()
while True:
    print("push")
    print("Pop")
    print("quit")
    do = input("what would you like to do? ").split()
    n = do[0].split()
    if n == 'Push':
        a_stack.push(int(do[1]))
    elif n == 'Pop':
        popped = a_stack.pop()
        if popped is None:
            print("Stack is Empty..!")
        else:
            print("Popped Value : ", int(popped))
    elif n == 'quit':
        break
    
    