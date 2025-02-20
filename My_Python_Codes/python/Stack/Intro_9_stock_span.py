# to facilitate import command
import sys
sys.path.insert(1,'C:\\Users\\ankit\\OneDrive\\Desktop\\rathee\\python\\Stack\\Intro_3_Class_stack.py')

from Intro_3_Class_stack import stack 

s=stack()
s.push(0)

output=[1]

p=[5,3,8,7,10,7,7,12,16,13]   # we will make such that even if we get same we will check up to end. ex 7, 7 in our ex. or we will keep counting backward untill we get greater
n=len(p)

for i in range (n-1):
    if  p[i+1]<p[i]:    
        output.append(1)
    else:
            if (p[s.top()]<=p[i]):
                 output.append(i+1)
                 s.push(i)
            else:
                 output.append(i+1-s.top())
print(output)
                 


        




    









 