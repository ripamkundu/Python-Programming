# Python program for linear search

def Linear_Search(List, key):  
    for i in range(len(List)): 
        if (List[i] == key): 
            return i 
    return -1

List = input("Enter the numbers for your list: ")
List = List.split()
List = [int(x) for x in List]  
print ("Your List is:", List)
key = int(input("Enter number to search: "))  

index = Linear_Search(List, key) 

# display result
if (index == -1):
    print(key, "not Found")
else:
    print(key, "Found at Index", index)