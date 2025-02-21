# import math
# l=[]
# def is_prime (n):
#     for i in range(2,(math.floor(math.sqrt(n))+1)):
#         if n%i==0:
#             return
#     return(l.append(n))
# for i in range (2,100):
#     (is_prime (i))
# print(f"list of prime no.  {l}")



#

# def removeduplicate(nums):

#     i=1
#     while i<len(set(nums)):
#         if nums[0:i+1].count(nums[i])>1:
#             nums.append(nums.pop(i))
#         else:
#             i+=1
#     return(len(set(nums)),nums)
# print(removeduplicate(nums))
nums=[0,0,1,1,1,1,2,2,3,3,4]
# u=0
# for i in range (1,len(nums)):
#     if nums[u]==nums[i]:
#         continue
#     if nums[i]>nums[u]:
#         u+=1
#         nums[u] = nums[i]
# print(nums)

# nums=[0,0,1,1,1,1,2,2,3,3,4,4]
# u=0
# for i in range(len(nums)-1):
#     if nums[i]==nums[i+1]:
#         continue
#     else:
#         u+=1
#         nums[u]=nums[i+1]
# print(nums)





# def list_numbers_square(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+(digit)*(digit)
#         n=n//10
#     return(sum)



def isHappy(n):
    count=0
    while count<100:
        if n==145:
            return(False)
        elif  n!=1:
            count+=1
            print(n)
            print(f'count is {count}') 
            sum=0
            while n>0:
                digit=n%10
                sum=sum+(digit)*(digit)
                n=n//10
            n=sum
        elif n==1:
            return (True)
        

print(isHappy(19))

    


















