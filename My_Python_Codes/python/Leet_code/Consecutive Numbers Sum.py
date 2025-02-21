
n=15
count,k=0,1
while 2*n>=k*(k+1):
    if (n-k*(k+1)/2)%k==0:
        count+=1
    k+=1
print(count)