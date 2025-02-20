n=int(input("enter the no.  "))
def in_range(n):
    for i in range(1,n+1):
        yield i   # yield is keyword not function no need of parenthesis for i
print (in_range(n)) # it will not return anything gives generator object Location 

# generators are better option to save memory#
#as only one number will occupy memory one time when it is called#

# example:
numbers=in_range(11)  # generator# after generating we can use it once # sequence of no.
for i in numbers:
    print(i)

for i in numbers:
    print(i)  # it will not re print the no. as they have been used once in above loop

for i in in_range(11): #Now we can reprint as we are generating the numbers again instead of using already generated 
    print(i)


# memory (list)  -[................] # will take complete memory at a time
# memory (generator) -[.] will take only one memory unit at a time 



