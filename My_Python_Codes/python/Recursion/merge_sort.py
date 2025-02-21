import sys
sys.setrecursionlimit(5000)
def merge(a,b,d):
    i=0
    j=0
    while i<len(a) or j<len(b):
        if i==len(a) and j<len(b):
            for j in range(j,len(b)):
                d.append(b[j])
            return(d)
        elif j==len(b) and i<len(a):
            for i in range(i,len(a)):
                d.append(a[i])
            return(d)
        else:
            if a[i]<=b[j]:
                d.append(a[i])
                i+=1
            elif  a[i]>=b[j]:
                d.append(b[j])
                j+=1
    return d

e=[]










def merging(a,b,d):
    i,j,k=0,0,0

    while i<len(a) and j<len(b):
        if (a[i]<b[j]):
            d[k]=a[i]
            k=k+1
            i=i+1
        else:
            d[k]=b[j]
            k=k+1
            j=j+1
    while i<len(a):
            d[k]=a[i]
            k=k+1
            i=i+1
    while j<len(b):
            d[k]=b[j]
            k=k+1
            j=j+1
    return(d)




m=[2,6,3,1]
def merge_sort(d):
    if len(d)==0 or len(d)==1:
        return()
    mid=len(d)//2
    a=d[0:mid]
    b=d[mid:]
    merge_sort(a)

    merge_sort(b)
    
    merging(a,b,d)
merge_sort(m)
print(m)