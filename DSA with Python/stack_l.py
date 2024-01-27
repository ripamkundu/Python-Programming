class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
while True:
    print('1.push <value>')
    print('2. pop')
    print('3. quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == '1':
        s.push(int(do[0]))
    elif operation == '2':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == '3':
        break