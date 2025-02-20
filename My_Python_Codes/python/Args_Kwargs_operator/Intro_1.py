#make flexible function
#     *operator
#     *Args



# we want to make a function which can take any no. of input all together
#Args operator gives output in set 
# we can use any keyword at place of args but acc. to convention we use args


def all_total(*args):
    total=0
    print(args)
    print(type(args))
    for i in args:
        total+=i
    return(total)
l=(1,2,3,4,5,6,7)  
# print(all_total(l))   #this print will work fine even without *args
# print(all_total(1,2,3,4,5,6,7,8,9,"t"))   # we have to use *args for this as no. of inputs are more than 1
                                            # otherwise error will be  all_total() takes 1 positional argument but 10 were given 



total=0
def ALL_TOTAL(*args):
    global total
    for i in args:
        total+=i
    return(total)
# print(ALL_TOTAL(1,2,3,4,5,6,7,8,9,10))    
# print(total,type(total))



# x=(1,2,3,4)
# print(type(x))


