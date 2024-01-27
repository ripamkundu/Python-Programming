# var_a=["test1","helloworld","google","python", "java", "javascript"]
# print(var_a," ",type(var_a))
# var_b=("test1","helloworld","google","python", "java", "javascript")
# print(var_b, " ", type(var_b))
# var_c={"test1","helloworld","google","python", "java", "javascript"}
# print(var_c, " ", type(var_c))


# list_1=["test1","helloworld","google","python", "java", "javascript","test5","test6","test9"]
# print(list_1[1:7+1])
# print("The length of the list is -> ",len(list_1))



# list_1=["techno", "google", 10, 200, 3000, 56.68, 969.1, 2+3j, 4+23j, True, False, 'A', 'X']
# print(list_1[0:2])

list_1=["python","javascript", "helloworld","test222","test333"]
# print("Original List -> ", list_1)
# list_1[0:4]=["yahoo.com","Saheb", "Elon Musk", "SpaceX"]  #it is replacing the old index element with the new element
# print("Modified List -> ", list_1)
# list_1.insert(0, 969.65)
# list_1.insert(1, "Messi")
# print("After Insertion method -> ", list_1)
# list_1.append("Narendra Modi")
# print("After Append Method -> ",list_1)
print("\nOriginal List -> ",list_1)
list_3=list_1[1:4]
print("\nList Limiting -> ",list_3)
# Merging two list together
# print("\nList 1 -> ",list_1)
list_2=["test1","test2","test3","test4","test5"]
print("\nList 2 -> ",list_2)
list_3.extend(list_2)
print("\nMerging Two list -> ",list_3)



