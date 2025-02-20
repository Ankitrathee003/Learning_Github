def nat(n):
    if n==0:
        return 0
    else:
        print(n)
        x=(nat(n-1))
        print(x)
        print(n*9)
nat(5)
        
