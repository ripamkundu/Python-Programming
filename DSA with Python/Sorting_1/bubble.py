arr=[]
n=int(input("How Many Number You Want ?"))
print("Enter Your " + str(n) + " Number : ")
for k in range(n):
    d=int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("Sorted Array List : " +str(arr))

f = open ("bubblep.txt","w")
for i in range(len(arr)):
 f.write("%d"%arr[i])
f.close()
