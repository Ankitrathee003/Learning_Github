# if we want to find the no. occuring more than half the times of length of string.

a=[3,1,9,9,6,3,3,3]
i=0
majority_no=a[0]
count=0
def moores_algo(a,i,majority_no,count):
    while i<len(a):
        if majority_no!=a[i]:
            count-=1
            if i==len(a)-1:
                return(majority_no)
        else:
            count+=1
            i+=1
        if count==0:
            majority_no=a[i]
            count+=1
            i+=1
        else:
            i+=1
    return(majority_no)         # majority no. will be the probable occuring more than half of length otherwise none is satisfying the condition
x=moores_algo(a,i,majority_no,count)
counting=0
for i in range (len(a)):
    if x==a[i]:
        counting+=1
if counting>=len(a)/2:
    print(f"{majority_no} is occuring more than or equal to half of length of {a}")
else:
    print(f"NONE IS OCCURING MORE THAN OR EQUAL TO HALF OF LENGTH OF {a}")

