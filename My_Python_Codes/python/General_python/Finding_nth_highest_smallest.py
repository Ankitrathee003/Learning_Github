l=[3,34,24,24,3,42,4,2443,3,422,3,23,3]
n=int(input("enter the nth value for which you want to find highest:  "))
def set(l): # making set from list
    a=[]
    for i in range (len(l)):
        if l[i] not in a:
            a.append(l[i])
    return(a)    
x=set(l)

  
def nth_highest(l): #finding  nth highest
    for i in range(len(l)):
        count=0
        for j in range(len(l)):
            if l[i]<l[j]:
                count+=1
        if count==n-1:
            print(f"{n}th highest is {l[i]}")
nth_highest(x)                   


 #finding  nth smallest
 
l=[3,34,24,24,3,42,4,2443,3,422,3,23,3]
n=int(input("enter the nth value for which you want to find smallest:  "))
def set(l): # making set from list
    a=[]
    for i in range (len(l)):
        if l[i] not in a:
            a.append(l[i])
    return(a)    
x=set(l)

  
def nth_smallest(l): #finding  nth smallest
    for i in range(len(l)):
        count=0
        for j in range(len(l)):
            if l[i]>l[j]:
                count+=1
        if count==((len(x)-n)):
            print(f"{n}th smallest is {l[i]}")
nth_smallest(x)                   



