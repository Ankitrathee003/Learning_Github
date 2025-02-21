nums=[1,2,2,1,0,0,2,1,1,0]

l=[]
count=0
for i in nums:
    if i==0:
        l.insert(0,0)
        count+=1
    elif i==1:
        l.insert(count,1)
    else:
        l.append(2)
print(l)