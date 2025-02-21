
# to facilitate import command
import sys
sys.path.insert(1,'C:\\Users\\ankit\\OneDrive\\Desktop\\rathee\\python\\Stack\\Intro_3_Class_stack.py')

from Intro_3_Class_stack import stack

s=stack()
s.push(12)
s.push(13)
s.push(15)

while not s.isEmpty():
   print(s.pop())  # it willl print automatically without writing print