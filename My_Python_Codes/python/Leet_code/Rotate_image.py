
# The issue in your code is with the line m = matrix. 
# In Python, when you assign a list to a new variable, 
# you are actually creating a reference to the original list, not a new copy.
# As a result, any modifications made to m 
# will also affect the original matrix since they both refer to the same underlying list.

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# n=len(matrix[0])
# m=matrix
# for i in range (n):
#     for j in range (n):
#         m[j][n-i-1]=matrix[i][j]
# print(m)




# to come out of it we will create a copy of matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix[0])
# m = [row[:] for row in matrix]     # to come out of it we will create a copy of matrix
# for i in range (n):
#     for j in range (n):
#         matrix[j][n-i-1]=m[i][j]
# print(matrix)
# for i in matrix:
#     print(i)



