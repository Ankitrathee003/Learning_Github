x=0
if len(x)==(1 or 0):
    print(x)
else:
    y=1
    if x<0:
        x=x*(-1)
        y=y*(-1)

    x=[int(i) for i in str(x)]
    def reversing_list(x):
        n=len(x)
        if len(x)==(1 or 0):
            return(x)
        else:
            for i in range(n//2):
                x[i],x[len(x)-1-i]=x[len(x)-1-i],x[i]
            return(x)
    reversing_list(x)
    def remove_zero(x):
        i=0
        while i<=len(x):
            if x[i]==0:
                del x[i]
            else:
                return(x)
    remove_zero(x)

    z=(str(i) for i in x)
    y=int("".join(z))*y
print(y)
