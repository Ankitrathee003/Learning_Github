# Time complexity to calculate fib(n) is O(2^n)
# In simple recursion we will be calculating subproblems again and again
# Using DP we want to overcome this repetating subproblems calculation by taking some space
## DP is used in overlapping subproblems as those subproblems value can be stored somewhere
## So this subproblems value storing idea will save time and the fibbnocci calculation case time complexity will reduce in liner

# def fibb(n):
#     if n==0 or n==1:
#         return n
#     ans1=fibb(n-1)
#     ans2=fibb(n-2)
#     myans=ans1+ans2
#     return myans
# print(fibb(6))                                             # 0,1,1,2,3,5,8
    

### MEMOIZATION  ###  ### TOP DOWN ##

#                         fib(5)
#                     /A/          \*J
#                    /A/            \
#               fib(4)               fib(3)
#              /B/     \               /      \ 
#        fib(3)      *I fib(2)     fib(2)       fib(1)
#     /C/  |H         /    \         /    \         
# fib(2)  *G.fib(1) fib(1)  fib(0) fib(1) fib(0)   
# /D/   \F
#fib*(1)-E->fib(0)      
# Recursion will follow the shown ABCDEFG_____ path
# Note that calculations of step G are directly taken from Table than calulation of I is directly taken and then value of J is taken
# This saves our time of travelling at each Node just by saving the number in dict So it is Called MEMOISATION ##TOP DOWN ##




### WHEN WE ARE STORING THE VALUES THIS IS CALLED MEMOIZATION ###
fib_dict = {}
def fibonacci(n):
    # Check if the value is already cached
    if n in fib_dict:
        print(f"I helped by providing value of of fib_dict[{n}] directly from dict]")
        return fib_dict[n]
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        result = n
    else:
        # Recursive case: Calculate Fibonacci for n
        result = fibonacci(n - 1)+fibonacci(n - 2)
    # Cache the result and return it
    print(f"result of fib_dict[{n}] is stored")
    fib_dict[n] = result
    return result
# Test the function
n = 5  # Change this value to the desired Fibonacci number you want to calculate
# print(f"Fibonacci({n}) =", fibonacci(n))






# Tabulation Solution [Bottom UP]
# Bottom Up means we will start from solving fib(0),fib(1),fib(2)----
def fibb_Tabulation(n):
    fib_Table=[0,1] ## Here we need not to search so can make List also
    for i in range (2,n+1):
        fib_Table.append(fib_Table[i-1]+fib_Table[i-2])
    return fib_Table[n]
print(fibb_Tabulation(10))


## WE Need not make complete list we can just keep store the previous value
def fib(n):
    a,b=0,1
    for i in range (n):
        temp=a
        a=b
        b+=temp
        ##OR##
        # a,b=b,a+b
    return a
print(fib(10))
