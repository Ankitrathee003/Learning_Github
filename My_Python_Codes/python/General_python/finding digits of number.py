n=int(input("enter the no. you want to find the digits in list:  "))
def digits_of_number(n):
    import math
    
    y=n
    count=1
    while n>=9:
        n=math.floor(n/10)
        count+=1
    # print(count)
    d=count
    a=[]
    for i in range (count):
        if count==d:            #storing last digit once in list so that loop can be used for further updation. 
            a.append(y%10)
            count-=1
        else:
            for i in range (0,count):   
                y=(y-a[i])/10            # subtracting the last digit and dividing by 10 ad updating y.
                a.append((y)%10)
                count-=1
    a=a[::-1]          # reversing the list as we get ist in reverse order.
    return(a)
print(digits_of_number(n))




    


