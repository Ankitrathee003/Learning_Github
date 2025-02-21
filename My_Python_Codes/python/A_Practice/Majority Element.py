# Majority Element
nums=[2,2,1,1,1,2,2]
sum,i=1,1
candidate=nums[0]
while i < (len(nums)):
    if (nums[i]==candidate): 
        sum+=1
        i+=1
    else:
        sum-=1
        if sum==0:
            candidate=nums[i]
            sum=1
            i+=1
        else:
            i+=1
print(candidate)
print(sum)

