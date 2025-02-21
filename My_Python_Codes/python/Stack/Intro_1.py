#  Stack is used to store elements like array and linked list 
#  it can be thought as of storing data in a bucket means same single point of entry and exit.
#  so here to access any element we have to access or remove elements present before than that


# Stack  is a ABSTRACT DATA TYPE

        # Before understanding what ADT is let us consider different in-built data types that are provided to us. 
        # Data types such as int, float, double, long, etc. are considered to be in-built data types 
        # and we can perform basic operations with them such as addition, subtraction, division, multiplication, etc.
        # Now there might be a situation when we need operations for our user-defined data type which have to be defined.
        # These operations can be defined only as and when we require them. So, in order to simplify the process of solving problems, 
        # we can create data structures along with their operations, and such data structures that are not in-built are known as Abstract Data Type (ADT).

# FUNCTIONALITIES
        #  push-->Insert
        #  pop--> delete
        #  top--> Access the top elements of stack without removing it
        #  size ---> No. of elements present in stack at that time
        #  is empty ---> is a boolean functioon

# Example if we insert no. in a stack name S = 22,33,44,55,66 in stack in given order 
# using consecutive   S.push(10),S.puch(33).......S.push(66) 
# so if we will use S.pop it will delete or give last element entered i.e 66



