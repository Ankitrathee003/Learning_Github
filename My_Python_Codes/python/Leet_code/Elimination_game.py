# def lastRemaining( n) :   
#         l=[i for i in range(1,n+1) if i%2==0]
#         n=len(l)
#         while len(l)!=1:
#             count=0
#             for j in range(-1,-n-1,-2):
#                 if len(l)!=1:
#                     l.pop(j+count)
#                     count+=1

#             n=len(l)
#             count=0

#             for i in range (0,n,2):
#                 if len(l)!=1:
#                     l.pop(i-count)
#                     count+=1
#             n=len(l)

#         return(l[0])
# print(lastRemaining(10))



def lastRemaining(n) :
        left_to_right = True
        remaining = n
        step = 1
        head = 1

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
print(lastRemaining(3))