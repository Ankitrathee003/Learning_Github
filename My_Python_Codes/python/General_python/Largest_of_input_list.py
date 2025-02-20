l=[]
n=int(input("enter the no. of elements: "))
for i in range (n):
    i=int(input(f"enter the {i+1} th element  "))
    l.append(i)
print(l) 
def largest (l):
    # while i<n-1:
    for i in range (n-1):
        if l[0]<l[i+1]:
            l[0]=l[i+1]
            # i+=1
        # else:
            # i+=1      
    print(f"largest of input list is {l[0]}")
largest(l)