#Stack using Class

class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        if(self.isFull() != True):
            self.index.append(data)
            print("Pushed Item : ",  data)
        else:
            print('Stack overflow')

    def pop(self):
        if(self.isEmpty() != True):
            return self.index.pop()
        else:
            print('Stack is already empty!')

    def isEmpty(self):
        return len(self.index) == []
        return myString

    def isFull(self):
        return len(self.index) == self.size
        return myString
 
    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

myStack = Stack(30)
for i in range(0, 15):
   myStack.push(i)
print(myStack.isEmpty())        
print(myStack.isFull())         
print(myStack)                  
print(myStack.Stack())      
print(myStack.pop())   