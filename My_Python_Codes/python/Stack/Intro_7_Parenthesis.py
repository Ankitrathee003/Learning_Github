open=['(','[','{','<',"'"]
close=[')',']','}','>',"'"]
str='{([(a-b)]),999([oo][{[]}])}'
s=[]

def parenthesis_check(open,close,str):
    if str[0] in close:
        return(False)
    for i in str:
            if i in open:
                s.append(i) 
            elif i in close:
                if s[-1]==open[close.index(i)]:
                    if s :    # we can pop() only when list s is nonn empty
                        s.pop()
                    else:
                      return(False)
                else:
                     return(False)
    return (not s)  # in last  stack should be empty for TRUE

                
print(parenthesis_check(open,close,str))



# without using extra space

# def check_parentheses(input_string):
#     stack = []  # Initialize an empty stack

#     for char in input_string:
#         if char == "(":
#             stack.append(char)  # Push opening parentheses onto the stack
#         elif char == ")":
#             if not stack or stack[-1] != "(":  # Check if stack is empty or if the top element is not an opening parenthesis
#                 return False
#             stack.pop()  # Pop the opening parenthesis from the stack

#     return len(stack) == 0  # Check if the stack is empty after processing all parentheses

# # Take input from the user
# user_input = input("Enter a string with parentheses: ")

# # Check if the parentheses are balanced
# if check_parentheses(user_input):
#     print("The parentheses are balanced.")
# else:
#     print("The parentheses are not balanced.")

    
