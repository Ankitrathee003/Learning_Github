multiply=1
def multiply_nums(*args):
    for i in args:
        global multiply
        multiply*=i
    return(multiply)
# print(multiply_nums(*[2,5,1]))    #by using * list will be unpaced it is called args as argument
# l=[2,3,4]
# print(multiply_nums(l))  # it will appear 10 times( 2*5*1) 
                        # as before that multiply value was 10 and we are initialising multiply value outside the function

#
l=[]
def power_fun(a,*args):
    for i in args:
        l.append(i**a)
    return(l)


# print(power_fun(2,3,4,5))
# x=2
# a=(1,2,3,4,5)
# z=[x**i  if a else print("list is empty") for i in a ]
# print(z)


# To check list is empty or not
# l=[]
# if l :
#     print("non empty")
# else:
#     print("empty")


# Not Working

# def to_power(nums,*args):
#     if args:
#         return(i**nums for i in args)
#     else:
#         return('list is empty')
# s=[1,2,3]       
# print(to_power(2,*s))



