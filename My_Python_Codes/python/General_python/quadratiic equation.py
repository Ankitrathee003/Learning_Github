from cmath import sqrt
x=(input("enter the value of coefficients of exponents i.e a,b,c    ").split(","))
print(type(x[1]))
x1=-(int(x[1])/(2*int(x[0])))+ (sqrt(int(x[1])**2-4*(int(x[0]))*int(x[2])))/(2*int(x[0]))
x2=-(int(x[1])/(2*int(x[0])))- (sqrt(int(x[1])**2-4*(int(x[0]))*int(x[2])))/(2*int(x[0]))
print(f"roots are {x1} and {x2}")
