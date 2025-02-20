# a = [[2,8,7],[7,1,3],[1,9,5]]
# print(max(sum(a[i]) for i in range(len(a))))
n=15
# def d(n):
x=list(map(str,range(1,(n+1))) )
# for i in range(16):
#     if i%3==0:
#         x[i-1]="fizz"
#     if i%5==0:
#         x[i-1]="Buzz"
#     if i%15==0:
#         x[i-1]="Fizzbuzz"
# print(x)


# def fizzBuzz( n) :
#     return ['FizzBuzz' if not i%15 else 'Fizz' if not i%3 else 'Buzz' if not i%5 else str(i) for i in range(1,n+1)]
# print(fizzBuzz(100) )


# for i in range (1,61):
#     if not i%30:   # implies i divisible by 30
#         print(i)


l=[1,9,-2,3,4] 
t=2
for i in range (len(l)):
    for j in range (len(l)):
        if i!=j and t==(l[i]+l[j]) :
                print(i,j)


    


            
    




