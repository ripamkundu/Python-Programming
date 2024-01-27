def test_1():
    a=int(input("Enter the value of A -> "))
    b=int(input("Enter the value of B -> "))
    if a>b:
        print("A -> ", a ,"B -> ",b, "\tA is greater than B ")
        c=a-b
        print("The difference between two values are ->  ", c)
    elif a==b:
        print("A -> ", a ,"B -> ",b, "\tA is equal to B")
    else:
        print("A -> ", a ,"B -> ",b, "\tB is greater than A ")
test_1()
        