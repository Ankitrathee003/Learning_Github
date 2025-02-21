user_info=dict(name='Ankit',age=34,fav_movies=('dangal','3idiot'))

#pop method
# e=user_info.pop('fav_movies') #it will return the values of fav_movies & delete the key value pair from list also.
# print(e,type(e))           # at least one argument to be passsed here
# print(user_info)


#popped item
#The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item
x=user_info.popitem()  #no argument to be passed here will return key as well as value
print(x)
print(user_info)


