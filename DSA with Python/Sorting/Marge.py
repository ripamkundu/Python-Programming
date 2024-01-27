def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)    
        mergeSort(right)
        i = 0       
        j = 0
        k = 0  

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]  
              i = i + 1      
            else:
                arr[k] = right[j]
                j = j + 1  
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k]=right[j]
            j =j + 1
            k =k + 1
def Display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr=[]
n=int(input("How Many Number You Want ?"))
print("Enter Your " + str(n) + " Number : ")
for k in range(n):
    d=int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))
mergeSort(arr)
print("Sorted Array : ", arr)
