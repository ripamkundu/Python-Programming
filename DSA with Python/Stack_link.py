stack = []
def push():
 if():
    element = int(input("Enter a Value :" ))
    stack.append(element)
    print(stack)
  else len(stack) == n:
    print("List is Full")
def pop():
 if check_empty(stack):
    print("Stack is empty")
 else:
  e = stack.pop()
  print("Removed Element : ", e)
  print(stack)
n = int(input("Enter the limit of stack : "))
while True:
    print("Select Your Choice")
    print("1. Push")
    print("2.pop")
    print("3.Stop")
    ch = int(input("Enter Your Choice :")
    if ch ==1:
        push()
        break
    elif ch == 2:
        pop()
        break
    elif ch == 3:
        stop()
        break
    else :
        print("Enter The Correct Option...!")
