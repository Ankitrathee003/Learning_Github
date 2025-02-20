# handling Exceptions
## TRY and EXCEPT

# try:
#     num=int(input('Enter the no. '))
  
#     den=int(input('Enter the denomminator '))
   
#     fraction = num/den
#     print(fraction)
# except ValueError:  # some more errors are nameError
#     print("Numerator and denominators should be integer")




## Multiple Exceptiontry:
# try:
#     num=int(input('Enter the no. '))
  
#     den=int(input('Enter the denomminator '))
   
#     fraction = num/den
#     print(fraction)
# except ValueError:  # some more errors are nameError
#     print("Numerator and denominators should be integer")
# except ZeroDivisionError:
#     print("Dnominator should not be zero")





## Custom Exceptions

try:
    num=int(input('Enter the no. '))
    den=int(input('Enter the denomminator '))
    fraction = num/den
    if den==0:
        raise ZeroDenominatorError('Denominator should not be zero')
    print("hi")
    print(fraction)
except ValueError:  # some more errors are nameError
    print("Numerator and denominators should be integer")
except ZeroDivisionError:
     print("Division by zero is not allowed")
except ZeroDenominatorError:
    print("Zerodenominatorerror is raised")
