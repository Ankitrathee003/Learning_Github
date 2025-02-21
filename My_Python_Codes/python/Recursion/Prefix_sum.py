# using two arrays

nums1=[1,2,3,4,5]
def prefixSum(nums1,nums2,sum=0,i=0):
    if len(nums1)==len(nums2):
        return nums2
    sum+=nums1[i]
    nums2.append(sum)
    x=prefixSum(nums1,nums2,sum,i+1)    # if we simply call the function here by prefixSum(nums1,nums2,sum,i+1) than it will return None because we are calling the function recursively so in stack there are 5 functions left return nums2 will work for lasrt but for other 4 we are not returning anything
    return x

# print(prefixSum(nums1,nums2=[]))



# using same array
nums1=[1,2,3,4,5]
def prefixSum(nums1,sum=0,i=0):
    if i==len(nums1):
        return nums1
    sum+=nums1[i]
    nums1[i]=sum
    x=prefixSum(nums1,sum,i+1)
    return x

print(prefixSum(nums1))
