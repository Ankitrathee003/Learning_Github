n=6
def isPowerOfTwo(self, n: int) -> bool:
        i=0
        def check(n,i):
            if (n==2**i):
                return(True)
            elif(n<2**i):
                return(False)
            else:
                i+=1
                return check(n,i)
        
            