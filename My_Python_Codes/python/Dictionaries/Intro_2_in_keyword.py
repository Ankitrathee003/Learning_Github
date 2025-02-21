#in keyword check whether particular key is present
user_info=dict(name='Ankit',age=34,fav_movies=['dangal','3idiot'])
if 'fav_movies' in user_info:
    print('present')
else:
    print('absent')

#if we want to check for values instead of key in a dictionary
user_info=dict(name='Ankit',age=34,fav_movies=['dangal','3idiot'])
if 34 in user_info.values():
    print('present')
else:
    print('absent')
    
