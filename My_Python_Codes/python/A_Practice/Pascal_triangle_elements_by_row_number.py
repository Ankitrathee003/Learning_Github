# #using Recursion

# def rec(rowIndex):
#         if rowIndex == 0:
#             return [1]
#         a = rec(rowIndex-1)
#         b = [1]
#         for i in range(1,rowIndex):
#             # print(rowIndex)
#             b.append(a[i-1] + a[i])
#         b.append(1) 
#         return b
# # print(rec(6))



# # using comb function
# import math
# rowindex=9
# l=[]
# for i in range(rowindex+1):
#     l.append(math.comb(rowindex,i))
# print(l)


print(ord("{"))