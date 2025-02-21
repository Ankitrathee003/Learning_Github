def evens(n):
    for i in range (2,n+1,2): 
            yield i
for i in evens(8):
    print(i)