rec1 =[0,0,1,1]
rec2 =[1,0,2,1]

x1=min(rec1[0],rec2[2],rec1[2],rec2[0])
x2=max(rec1[0],rec2[2],rec1[2],rec2[0])

y1=min(rec1[1],rec2[3],rec1[3],rec2[1])
y2=max(rec1[1],rec2[3],rec1[3],rec2[1])
print(x1,x2,y1,y2)

area=(x2-x1)*(y2-y1)
print(f'area is {area}')

AA=(rec1[3]-rec1[1])*(rec1[2]-rec1[0])+(rec1[3]-rec1[1])*(rec1[2]-rec1[0])

area2=(rec1[2]-rec1[0]+rec2[2]-rec2[0])*(rec1[3]-rec1[1]+rec2[3]-rec2[1])
print(f'area2 is {area2}')

# if area
if area<area2:
    print(True)
else:
    print(False)