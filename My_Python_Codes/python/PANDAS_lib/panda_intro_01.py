import pandas as pd

# when data is given in column format
data=[[1,4,7],[2,5,8],[3,6,9]]
df_COL=pd.DataFrame({"A":data[0],"B":data[1],"C":data[2]},index=[1,2,3])  # if we do not specify index it will start from 0,1,2
# print(df_COL)
# OUTPUT 
#    A  B  C
# 1  1  2  3
# 2  4  5  6
# 3  7  8  9


# when data is given in Row format
df_row=pd.DataFrame(data,columns=["A","B","C"])
# print(df_row)
#OUTPUT
#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9

print(list(df_COL.shape))
