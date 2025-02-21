nums=[1,2,3,9,8,6,4,10,7]
n=len(nums)
stack=[]
ans=[-1]*n
n-=1
for i in nums[::-1]:
    if not stack:
        stack.append(i)
        n-=1
        continue
    while stack:
        if i<stack[-1]:
            ans[n]=stack[-1]
            break
        stack.pop()
    stack.append(i)
    n-=1
print(ans)




    

