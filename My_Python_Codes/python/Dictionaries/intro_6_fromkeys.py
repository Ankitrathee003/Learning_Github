d={'name':'unknown','age':'unknown'}
# fromkeys
#if we want to have the same values of keys 
# d=dict.fromkeys(('name','age','height'),'unknown')
# print(d)

d1=dict.fromkeys("abc",'unknown') # all abc will be new keys
# print(d1)0
l=[i for i in range(9)]
d2=dict.fromkeys([j for j in l],0)
print(d2)


# d3=dict.fromkeys(['name','age'],('unknown','nhi_pata'))
# print(d3)       # output   {'name': ['unknown', 'nhi_pata'], 'age': ['unknown', 'nhi_pata']}


#get method()

user_info=dict(name='Ankit',age=34,fav_movies=('dangal','3idiot'))
# print(user_info['hobbies'])    # will return error as 
# print(user_info.get('hobbies'))  #to get rid of above error we use get it returns none

# if user_info.get('name'):
#     print("Present")
# else:
#     print("Absent")



# user_info.clear()
# print(user_info)


# Here x and user_info are same dictionaries
# we can use copy method so that we can work on them seprately


x=user_info
# print(x)
# x.clear()
# print(x)
# print(user_info)
# print(x is user_info)  # returns True means same dictionaries



s=user_info.copy()
# print(user_info is s) # returns False means same dictionaries





