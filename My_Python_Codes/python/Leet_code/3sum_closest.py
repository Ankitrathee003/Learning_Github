nums = [-1,0,1,2,-1,-4]

nums=sorted(nums)
n=len(nums)
l=[]
s=0
e=n-1
while s<(n-2):
    m=s+1
    e=n-s-1
    while m<n:
        if m<e:
            t=nums[s]+nums[m]
            if -t < nums[e]:
                e-=1
            elif -t>nums[e]:
                m+=1
            else:
                l.append((nums[s],nums[m],-t))
                m+=1
                e-=1
        else:
            break
    s+=1
print(l)