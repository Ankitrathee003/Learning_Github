# l=[1,2,3,4,5,6]
# l[0],l[2]=l[2],l[0]  # to swap we  will have to write command in a same line 
# print(l)

def partition(a,si,ei):
    pivot=a[si]        # we will take pivot to be first element of our list.
                      
    c=0
    for i in range(si,ei):  # find no. of elements (count) smaller than pivot
        if pivot > a[i]:
            c=c+1       
    a[si+c],a[si]=a[si],a[si+c]   # will swap the first element so that it can reach to exact position or final position of a[si] 
    pivot_index=si+c

    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1   # will shift left pointer right by one if element is already smaller
        elif a[j]>pivot:
            j=j-1    # will shift right pointer left by one if element is already greater
        else:
            a[i],a[j]=a[j],a[i]  # will swap the elements whenever we find the elements on both side not satisfying the condition.
            i=i+1
            j=j-1
    return(pivot_index)



def quick_sort(a,si,ei):
    if si==ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index)
    quick_sort(a,pivot_index+1,ei)

a=[99,33,23,8,7,56,2,33]
quick_sort(a,0,len(a)-1)
print(a)