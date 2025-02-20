def trap(height):


    left=[height[0]]
    # creating an array having all elements graeater than or equal to it from left
    for i in height[1:]:
        if i <=left[-1]:
            left.append(left[-1])
        else:
            left.append(i)
    print(left)
    
    # creating an array having all elements graeater than or equal to it from right
    right=[height[-1]]
    for j in height[-2::-1]:
        if j<= right[0]:
            right.insert(0,right[0])
        else:
            right.insert(0,j)
    print(right)


    n=len(height)
    area=0
    for k in range (1,n-1):
        area+=(min(left[k],right[k])-height[k])
    return(area)
height=[0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))
print(height)
