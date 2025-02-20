#Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# def isHappy(n):
#     count=0
#     while count<100:
#         if n==4:
#             return(False)
#         elif  n!=1:
#             count+=1
#             print(n)
#             print(f'count is {count}') 
#             sum=0
#             while n>0:
#                 digit=n%10
#                 sum=sum+(digit)*(digit)
#                 n=n//10
#             n=sum
#         elif n==1:
#             return (True)

o=0

for i in range (1,1001):
    o+=i**10
print(o)
        

# # print(isHappy(195885415552254254))
# n=1232
# n=str(n)
# list=[int(n[i]) for i in range(len(n))]
# print(list)
# print(type(list))