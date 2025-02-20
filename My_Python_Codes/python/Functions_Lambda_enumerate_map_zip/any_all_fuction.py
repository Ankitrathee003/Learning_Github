N1=[2,3,5]
N2=[1,3,5,7,9]

evens1=[]
for x in N1:
    evens1.append(x%2==0)
# print(evens1)

evens2=[i%2==0 for i in N1]
# print(evens2,type(evens2))


# print(all([True, True, True, True, True]))
# print(all([i%2==0 for i in N1]))

# Above function wil return single TRUE if all are True 
# even one False will result in False
# print(any([i%2==0 for i in N1]))
# any function will give True even if one True is present. 


# use of all function to filter data types
def sum(*args):
    total=0
    if(all(type(i)==int or type(i)==float for i in args)):
        for i in args:
            total+=i
        return(total)
    else:
        return('wrong input')
print(sum(1,2,3,4,5,9)) 