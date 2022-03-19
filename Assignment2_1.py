for i in range(1,10):
    if i<=5:
        for j in range(0,i):
             print('*',end=" ")
        print("\r")
    else:
        for j in range (10,i,-1):
            print('*', end=" ")
        print("\r")