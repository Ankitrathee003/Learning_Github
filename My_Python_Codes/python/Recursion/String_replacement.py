s='dpiepielkpie'
#method 1
# def string_rep(s,i):
#     if len(s)==0:
#         return('it is empty string')
#     elif i<len(s):
#         if s[i]=='a':
#             s=s.replace('a','b',1)
#             return(string_rep(s,i+1))
#         else:
#             return(string_rep(s,i+1))
#     elif i==len(s):
#         return(s)
# print(string_rep(s,0))


#  method 2

# def string_repl(s,a,b):
#     if len(s)==0 :
#         return(s)
#     smalloutput=string_repl(s[1:],a,b)
#     if s[0]==a:
#         return(b+smalloutput)
#     else:
#         return(s[0]+smalloutput)
# print(string_repl('babararb','b','a')) 

#  method 3
def string_repl(s,a,b):
    if len(s)==0 or len(s)==1 or len(s)==2:
        return(s)
    if s[0]=='p' and s[1]=='i' and s[2]=='e':
        return(b+string_repl(s[3:],a,b))
    else:
        return(s[0]+string_repl(s[1:],a,b))
print(string_repl('babapiehgpierarb','pie','3.14'))




    

     