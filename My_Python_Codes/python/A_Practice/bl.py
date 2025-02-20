# # s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # def convert(s, numRows):
# #     if numRows == 1 or numRows >= len(s):
# #         return s

# #     result = [''] * numRows
# #     index= 0
# #     step=1
# #     for char in s:
# #         result[index] += char
# #         if (step==1 and index<numRows-1) or (step==-1 and index=nbh):
# #             result[index]+=" "*(numRows-index-2)
# #         else:
# #             result[index]+=" "*(index-1)
# #         if index ==nbh:
# #             step = 1
# #         elif index == numRows - 1:
# #             step = -1
# #         index += step

# #     return result
# # # print(convert(s,6))
# # for i in (convert(s,6)):
# #     # print(type(convert(s,6)))
# #     print(i)


# # a=["abcd"]*5
# # print('123'.join(a))

# # def name(fname,lname):
# #     return(fname+""+lname)

# # print(name("Ankit","Rathee"))

# # x=(lambda x,y:x**y*x)(3,2)
# # print(x)

# # str="123"
# # str+="4"*5
# # print(str)

# # l=[1,2,3,4,5]
# # numnbh
# # for count,i in enumerate(l[::-1]):
# #     num+=i*(10**(count))
   
# # # print(num)
# # b=[1,2,4,5]
# # # print("".join(map(str,b)))
# # b_int = int("".join(map(str, b)))
# # # print(b_int)
# # import math
# # # print(math.ceil(9/2))


# # s = "axc"
# # t = "ahbgdc"
# # def isSubsequence(s ,t) :
# #     jnbh
# #     inbh
# #     m=len(s)
# #     n=len(t)
# #     while i< len(s):
# #         while j<n:
# #             if s[i]==t[j]:
# #                 print(j,i)  
# #                 j+=1
# #                 i+=1
# #                 break
# #             else:
# #                 j+=1
# #         if j==n and i<m:
# #             return False
# #     return True
# # print(isSubsequence(s,t))

# # s='hello'
# # s[1],s[2]=s[2],s[1]
# # print(s+"ans")

# # for i in range(-6,-1,2):
# #     print(i)
# # l=[i for i in range(11)]
# # print(l.pop(),l.pop())

# # left=7
# # if left:
# #     print(0)


# # mult2=1
# # max2=float("-inf")
# # nums=[0,2,3,5,6,7]
# # n=len(nums)
# # for j in range(n-1,-1):
# #     print(j)
# #     mult2*=nums[j]
# #     max2=max(max2,mult2)
# # print(max2)

# # n=int(input())
# # while n>-1:
# #     if n==1:
# #         print("ODD") 
# #     if n==0:
# #         print("EVEN")
# #     n-=2

# def mod(l):
#     l=[1,2,3,4]
# l=[9,10,11]
# mod(l)
# # print(l)



# def mod(l):
#     # Modify the original list 'l' by adding elements
#     l+=[1, 2, 3, 4]

# l = [9, 10]
# # mod(l)
# # print(l)  # This will print [9, 10, 1, 2, 3, 4]


# # def Factorial(n):
# #     dp=[1]*(n+1)
# #     for i in range(1,n+1):
# #         dp[i]=i*dp[i-1]
# #     return dp[n]
# # print(Factorial(6))

# mat=[[1,2,3],[4,5,6]]
# r=[7,8,9]
# for row in mat:
#     r = {m + n for m in row for n in r}
# print(r)


# def flipBit(N,M,mat,x,y):
#     if mat[x-1][y-1]=='B':
#         mat[x-1][y-1]='R'
#     else:
#         mat[x-1][y-1]='B'
#     return mat

# arr=[2,54,11,65,98,1,3]
# arrpos = [*enumerate(arr)] 
# print(arrpos)

# text = "Alice and Bob are friends" 
# print(text.split())
 # import nltk

# from nltk.tokenize import word_tokenize from nltk.util import ngrams

# text = "I love to play UNO."

# tokens = word_tokenize(text.lower())

# bigrams = list(ngrams (tokens, 2))

# print(bigrams)
# def transform_string(input_str):
#     output_str = ''
#     for char in input_str:
#         if char.isalpha():
#             current_char = char
#         else:
#             output_str += ''.join([chr(ord(current_char) + i) for i in range(int(char))])
#     return output_str
# sample_input_1 = "A3G4B2"
# sample_output_1 = transform_string(sample_input_1)
# print(f"Sample Input 1: {sample_input_1}")
# print(f"Sample Output 1: {sample_output_1}")

# sample_input_2 = "A3X4Z3"
# sample_output_2 = transform_string(sample_input_2)
# print(f"Sample Input 2: {sample_input_2}")
# print(f"Sample Output 2: {sample_output_2}")

# def transform_string(input_str):
#     result = ''
#     i = 0

#     while i < len(input_str):
#         char = input_str[i]

#         if char.isalpha():
#             result += char
#             i += 1
#         else:
#             num = int(input_str[i])
#             result += chr(ord(char) + num)
#             i += 2

#     return result

# # Sample Input 1
# input_str_1 = "A3G4B2"
# output_str_1 = transform_string(input_str_1)
# print(output_str_1)

# def transform_string(input_str):
#     result = ''
#     i = 0

#     while i < len(input_str):
#         char = input_str[i]

#         if char.isalpha():
#             result += char
#             i += 1
#         else:
#             num = int(input_str[i])
#             result += chr(ord('A') + num - 1)
#             i += 2

#     return result

# # Sample Input 1
# input_str_1 = "A3G4B2"
# output_str_1 = transform_string(input_str_1)
# print(output_str_1)

# abc=1,000,000
# # a b c = 1000 2000 3000
# a,b,c=1000,2000,3000
# a_b_c=1,000,000

# print(abc,a,b,c,a_b_c)


# l=[1,2,3].reverse()
# print(l)
# i=1
# j=1

# for i in range(1,11):
#     if i%3!=0:
#         j+=2
#         continue
#     if j%3==0:
#         break
# print(i+j)

# n=10
# for i in range(10):
#     print(' '*(n-i-1),'* '*(i))
# d={'t': 1, 'r': 1, 'e': 2}


# N=12
# dp = [float('inf')] * (N +1)
# squares=[1,4,9,16,25]
# dp[0]=0
# for i in range(1, N + 1):
#     # Compute the minimum coefficients for the current number
#     for square in squares:
#         if square <= i:
#             dp[i] = min(dp[i], dp[i - square] + 1)
#         print("outer",dp)

# # Return the minimum coefficients for N
# print(dp)

# s="ABCD"
# print(s[0:3])


# def count (child_dict, i):
#     if i not in child_dict.keys():

#         return 1

#     ans = 1

#     for j in child_dict[i]:

#         ans += count (child_dict, j)

#     return ans

# child_dict =dict()

# child_dict[0] = [1,2]

# child_dict[1] = [3,4,5] 
# child_dict[2] = [6,7,8]

# print (count (child_dict, 0))
    
    
nums=[1,2,34,4]
from collections import Counter
arr=Counter(nums)
print(arr[1])
