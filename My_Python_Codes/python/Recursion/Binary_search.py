l=[2,4,6,8,9,12,24,34,36,56,68]
  ## iterative approach#   ##
def binary_search(l,a):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<a:
            # print(f'1   {mid}')
            low=mid+1
        elif l[mid]>a:
            # print(f'2   {mid}')
            high=mid-1
        else:
            # print(f'3   {mid}')
            return(mid)
# print(binary_search(l,24))



## binary search  using reccursion ##
def binary_rec(l,a,low,high):
    mid=(low+high)//2
    if len(l)==0:
        return('List is empty')
    elif l[mid]==a :
        return(mid)
    else:
        if l[mid]<a:
            low=mid+1
            # print(f'1  {mid}')
            return(binary_rec(l,a,low, high))
        elif l[mid]>a:
            high=mid-1
            # print(f'2  {mid}')
            return(binary_rec(l,a,low,high))
print(binary_rec(l,12,0,len(l)-1))



