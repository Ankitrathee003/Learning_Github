def exponent(x,n):
    flag=True
    if n<0 and flag:
        x=1/x
        n=-n
        flag=False
    if n==0:
        return 1
    if n%2==0:
        val=exponent(x,n/2)
        return val*val
    else:
        return x*exponent(x,n-1)
    
print(exponent(2,4))
    