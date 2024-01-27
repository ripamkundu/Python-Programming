def tower_of_
-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          hanoi(n,s,d,t):
    if n==1:
        print("Move disk from {) to {}".format(s,d))
        return
    else:
        tower_of_hanoi(n-1,s,t,d)
        tower_of_hanoi(1,s,d,t)
        tower_of_hanoi(n-1,t,d,s)
n=int(input("Enter disk name:"))
a,b,c=[d for d in input("Enter disk name:").split()]
tower_of_hanoi(n,a,b,c)
