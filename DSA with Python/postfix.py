def Postfix(n):
    stack = []
    for charact in n:
        if charact.isdigit():
            stack.append(int(charact))
        else:
            f = stack.pop()
            s = stack.pop()
            if charact == '+':
                stack.append(s + f)
            
            elif charact == '-':
                stack.append(s - f)
 
            elif charact == '×':
                stack.append(s * f)
           
            elif charact == '/':
                stack.append(s // f)
    return stack.pop()
n = input("Enter postfix Expression = ")
print("Result of the  postfix expression = ", Postfix(n))