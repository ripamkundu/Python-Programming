def operations():
    a=float(input("Enter 1st number -> "))
    b=float(input("Enter 2nd number -> "))
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    print("\n---------RESULT-------------")
    print("Add -> ",round(add,1))
    print("Substract -> ",round(sub,1))
    print("Division -> ",round(div,1))
    print("Multiplication -> ",round(mul,1))
def string_operations():
    print("\n")
    a=str(input("Enter your name -> "))
    b=str(input("Enter your address -> "))
    c=str(input("Enter your phone number -> "))
    d=str(input("Enter your age -> "))
    about_me="My name is {0} , I stay in {1} , my contact number is {2} , & my age is {3}"
    print("\n---------RESULT-------------")
    print(about_me.format(a,b,c,d))
operations()
string_operations()
    
    