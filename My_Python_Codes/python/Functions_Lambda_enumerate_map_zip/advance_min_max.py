n=[1,2,3,48]
# print(max(n),min(n))

### max(input,key=function name)##
### max(input,key=lambda input:function)##
name=['Ankit','Rathee','Abhinav','jain']
# print(max (name))
# print(max(len(name[i]) for i in range(len(name))))
def func(j):
    return(len(j))
# print(max(name,key=func))
# print(max(name,key=lambda name:len(name) )) # give complete list name in input 
                                            # lambda function will automatically take one by one


students=[
    {'name':'harshit','score':38,'age':24},
    {'name':'Ankit','score':25,'age':23},
    {'name':'Rathee','score':98,'age':18}
]


# print(max(students, key=lambda students:students['score']))
# print(max(students, key=lambda i:i['score'])['age']) # we want to return only age of highest scorer


#
student2={
    'Harshit':{'score':90,'age':24},
    'Mohit':{'score':75,'age':30},
    'Rohit':{'score':90,'age':45}
    }
print(max(student2,key=lambda i:student2[i]['score']))
print(student2['Harshit'])