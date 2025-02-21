# Product of Array Except Self
nums=[1,2,3,4]
# def productExceptSelf(nums): # Not completed

l=[]
i=0
n=len(nums)
while i< n-1:
    x=nums.pop(0)
    nums.append(x)
    temp=nums[:]
    l.append(temp)
    # print(l)
    i+=1
print(l)

x=nums
x[2]=243

# print(x,nums)