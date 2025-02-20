
#To print name of keys & values


user_info=dict(name='Ankit',age=34,fav_movies=['dangal','3idiot'])
# for i in user_info:
#     print(i)
# for i in user_info.values():
#     print(i)

#dict_values
# x=user_info.values()
# print((x),type(x))


# printing values using keys
# for i in  user_info:           # i=key here
#     print(user_info[i])


#item_method   (dict_items) will return list of tuples  of <class 'dict_items'>
#dict_items([('name', 'Ankit'), ('age', 34), ('fav_movies', ['dangal', '3idiot'])]) <class 'dict_items'>
# q=user_info.items()
# print(q,type(q))


# # <class 'dict_items'>
# for x,y in user_info.items():
#     print(f"key is {x} and value is {y}")



for x in user_info.items():
    # print(x)
    print(x[0])
    # print(x[1])