# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

 

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3


# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


# Example 3:
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.



import math as mt
def is_prime(n):
    l=int(n/2)
    if n%2==0:
       n+=1
       is_prime(n)
      
    else:
        i=3
        while i<l:
            if n%i==0:
                n+=1
                is_prime(n)
            else:
                i+=2
    return(n)
print(is_prime(45))    
  

# def next_prime(n):
#     if n%2==0:
#        return(False)
#     else:
#         i=3
#         while i<l:
#             if n%i==0:
#                 return(False)
#             else:
#                 i+=2
#         return(True)

# print(is_prime(97))         








def isUgly(n):
    def is_prime(n):
        l=int(mt.sqrt(n))
        if n%2==0  or n==1 or n==3 or n==5:
         return(False)
        else:
            i=3
            while i<l:
                if n%i==0:
                    return(False)
                else:
                    i+=2
            return(True)

    if n<=0 or is_prime(n):
        return(False)
    else:
        i=7
        while i<=n/2:
            if n%i==0 and is_prime(i):
                return(False)
            else:
                i+=2
        return(True)
# print(isUgly(9))