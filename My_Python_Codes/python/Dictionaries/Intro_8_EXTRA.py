# in get method if key not found it returns None 
# we can return anything not only None by overwriting
# user_info=dict(name='Ankit',age=34,fav_movies=('dangal','3idiot'))
user1={'name':'ankit','age':23,'age':34}
# print(user_info.get('names'))     # in get method if key not found it returns None 
# print(user_info.get('names','not found')) 



#  overwrite in dictionaries
# print(user1) #we can overwrite in dictionaries as age will be taken as 34.



#finding cubes and storing in dictionary
def Cube_finder(n):
    x={}
    for i in range (2,n+1):
        x[i]=i**3
    return(x)
print(Cube_finder(6))


#word counter
# d={'a':1,'h':2,'a':3}
# print(d)
def word_counter(s):
    x={}
    for i in s:
        x[i]=s.count(i)
    return(x)
print(word_counter("ankit_rathee")) #no need to take care that a is coming 2 times 
                                   # it will automatically overwrite



#taking input from user and printing in different lines
# o={}
# o['name']=input("enter your Name ")
# o['age']=input("enter your age")
# o['hobbies']=input(["enter your hobbies"]).split(",")
# print(o)
# for key,value in o.items():
    # print(f"{key}:{value}") 



