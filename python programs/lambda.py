class Main:
    def test():
        x=lambda a,b:a*b
        print(x(5,5))
    test()
obj=Main()
obj.test
        
def helloworld(n):
    return lambda a:a*n
x=helloworld(3)  #n value
print(x(300))  #a value