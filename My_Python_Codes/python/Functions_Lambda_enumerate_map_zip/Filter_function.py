# Filter Function
# filter(function name, input)
def is_even(a):
        return(a%2==0)
n=[i for i in range(1,11)]

# evens=list(filter(is_even,n))
# print(evens)

# we can also use lambda expression
a=(lambda n: n%2==0)
evens=list(filter(a,n))  # function a will return true for even no.
print(evens)             # so only those n will be in list which are even


