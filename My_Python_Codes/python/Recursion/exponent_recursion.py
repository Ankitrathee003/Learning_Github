x=int(input("enter the value of x  "))
n=int(input("enter the value of n  "))
def fun(x,n):
        if n==0:
            return 1
        elif x==0:
            return 0
        else:
            return(x*fun(x,n-1))
print(fun(x,n))
