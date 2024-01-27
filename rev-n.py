# input = "Ripam Kundu"

def rev(input):
    n =  " "
    for i in range(len(input) -1, -1, -1):
        n = n+input[i]
    return n

input = "Ripam Kundu"
rs = rev(input)
print('Result', rs)

