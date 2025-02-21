l=[]
n=int(input("enter the no. of elements: "))
for i in range (0,n):
    i=int(input())
    l.append(i)
print(l) 
def evod(l):  
  even =[]
  odd=[]
  for i in l:
      if (i%2==0):
        even.append(i)
      else:
        odd.append(i)
  return(print(f"even list is {even}     odd list is {odd}"))
evod(l)  
   

