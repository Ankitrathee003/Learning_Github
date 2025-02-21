matrix = [[7],[9],[6]]
o=[]
Row=len(matrix)
Column=len(matrix[0])
def fun(matrix,o,Row,Column):
    count=0
    if Row==1:
        p=0
        while p <Column:
         o.append(matrix[0][p])
         p+=1

    else:
        while 2*count < Row :
                i=count
                while i<Column-count:
                    o.append(matrix[count][i])
                    i+=1

                j=count
                while j<Row-count-1:
                    o.append(matrix[j+1][Column-count-1])
                    j+=1

                k= (Column-count-1 if count==0 else Column-count-1)
                while k>count:
                    o.append(matrix[Row-count-1][k-1])
                    k-=1

                l=Row-count-1
                while l-1>count:
                    o.append(matrix[l-1][count])
                    l-=1
                count+=1
    return(o)

a=fun(matrix,o,Row,Column)
print(a)
