# def tower_hanoi(n,source,helper,destination):
#     if n==1:
#         print("move 1st disk from ",source," to ",destination)
#         return
#     tower_hanoi(n-1,source,destination,helper)
#     print("move ",n,"th disk from ",source," to ",destination)
#     tower_hanoi(n-1,helper,source,destination)

# tower_hanoi(2,'source','helper','destination')



def toh(n,a,b,c):
    if n == 1:
        print("Place disk",n,"th disk from",a,'to',c)
        return
    toh(n-1,a,c,b) 
    print("Place disk",n,"th disk from",a,'to',c)
    toh(n-1,b,a,c)
toh(4,'a','h','d')
    