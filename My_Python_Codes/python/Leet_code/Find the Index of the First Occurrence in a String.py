# # Find the Index of the First Occurrence in a String
# haystack = "mississippi"
# needle = "issip"




class Solution:   # best solution from Leeet code
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        return haystack.index(needle) if needle in haystack else -1  # will return first index from haystack
    




# h=len(haystack)
# n=len(needle)
# if n<=h:    
#     def find_start(haystack,needle,i):
#         while i < =h-n:
#             if haystack[i]==needle[0]:
#                 print(f'just {i}')
#                 i+=1
#                 break
#             else:
#                 i+=1
#         return(i-1)

# def checker(i):
#     if all (  (haystack[j]==needle[j-i])   for j in range (i,i+n) if j<h) :
#             return(f"hey i am  a {i}") 
    
# i=0
# while  (i<h):
#     x=find_start(haystack,needle,i)
#     print(checker(x))
#     i=x+1
# print(f"hey i am b {i}")








# # class Solution:
# #     def strStr(self, haystack: str, needle: str) -> int:
# #         h=len(haystack)
# #         n=len(needle)
# #         if n<=h:
# #             i=0
# #             def find_start(haystack,needle,i):
# #                 while i < h:
# #                     if haystack[i]==needle[0]:
# #                         return(i)
# #                     else:
# #                         i+=1
# #                 i=(i-1)
# #             Solution.find_start(haystack,needle,i)
# #             if all (  (haystack[j]==needle[j-i])   for j in range (i,i+n)) :
# #                     return(i) 
# #             elif i+1<h:
# #                 find_start(haystack,needle,i+1)
# #             else:
# #                 return(-1)
            
# #         return(-1)
    
# # why=Solution()  
# # x=(why.strStr("abcd","cd"))
# # print(x)


a="hello s"
b='e'
print(a.index(b))