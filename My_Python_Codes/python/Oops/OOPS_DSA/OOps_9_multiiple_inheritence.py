# in multipe inheritence class will have properties from different base classes


class Mother:
    def __init__(self):
        self.name="Rajdevi"
    def print(self):
        print("print of mother called")


class Father:
    def __init__(self):
        self.name="sanjay"
    def print(self):
        print("print of father called")


class child(Mother,Father): ## print is in both super classes so print of that class will run who has been written first
    def __init__(self):
        super().__init__()
    def printchild(self):
        print("name of child is",self.name)


c=child()
c.printchild()
c.print()  # print is in both super classes so print of that class will run who has been written first
    

print(child.mro())                # TO watch the order in which these classes will be called is done with  help of method resolving order 
                    # method resolving order