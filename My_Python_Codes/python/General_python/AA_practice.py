
# n=len(l)  
# output=0
# for i in range (n):
#     for j in range(i+1,n):
#         x=(min(l[i],l[j]))*(j-i)
#         if x>output:
#             output=x
# print(output)
# 

# height = [4,2,3]
# for i in height:
#     if i!=0:
#         i=(height.index(i))
#         break
# x=-1
# while x>-(len(height)):
#     if height[x-1]>=height[x]:
#         x-=1
#         continue
#     else:
#         break
# x=x+(len(height))

    
# area=0 
# j=i+1

# while j<=x:
#         if height[j]>=height[i]:
#             area+=height[i]*(j-i-1)-sum(height[i+1:j])
#             i=j
#             j+=1
#         else:
#             j+=1
#             if j==len(height):
#                 i+=1
#                 j=i+1
# print(area,i,j-1)  
# print(x,len(height))  


rows = int(input("Enter the number of rows: "))

for i in range(rows+1):
  n=int(rows-i)
  print  (' '*n, '# '*(i+1), ' '*n) 
i=0
while i <rows:
  print  (' '*(i+1), '# '*(rows-i), ' '*(i+1))
  i+=1

  
  

        


    


