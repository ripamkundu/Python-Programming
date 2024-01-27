#Queue using linklist

queue = []
def insert():
 n = input("Enter the Element : ")
 queue.append(n)
 
def delete():
 if check_empty(queue):
  print("Queue is empty.!")
 else:
  e = queue.pop(0)
  print("Removed Element : ",e)

def display():
 print(queue)
  
while True:
  print("Select your choice : ")
  print("1. Add Element")
  print("2. Removed Element")
  print("3. Show")
  print("4. Exit")
  c = int(input("Enter Your Choice : "))
  if c ==1 :
   insert()
  elif c == 2:
   delete()
  elif c == 3:
   display()
  elif c == 4:
   break
  else:
   print("Enter The correct operation.!")
 