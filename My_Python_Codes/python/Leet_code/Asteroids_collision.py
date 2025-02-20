def asteroidCollision(asteroids):
    n=len(asteroids)
    i=0
    while i<n-1:
        if asteroids[i]>0 and asteroids[i+1]<0:
            if asteroids[i]>-asteroids[i+1]:
                asteroids.pop(i+1)
            elif asteroids[i]<-asteroids[i+1]:
                asteroids.pop(i)
                n-=1
                j=i
                while j>0:
                    if asteroids[j-1]<0:
                        break
                    elif asteroids[j-1]<-asteroids[j]:
                        asteroids.pop(j-1)
                        n-=1
                    elif asteroids[j-1]>-asteroids[j]:
                        asteroids.pop(j)
                        n-=1
                        break
                    else:
                        asteroids.pop[j]
                        asteroids.pop[j-1]
                        n-=2
                        break
            else:
                asteroids.pop(i+1)
                asteroids.pop(i)
                i-=1
                n-=2
        i+=1
    # print(asteroids)
    if len(asteroids)>1 and asteroids[-1]<0:
        j=len(asteroids)-1
        print(j)
        while j>0:
            if asteroids[j-1]<0:
                break
            elif asteroids[j-1]<-asteroids[j]:
                asteroids.pop(j-1)
                j-=1
            elif asteroids[j-1]>-asteroids[j]:
                asteroids.pop(j)
                j-=1
                break
            else:
                asteroids.pop(j)
                asteroids.pop(j-1)
                j-=2
                break
        return asteroids
asteroids=[-2,2,-1,1]
asteroidCollision(asteroids)