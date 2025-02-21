import sys
sys.setrecursionlimit(20000)
# def reverse_sum(n):
#     if n==1:
#         return(0)
#     else:
#         return(1/n+reverse_sum(n-1))
# print(reverse_sum(4))




#  EULER NUmber
def reverse_factorial_sum(n):
    if n==0:
        return(1)
    else:
        return(1/n*reverse_factorial_sum(n-1))
sum=0
for i in range (1000):
    sum+=reverse_factorial_sum(i)
print(sum)