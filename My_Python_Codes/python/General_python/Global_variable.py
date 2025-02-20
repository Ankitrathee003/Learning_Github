# First let's try to access a global variable from the inside of a function,
# c = 1 
# def add():
#     print(c)
# add()   # Output: 1



# c = 1 
# def add():
#      # increment c by 2
#     c = c + 2
#     print(c)
# add()   #UnboundLocalError: local variable 'c' referenced before assignment


# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.
multiply=1
def multiply_nums(*args):
    for i in args:
        global multiply
        multiply*=i
    return(multiply)

# output 1
print(multiply_nums(2,4,1))
print(multiply)

#output 2
# print(multiply)
# print(multiply_nums(2,4,1))