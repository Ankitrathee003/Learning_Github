def fib(n):
    a,b=0,1
    for i in range (n):
        temp=a
        a=b
        b+=temp
    return a
# print(fib(5))



       
factTable={}
def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n==0:
            factTable[0]=1
            return 1
        else:
            factTable[n]=n*factorial(n-1)
            print(factTable)
            return factTable[n]

print(factorial(5))
        


    
