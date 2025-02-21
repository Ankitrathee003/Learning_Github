n = 5
k = 2
l=[i for i in range(1,n+1)]
s=0
def remove_one_element(l,k,s):
    if len(l)==1:
        return int(l[0])
    else:
        a=(s+k-1)%len(l)
        l.pop(a)
        s=a 
        return remove_one_element(l,k,s)
print(remove_one_element(l,k,s))

