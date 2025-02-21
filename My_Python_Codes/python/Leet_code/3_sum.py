nums = [-1,0,1,2,-1,-4]
# n=len(nums)
# l=[]
# s=set()
# i=0
# while i<n:
#     j=i+1
#     while j<n:
#         k=j+1
#         while k<n:
#             if nums[i]+nums[j]+nums[k]==0:
#                 # l.append([nums[i],nums[j],nums[k]])
#                 x=(nums[i],nums[j],nums[k])
#                 x=tuple(sorted(x))
#                 s.add(x) 
#                 break           
#             else:
#                 k+=1
#         j+=1
#     i+=1

# l=[]
# nums.sort()
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range (j+1,len(nums)):
#             if nums[i]+nums[j]+nums[k]==0:
#                 l.append((nums[i],nums[j],nums[k]))
# print(type(set(l)))
# print(set(l))


# z=[]
# for i in list(s):
#     z.append(list(i))
# print(z)
