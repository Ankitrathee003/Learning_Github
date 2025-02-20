def mod(l):
    # l[0]=33
    l=[1,2,3,4]
    l[0]=33
    # print(l)
l=[9,10]
mod(l)
print(l)



# In the code you provided, you have a function mod that takes a list l as an argument and assigns a new list [1, 2, 3, 4] to the variable l within the function. 
# Then, you call the mod function with the list [9, 10] as an argument and print the list l after calling the function.
# However, the modification you make to l within the mod function does not affect the original list l that was passed to the function.
#  This is because lists are mutable objects in Python, and when you assign a new value to a variable within a function, 
# it does not modify the original object passed as an argument.
# So, when you print l after calling mod(l), you will still get [9, 10], not [1, 2, 3, 4].
# If you want to modify the original list l within the function, 

# ########you can do so by modifying the elements of the list rather than reassigning the variable l.###########



def f(value, values):
    values[0]=44
t=9
v=[1,2,3]
f(t,v)
print(t,v)    ### output   9,[44,2,3]





#  Here's an example of how you can modify the original list:
# Inside the mod function, you create a new local variable l and assign it a new list [1, 2, 3, 4].
#  This local variable l is separate from the global variable l outside the function.
#  The modification only affects the local variable, not the global one.
# If you want to modify the original list passed to the function, 
# you should operate on the same list object rather than creating a new local variable. \
# You can do this by using methods like append, extend, or modifying elements within the list. For example:

def mod(l):
    l.extend([1, 2, 3, 4])
l = [9, 10]
mod(l)
print(l)  # This will print [9, 10, 1, 2, 3, 4]







# First let's try to access a global variable from the inside of a function,
# c = 1 
# def add():
#     print(c)
# add()   # Output: 1




# c = 1 
# def add():
#      # increment c by 2
#     c = c + 2
#     print(c)
# add()   #UnboundLocalError: local variable 'c' referenced before assignment


# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.
multiply=1
def multiply_nums(*args):
    for i in args:
        global multiply
        multiply*=i
    return(multiply)

# output 1
# print(multiply_nums(2,4,1))
# print(multiply)

#output 2
# print(multiply)
# print(multiply_nums(2,4,1))




def f(value, values):
    v=1
    values[0]=44
t=3
v=[1,2,3]
f(t,v)
# print(t,v)





txt = "I could eat bananas all day"
x = txt.partition("eat")
# print(x)

y="Hello"
a=y.partition("Hello")
# print(a)






# In most of the programming languages (C/C++, Java, etc), the use of else statement has been restricted with the 
# if conditional statements.
#  But Python also allows us to use the else condition with for loops.
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

for i in range(1, 4):
	print(i)
else: # Executed because no break in for
	print("No Break")


for i in range(1, 4):
    print(i)
    break
else: # Not executed as there is a break
    print("No Break")

print("abcdefbujnioj".partition("cd"))
a="asd"
b="frg"



## we can not add set and dict using + otherwise all can be added



# def binaryStrings(str,output):
#     n=len(str)


#     def helper(ans,ind):
#             if len(ans)==n:
#                 output.append(ans)
#                 return 
#             if str[ind]=="0" or str[ind]=="1":
#                 helper(ans+str[ind],ind+1)
#             elif len(ans)<n:
#                 helper(ans+"1",ind+1)
#                 helper(ans+"0",ind+1)
#     helper(ans="",ind=0)
#     return output
# output=[]
# binaryStrings("?",output)
# print(output)



def binaryStrings(s):
    # Write your code here.
	ans=""
	output=[]
	n=len(s)
	def helper(ans,ind):
		if len(ans)==n:
			output.append(ans)
			return 
		if s[ind]=='0' or s[ind]=='1':
			helper(ans+s[ind],ind+1)
		elif s[ind]=='?':
			helper(ans+"0",ind+1)
			helper(ans+"1",ind+1)
	
	helper(ans,ind=0)
	return output
# Main.
t = 1
for i in range(t):
	s = "1010?00??"
	result = binaryStrings(s)
	for res in result:
		print(res)


