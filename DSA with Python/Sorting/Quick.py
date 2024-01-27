def quick(arr,low,high):
   i = (low - 1)
   pivot = arr[high] 
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):
   if low < high:
      pi = quick(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

arr = []
n = int(input("How many element Would you want ?"))
print("Enter Your " + str(n) + " Number : ")
for k in range(n):
    d = int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))
quickSort(arr,0,n-1)
print ("Sorted array is : ", arr)
