import math

# from numpy import zeros
x=int(input("enter the no. you want to check for amstrong:  "))
y=x
z=x
count=1
while x>=9: 
        x= math.floor(x/10)
        count+=1
# print(count)
d=count
l=[]
i=0
if count==1:
    l.append(x)
else:
    while count>1:
        if i==0:
            l.append(math.floor((y)/(10**(count-1))))
            i+=1
            # print(f"in if {l}")
        else:
            y = y-l[i-1]*(10**(count-1))
            l.append(math.floor(y/(10**(count-2))))
            i+=1
            count-=1
            # print(f"in else {l}")
    # print(l)
# print((9*d))
sum=0
for k in range (d):
    sum+=(l[k])**d
if sum==z:
    print(f"{z} is a amstrong no.")
else:
    print(f"{z} is not a amstrong no.")




