S =[]
top = None
def isempty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk)-1

def s_pop(stk):
    if(isempty(stk)):
        return('Underflow')
    else:
        i = stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top = top - 1
        return i

def display(stk):
    if(isempty(stk)):
        return('Empty stack')
    else:
        top = len(stk)-1
        print(stk[top])
        for i in range(top-1,-1,-1):
            print(stk[i])
while True:
    print('1.PUSH')
    print('2.POP')
    print('3.DISPLAY')
    print('4.EXIT')
    ch=input('enter choice')
    if(ch=='1'):
        item=int(input('Enter item to push :'))
        push(S,item)
        print('%d added'%item)

    elif(ch=='2'):
        item==s_pop(S)
        if(item=='underflow'):
            print('Empty stack')

    elif(ch=='3'):
        display(S)
    elif(ch=='4'):
        break
    else:
        print("Enter The correct Option.!")
        break
   
        