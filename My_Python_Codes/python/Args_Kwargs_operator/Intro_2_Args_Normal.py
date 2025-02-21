# Args as a parmeter
# while defining a function we input a parameter
# while calling a function we give input to function as argument
multiply=1
def multiply_nums(*args):
    for i in args:
        global multiply
        multiply*=i
    return(multiply)
# print(multiply_nums(2,4,1))
# print(multiply_nums([2,4,1])) #we are giving input as a list it will remain packed 
print(multiply_nums((2,4,1)))  #we are giving input as a tuple it will remain packed
# print(multiply_nums(*[2,4,1]))    #by using * list will be unpaced


#
multiply=1
def multiply_nums(a,*args):
    for i in args:
        global multiply
        multiply*=i
    print(a,args,multiply)
    return(a,*args,multiply)  # here args will unpack 
# print(multiply_nums(10,2,6,1)) # 10 will not be taken as args being first element it will go to the a 


