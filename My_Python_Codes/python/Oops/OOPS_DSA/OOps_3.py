# class Fraction:
#     def __init__(self,num=0,den=1):
#         self.num=num
#         self.den=den
# f=Fraction(1,3)
# print(f.__dict__)
# f2=Fraction(34)
# print(f2.__dict__)



class Fraction:
    def __init__(self,num=0,den=1):
        if den==0:
            # THROW ERROR
            den=1
        self.num=num
        self.den=den
    def print_it(self):
        if self.num==0:
            print(0)
        elif self.den==1:
            print(self.num)
        else:
            print(self.num,'/',self.den)
    def simplify(self):
        
        current =min(self.num,self.den)
        current=int(current)
        while current >1:
            if self.num % current ==0 and self.den % current ==0:
                break
            current-=1
        self.num=self.num//current
        self.den=self.den//current
        return(self.num,'/',self.den)


    def add (self,otherfraction):
        newNum=otherfraction.den * self.num  +  otherfraction.num * self.den
        newDen=otherfraction.den * self.den
        return Fraction(newNum,newDen)
        
    def multiply(self,otherfraction):
        newnumer=self.num*otherfraction.num
        newdeno=self.den*otherfraction.den
        return(Fraction(newnumer,newdeno))
        

# f1=Fraction(27,15)
# print(f1.simplify())


        


f3=Fraction(4,8)
f4=Fraction(12,6)

f9=(Fraction.add(f3,f4) )   
f9.simplify()
f9.print_it()


# f5=Fraction.multiply(f3,f4)
# f5.simplify()
# f5.print_it()


