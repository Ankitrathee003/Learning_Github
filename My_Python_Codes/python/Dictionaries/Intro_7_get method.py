#get method()

user_info=dict(name='Ankit',age=34,fav_movies=('dangal','3idiot'))
# print(user_info['hobbies'])    # will return error as 
# print(user_info.get('hobbies'))  #to get rid of above error we use get   it returns none

if user_info.get('name'):
    print("Present")
else:
    print("Absent")

print(user_info.get("nam","agar na mile key to yeh return hota h"))

# user_info.clear()
# print(user_info)


# Here x and user_info are same dictionaries
# we can use copy method so that we can work on them seprately


# x=user_info
# print(x)
# x.clear()
# print(x)
# print(user_info)
# print(x is user_info)  # returns True means same dictionaries



# s=user_info.copy()
# print(user_info is s) # returns False means different dictionaries





