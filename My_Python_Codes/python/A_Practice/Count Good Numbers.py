# Count Good Numbers
n=1
if (n%2==0):
    print(pow(20,int(n/2),1000000007))

else:
    n=n-1
    print(pow((5*pow(20,int(n/2),1000000007)),1,1000000007))