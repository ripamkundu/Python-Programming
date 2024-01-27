def quick(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return(i + 1)
def quicksort(arr, low, high):
    if low < high:
        pi = (arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
arr = []
n =  int(input("How many element you want?"))
print("Enter Your" + Str(n) + "Data : ")
for i in range(n):
    d = int(input())
    arr.append(d)
print("Unsorted Array Is : ", arr)
quicksort(arr, 0 , n -1)
print("Sorted Array is  : ", arr)
        
