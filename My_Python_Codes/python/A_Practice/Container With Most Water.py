height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# Output: 49

n=len(height)-1 
l,r,area=0,n,0
while l<r:
    x=(min(height[l],height[r]))*(r-l)
    if x>area:
        area=x
    if height[l]>height[r]:
        r-=1
    else:
        l+=1
print(area)
