import math 
count = 0
def Function(n): 
    global count 
    if n <= 2: 
       print(("hello i am here"))
    else: 
        
        print(f"www {math.sqrt(n)}")
        print(round(math.sqrt(n)))
        print(f"1st count is {count}")
        Function(round(math.sqrt(n))) 
        print(f"2nd count is {count}")

        count = count+1 
        print(count)
        return (count )
print(Function(100)) 