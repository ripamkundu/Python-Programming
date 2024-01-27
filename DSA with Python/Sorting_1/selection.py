arr=[]
n=int(input("How Many Number You Want ?"))
print("Enter Your " + str(n) + " Data : ")
for k in range(n):
    d=int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))

for i in range(len(arr)-1):
    a = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[a]:
            a = j
    if arr[i] != arr[a]:
        swap = arr[a]
        arr[a] = arr[i]
        arr[i] = swap
print("Sorted Array Is :" +str(arr))

f = open ("selection.txt","w")
for i in range(len(arr)):
 f.write("%d"%arr[i])
f.close()
