import matplotlib.pyplot as plt
import numpy as np

plt.plot([0,2,4,6,4,2]) # here x axis is not mentioned that will be indices by default (0,1,2,3,4)
plt.show()

plt.plot([4,5,6,7,8],[16,25,36,49,64],'ro')  #plt.plot([x-axis array],[y-axis array],'ro'=red colour dots instead of line)
plt.grid()  # grid will be there in our plot
plt.show()



# plt.xlabel('Numbers')
# plt.ylabel('output/Range')
# plt.title('Sin(x)')
# x=np.linspace(0,44/7,60)  #taking x values =60 eually spaced from 0 to 2*pie.
# x1=np.arange(0,np.pi,0.5) 
# y=x1 
# print(y)
# plt.plot(x,np.sin(x),'g--',label='sin(x)')    #if we will use 'g-' it will plot straight line instead of dash line
# plt.plot(x,np.cos(x),'r^',label='cos(x)')
# plt.plot(y/10,linewidth=3,color='y',label="x/10") #linewidth #color
# plt.legend()
# plt.grid()
# plt.show()


# x2=np.arange(1,11,1)

# x3=[10,11,12,13,14,15]
# y3=[20,22,24,26,28,30]

# lines=plt.plot(x2,2*(x2),x3,y3)  #two lines y2 & y3 (INPUT1,output1,INPUT2,output2)
# plt.setp(lines[0],color='r',linewidth='3')  #to set properties of lines we use plt.setp
# plt.setp(lines[1],color='g',linewidth='1')
# plt.grid()
# plt.show()




                ###subplot###
def f(t):
    return(np.exp(-t)*np.cos(2*np.pi*t))


t1=np.arange(0,5,0.01)
plt.figure(94838478) # it is just figure no. useful when we are simultaneously show many figures differently in different windows here not so useful
                  # subplot no. where subplot ranges from 1 to numrows*numcols,subplot_NO.
plt.subplot(311)  #(311) meaning 3 rows 1 column  subplot 1
plt.grid()
plt.plot(t1,np.exp(-t1),'y-',label='e^(-x)')
plt.legend()

plt.subplot(312)
plt.grid()
plt.plot(t1,np.cos(2*np.pi*t1),label='cos(2*pie*t')
plt.legend()


plt.subplot(313)
plt.plot(t1,f(t1),color='r',label='multiply of 1 And 2')
plt.grid()
plt.legend()
plt.show()









