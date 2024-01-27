# Binary Search in python

def Binary_Search(List, k):
	low = 0
	high = len(List) - 1
	mid = 0

	while low < high:

		mid = (high + low) // 2

		# means k is present at mid
		if List[mid] == k:
			return mid
			
		# If k is smaller, ignore right half
		elif List[mid] > k:
			high = mid - 1

		# If k is greater, ignore left half
		else:
			low = mid + 1

	# If we reach here, then the element was not present
	return -1
	
List = input("Enter the numbers for your list: ")
List = List.split()
List = [int(x) for x in List]  
print ("Your List is:", List)
k = int(input("Enter number to search: "))  

index = Binary_Search(List, k) 

if (index == -1):
    print(k, "not Found")
else:
    print(k, "Found at Index", index)
