import sys
sys.setrecursionlimit(2000)  # exceed limit on factorial
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(170))  


# x = "awesome"
# def myfunc():
#   print("Python is "+x)

# myfunc()
