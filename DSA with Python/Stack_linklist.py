#Stack using Linklist

stack = []
def push():
 if (): 
  element = input("Enter the element : ")
  stack.append(element)
  print(stack)
 else len(stack) == n:
  print("List is Full.!")

def pop_element():
 if check_empty(stack):
  print("Stack is empty.!")
 else:
  e = stack.pop()
  print("Removed Element : ",e)
  print(stack)
  
n = int(input("Enter limit of stack : "))
while True:
  print("Select your choice : ")
  print("1. push")
  print("2. pop")
  print("3. Stop")
  c = int(input)
  if c == 1:
   push()
  elif c == 2:
   pop_element()
  elif c == 3:
   break
  else:
   print("Enter the correct operation.!")
  