# doc string can be written using single triple quote or double triple quote 
# doc string helps to understand the code written by other users
def add(a,b):
    '''this function takes two arguments and return their sum'''
    return(a+b)
print(add.__doc__) # it will print doc string present in string

# max,len,min,sum,round
# print(max.__doc__)
# print(round.__doc__)
print(help(sum))