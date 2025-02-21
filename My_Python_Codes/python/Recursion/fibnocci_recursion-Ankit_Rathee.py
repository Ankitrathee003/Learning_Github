n=int(input("enter the no. of terms of fibnocci  "))
l=[]
def f(n):
        if n==1 or n==2:
            return(1)
        else:
            return(f(n-1)+f(n-2))
for i in range(1,n+1):
    (l.append(f(i)))
print(l)
print(f(n))








