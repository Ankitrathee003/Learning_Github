import math
x=input("Enter the word you want to check for palindrome:  ")
def palindrome(x):
    for i in range(0, math.floor((len(x))/2)):  #floor largest integer function. give(-43) for (-42.1) & give(8) for (8.94)
        if x[i]==x[(len(x)-i-1)]:
            if i==math.floor((len(x)/2)-1):
                return(f"{x}  is a palindrome of length {len(x)}")
        else:
            return((f"{x}  is  NOT a palindrome of length {len(x)}"))
print(palindrome(x) )             

