# l='augumentedreality'
# print(('hello everyone' +" "*3 +'Ankit'  ))
# n=5
# i=0
# # while i<n:
#     if (n-1)!=i:
#         print(f'{l[i]}'  + " "*(n-i) +  f'{l[i+2*n-2*(i+1)]}')  
#         i+=1
#     else:
#          print(f'{l[i]}')
#          i+=1 

nums=[82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,-29393,-64727,-14778,32075,-63412,-40524,86440,-2707,-36821,63850]
print(len(nums))
l=[]
for i in range(len(nums)) :
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if i!=j and i!=k and j!=k:
                        if -nums[i]==nums[j]+nums[k]:
                            x=[nums[i],nums[j],nums[k]]
                            x=sorted(x)
                            if x not in l:
                                l.append(x )
print(l)