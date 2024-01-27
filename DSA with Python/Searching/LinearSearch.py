# Linear Search in Python

def Linear_Search(List, n, k):

    # Going through array sequencially
    for i in range(0, n):
        if (List[i] == k):
            return i
    return -1


List = [16, 45, 90, 21, 79]
k = 79
n = len(List)
index = Linear_Search(List, n, k)
if(index == -1):
    print("Element not found")
else:
    print(k, "found at index: ", index)