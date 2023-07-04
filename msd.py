import pandas as pd 
import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
d=0
k=0
p=0

df=pd.read_excel('1511.xlsx')

for d in range (1,601):
    k=0
    p=0
    x.append(d)
    for i in range (0,1253):
        e=i+d
        if e == 1253:
            break
        a=(df.iloc[i+d,1]-df.iloc[i,1])
        m=(df.iloc[i+d,2]-df.iloc[i,2])
        b=a**2
        n=m**2
        p=p+n
        k=k+b
    l=k/(1253-d)
    o=p/(1253-d)
    y1.append(l)
    y2.append(o)

nety=[]
for i in range (0,600):
    r=y1[i]+y2[i]
    nety.append(r)

plt.xlabel("Tau")
plt.ylabel("Net msd")
plt.xscale("log")
plt.yscale("log")


plt.plot(x,nety,'r', label='net msd')
plt.plot(x,y1, 'b', label='msd x_pixel')
plt.plot(x,y2, 'y', label='msd y_pixel')
plt.legend(loc="upper left")
plt.show()

print (y1[9])

