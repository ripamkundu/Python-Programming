l = []
num = int(input("Enter size of list : "))
for i in range(num):
 n = int(input("Enter a number :"))
 l.append(n)
 
x = int(input("Enter number to search: ")) 
found = False
for i in range(len(l)):
 if l[i] == x:
 found = True
 print(" found at position " % (x, i))
 break
if not found:
 print("is not in list ", x)