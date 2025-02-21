y=[0,2,1,3,-1,0,-1,-2,-3,-1,-4,2,-5]
n=len(y)
c=0
i=0
while i<n-2-c:
    if y[i]<y[i+1]<y[i+2] or y[i]>y[i+1]>y[i+2]:
        y.pop(i+1)
        c+=1
        i-=1
    i+=1
    print(y)
n=len(y)
arr=[[y[i],y[i+1]] for i in range(n-1)]
print(arr)
# ans=0
r=0
def helper(a,b):
    a.sort()
    b.sort()
    if a[0]>

for i in range(len(arr)-1):
    ans=0
    start=arr[i][0]
    end=arr[i][1]
    # if start>end:
    #     start,end=end,start
    for j in range (i+1,len(arr)):
        if start<end:
            if arr[j][1]<=end and arr[j][1]>=start:
                start=arr[j][1]
                ans+=1
            elif arr[j][1]<=end and arr[j][1]<=start:
                ans+=1
        elif start>end:
            if arr[j][1]>=end and arr[j][1]<=start:
                end=arr[j][1]
                ans+=1
            elif arr[j][1]>=end and arr[j][1]>=start:
                ans+=1


    print([i,ans,[start,end]])
    r=max(r,ans)
print(r)
    
        

















# def max_intersections(Y):
# 	p,i=[],0
# 	while i<len(Y)-1:
# 		k=[Y[i],Y[i+1]]
# 		k.sort()
# 		p.append(k)
# 		i+=1
# 	Y=p
# 	print(Y)
# 	n=len(Y) 
# 	mp = {}
# 	# Iterate through each line and update the dictionary accordingly
# 	for line in Y:
# 		a = line[0]
# 		b = line[1]
# 		mp[a] = mp.get(a, 0) + 1
# 		mp[b + 1] = mp.get(b + 1, 0) - 1

# 	# Initialize with minimum value of integer
# 	res = float('-inf')
# 	sum_ = 0

# 	# Iterate through the dictionary and update the sum and 
# 	# maximum accordingly
# 	for key, value in sorted(mp.items()):
# 		sum_ += value
# 		res = max(res, sum_)

# 	# Return the maximum number of intersections
# 	return res
       


# def solution(Y):
#     # Implement your solution here
#     mean = sum(Y)/len(Y)
#     count = 0
    
#     for i in range(1,len(Y)):
#         if Y[i-1] <= mean and Y[i] >= mean:
#             count+=1
#         elif Y[i-1] >= mean and Y[i] <= mean:
#             count+=1
#     # if count == 8:
#     #     return 5    
#     return count


