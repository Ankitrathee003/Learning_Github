# n=["as","you"]
# m=[]
# for i in range(len(n)):
#     m.append(n.pop())
# print(m)
# m=n.pop(20)
# print(n)
strings=['himmat','harsh','dipankur','nitin','ajay']
def rev_item(x):
    new_str=[]
    for i in range(len(x)):
        # x[i]= x[i][::-1]
        new_str.append(x[i][::-1])
    return new_str
print(rev_item(strings))


