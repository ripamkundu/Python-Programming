def create_stack():                 # Creating a stack
    stack = []
    return stack
def check_empty(stack):             # Creating empty stack
    return len(stack) == 0
def push(stack, item):
    item = input("Enter the element : ")              # Adding items into the stack
    stack.append(item)
    print("pushed element in the list : ",item)
def pop(stack):                     # Remov the element from the stack
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str())
push(stack, str())
push(stack, str())
push(stack, str())
push(stack, str())
print("Full Stack in the list : ",stack)
print("popped item List In array : ",pop(stack))
print("stack after popping element: ",stack)
print("popped item List In Array : ",pop(stack))
print("stack after popping element: ",stack)
print("popped item List In Array : ",pop(stack))
print("stack after popping element: ",stack)
