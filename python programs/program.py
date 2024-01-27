def even():
    a=int(input("Enter the starting point number -> "))
    b=int(input("Enter the ending point number -> "))
    print("\n-------EVEN NUMBERS--------")
    for x in range(a,b+1):
        if x%2==0:
            print(x, end=" ")
def odd():
    print("\n")
    a=int(input("Enter the starting point number -> "))
    b=int(input("Enter the ending point number -> "))
    print("\n")
    print("-------ODD NUMBERS--------")
    for x in range(a,b+1):
        if x%2==1:
            print(x, end=" ")
even()
odd() 
    
    