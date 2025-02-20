l=[3,543,65,43,6543,25,5,343,4,4,4,43,65,3,2,10]
def greatest(l):
    a=[0]*len(l)
    for i in range (len(l)):
        count=0
        for j in range (len(l)):
            if l[i]<=l[j]:
                 count+=1
        if l[i] in a:                      #line 9 to 12 are for repeating elements 
            x = a.count(l[i])
            count-=x
        a[count-1]+=l[i]
    print(a)
greatest(l)


