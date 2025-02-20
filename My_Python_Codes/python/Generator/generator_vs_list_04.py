# list vs generator
# MEMORY USAGE
# when to use list, when to use generator


l=[i**0.5 for i in range(99999)] # it is taking very high memory 
# l=(i**0.5 for i in range(99999999)) # it will take les memory as at one time only one no. will be there




# import time
# t1=time.time()
# l=[i**2 for i in range(1000000)]
# t2=time.time()
# print(f"list time {t2-t1}")


# data we have to used again and again list is used
# where we have to use the elements once we can use generators



# t3=time.time()
l=(i**2 for i in range(10))
# t4=time.time()
# print(f"generator time is {t4-t3}")
