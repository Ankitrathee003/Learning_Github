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




m=[2,6,3,1,15]
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


 ####
# Working of above code

# 0.merge_sort(a)  is called with a*=[2,6]   (remaining lines are in stack:   1.merge_sort(b)   2.merging(a,b,d)   till it returns)
            #   merge sort(a) is called with a=[2] being single element it returns() control goes to next line
                    # return()
            #   merge sort(b) is called with b=[6] being single element it returns() control goes to next line
                    # return()
            #   merging(a,b,d) is called with a=[2] ,b=[6], d (same as a*)=[2,6] it returns( sorted array d=[2,6])
                    # return(d) d=[2,6]

# 1.merge sort(b)  is called with b=[3,1,15] (with   3.merging(a,b,d)   in stack   d=[3,1,15] d will be what it was before breaking into a,b)
            #   merge sort(a) is called with a=[3] being single element it returns() control goes to next line
                    # return()
            #   merge sort(b) is called with b=[1,15] (  4.merging(a,b,d)   in stackith d=[1,15] )
                        #   merge sort(a) is called with a=[1] being single element it returns() control goes to next line
                                  # return()
                        #   merge sort(b) is called with b=[15] being single element it returns() control goes to next line
                                  # return()
                        #   4.merging (a,b,d) is called with a=[1] b=[15]  d=[1,15]
                                  # returns(d)  with d=[1,15]
            #   3.merging(a,b,d) with a=[3]   (b=[1,15] which was returned by 4.merging (a,b,d) to merge sort(b))    d=[3,1,15] 
                    #  returns(d)  d=[1,3,15]
# 2.merging(a,b,d) is called with a =[2,6] (returns from 0.merge_sort(a)) b=[1,3,15] returns from (1.merge sort(b)) with d=[2,6,3,1,15]
            # return(d) d=[1,2,3,6,15]
            

                        
