# we will define it as a private variable
# so that it can not be changed

class stack:
    def __init__(self):
        self.__data=[]   # private variable  (we can take it as list named  self.__data)
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print(" stack is empty!! ")
            return
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            print(" stack is empty!! ")
            return
        return self.__data[len(self.__data)-1]  
    def size(self):
        return (len(self.__data))

    def isEmpty(self):
        return(self.size()==0)     # will be poped acc. to LIFO (last in first out)

 
