# class Google:
#     def __init__(x,name, title):  #__init__ is used to assign values to the object
#         x.abc=name
#         x.xyz=title
#     def test(x):
#         print(x.abc+" "+x.xyz)
# obj=Google("Mainak", "Deb") 
# obj.test()
# # print(x.abc, x.xyz)
# #object value modification-----------
# obj.xyz="python"
# obj.abc="Saheb" 
# # print("\nAfter Modification-----")     
# obj.test()













#   I N H E R I T E N C E    I N    P Y T H O N

class Main:
    def __init__(self):
        self.abc=str(input("fname -> "))
        self.xyz=str(input("lname -> "))
        
    def test(self):
        print(self.abc + " "+ self.xyz)

class Main_2(Main):
    pass
class Main_3(Main_2):
    pass

obj=Main_3()
obj.test()
    
    
    
    
    
# class Hello:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
        
#     def mit(self):
#         print("First name -> ",self.firstname,"\nLast name -> ",self.lastname,"\nIdentification -> ",self.identify) 
# class Hello_2(Hello):
#     def __init__(self,fname,lname,id):
#         super().__init__(fname,lname)
#         self.identify=id
        
        
#     def mit_2(self):
#         print("First name -> ",self.firstname,"\nLast name -> ",self.lastname,"\nIdentification -> ",self.identify)

# obj=Hello_2("Mainak","Deb",888888888)
# obj.mit_2()    #this is from child class
# print("\n")
# obj.mit()   #this is from parent class 
    
    
 
 
 
 
  
    

    
# class Test
# {
#     public static void main(String args[])
#     {
#         System.out.print("test");
#         System.out.println("test");
#     }
# }
    
     
# class Test:
#     def main():
#         # a=int(input("Enter a number -> "))
#         b=str(input("Enter Your name -> "))   #0
#         c=str(input("Enter your college name -> "))    #1
#         d=str(input("Enter your roll no -> "))     #2
#         a=str(input("Enter your address -> "))    #3
#         final_str="NAME -> {0}, \nCOLLEGE -> {1} , \nROLL NO -> {2}, \nAddress -> {3}"
#         print(final_str.format(b,c,d,a))
#         print("Test\nTest1")
#     main()
# obj_1=Test
# obj_1.main
 
 

     


# class Array:
#     def main():
#         list_1=[]
#         n=int(input("Enter the no. of elements of array -> "))
#         for x in range(0,n):
#             y=int(input())
#             list_1.append(y)
#         print("Original Array -> ",list_1)
#         list_1.sort()
#         print("Ascending Order -> ", list_1)
#         list_1.sort(reverse=True)
#         print("Descending Order -> ",list_1)
#     main()
# obj_xyz=Array()
# obj_xyz.main
            
            
         
        
    
    
    
    
    
    
    
    
    
    






