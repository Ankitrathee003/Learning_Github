nums=[2,9,8,7,20]
f=previous=nums[0]
s=float("inf")
for i in nums:
    if i<=f:
        f=i
    elif i<=s:
        s=i
    else:
        print(f,s,i,True)
print("i am outside the loop")