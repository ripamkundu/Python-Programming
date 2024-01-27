# 1a) write a program in python 3 to test the greater, equal and lesser values with ladder if-else structure.
# b. define a new method to format all the string with the format method and capitalize every first characters with title() method.

def main():
    a=int(input("Enter a value of A -> "))
    b=int(input("Enter a value of B -> "))
    if a>b:
        print("A -> ",a, "B -> ",b, "\tA is greater than B")
        print("The difference between two values of A and B is -> ", a-b)
    elif a==b:
        print("A -> ",a, "B -> ",b, "\tA is equal to B")
    else:
        print("A -> ",a, "B -> ",b, "\tB is greater than A")
        print("The difference between two values of A and B is -> ", a-b)
def main_2():
    print("\n")
    a=str(input("Enter the value of string A -> "))
    b=str(input("Enter the value of string B -> "))
    c=str(input("Enter the value of string C -> "))
    d=str(input("Enter the value of string D -> "))
    final_string="{0}, {1}, {2}, {3}"
    final_string_print=final_string.format(a,b,c,d)
    final_string_print_title=final_string_print.title()
    print("Original String -> ", final_string_print)
    print("First Charater of each word capital -> ", final_string_print_title)
main()
main_2()
    






