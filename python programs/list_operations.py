# list_1=["mainak","college","java", "python", 56, 2589, 265.96]
# print(list_1)
# print("\n")
# print("List Printing in For Loop.....")
# for x in list_1:   #iteration operation i.e accessing each and every elements in the list
#     print(x)
    
# print("\n")
# print("List Printing In While Loop......")
# i=3
# while i< len(list_1):  #length of the list is greater than than the i=0
#     print(list_1[i])
#     i=i+1     #iteration in while loop


#User Input in LIST


# list_1=[]
# list_2=[]
# n=int(input("Enter the no. of elements you want to store in the list -> "))
# for i in range(0,n):
#     ram=int(input())
#     list_1.append(ram)
# m=int(input("Enter the no. of elements you want to store in the string list -> "))
# for j in range(0,m):
#     shyam=str(input())
#     list_2.append(shyam)
# print("Final List -> ",list_2+list_1)


#user input list Ascending and descending order----------

def ascending():
    list_a=[]
    n=int(input("Enter no. of list elements -> "))
    for i in range(0,n):
        x=int(input())
        list_a.append(x)
    print("Final List -> ", list_a)
    list_a.sort()
    print("List in Ascending Order -> ", list_a)

def descending():
    list_b=[]
    n=int(input("Enter no. of list elements -> "))
    for i in range(0,n):
        x=int(input())
        list_b.append(x)
    print("Final List -> ", list_b)
    list_b.sort(reverse=True)
    print("List in Descending Order -> ", list_b)
print("Ascending Order -> ")
ascending()
print("\n")
print("Descending Order -> ")
descending()






















    




























