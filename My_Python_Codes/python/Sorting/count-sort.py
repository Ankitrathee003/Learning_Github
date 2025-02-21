def count_sort(nums):
    # finding max in array
    i=0
    max=nums[0]
    while i<(len(nums)):
        if max>=nums[i]:
            i+=1
        else:
            max=nums[i]
            i+=1
 
    count_array=[0]*(max+1)  # initialising the count array with zeroes and size = 1+maximum number in nums

    for i in nums:
        count_array[i]+=1   # filling the counting array with frequency of numbers (at index same as number(i) in nums)


    j=0   #initialising for traversing count-array
    i=0   #initialising for overwriting nums
    while j<len(count_array):
        if count_array[j]==0:
            j+=1
        else:
            nums[i]=j
            i+=1
            count_array[j]-=1
    return(nums)
nums=[9,5,3,3,4,1,2,87,47,87,9,3,4]
print(count_sort(nums))




    

