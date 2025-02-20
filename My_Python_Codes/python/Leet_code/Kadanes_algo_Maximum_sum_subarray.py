# key concept is that we will not carry the negative sum ahead
# return the array with max sum
# given that sum will not be less than zero if less than zero return 0
# if in case max sum is negative if all are negative  it will fail return 0 instead of that negative sum
nums=[-2,1,-3,4,-1,2,1,-5,4]
# maxsum=0
# sum=0
# l=[]
# for i in range(len(nums)):
#     if sum==0:
#         start=i
#     sum+=nums[i]
#     if sum>maxsum:
#         maxsum=sum
#         end=i   # end is updating continuously as long as sum is increaing
#     if sum<0:   # we are not taking the condition sum=0 as if in case max sum=0 we will not able to return the array
#         sum=0
# print(maxsum)
# print(nums[start:end+1])


## this code also work on same logic here we will able to return even negatives sum for this we need to track for all sums instead of deciding maxsum at each iteration

nums=[-2,1,-3,4,-1,2,1,-5,4]
maxsum=0
sum=0
l=[]
for i in range(len(nums)):
    sum+=nums[i]
    l.append(sum)
    if sum<0:    
        sum=0

print(max(l))





          ##SIMILAR###
# for i in range(1, len(nums)):
#         if nums[i-1] > 0:
#             nums[i] += nums[i-1]
# print(nums)
# print(max(nums))
