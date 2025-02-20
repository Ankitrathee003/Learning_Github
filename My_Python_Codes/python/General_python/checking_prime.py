import math as mt
# l=[]
# def is_prime (n):
#     for i in range(2,(mt.floor(mt.sqrt(n))+1)):
#         if n%i==0:
#             return
#     return(l.append(n))
# for i in range (2,1000):
#     (is_prime (i))
# print(f"list of prime no.  {l}")


def checkPrime(x):
        if any (x%i==0 for i in range (2,mt.floor(mt.sqrt(x)+1)) ):
            return False
        else:
            return True
# print(checkPrime(2))
# print ([i for i in range(2,mt.floor(mt.sqrt(2)+1))])

l=[i for i in range(2,1500000) if i%2!=0 and 1%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0]
print(len(l))
