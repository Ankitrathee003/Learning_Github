n = int(input('enter the number'))
list1 = []
for i in range(n):
  value = int(input('enter the value'))
  list1.append(value)
print('list formed', list1)
num = int(input('enter how much largest number wants to find'))
list3 = []
for k in range(0,num):
  list2 = []
  max1 = 0
  for j in list1:
    if j > max1:
      max1 = j

  for m in list1:
    if m!= max1:
      list2.append(m) 
     
  list1 = list2  
  list3.append(max1)     
print(list3) 