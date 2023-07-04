import pandas as pd
import matplotlib.pyplot as plt
d=e=i=t=0
df=pd.read_excel('abc.xlsx')
x=y=[]


for t in range (1,600) :
    d=0
    x.append(t)
    
    for i in range (0,1252):
        f=i+t
        if f >= 1250 :
            break
        b=(df.iloc[i+t,1]-df.iloc[i,1])
        c=b**2
        d=d+c
    e=d/(1252-t)
    y.append(e)
plt.ylim(1,1000)
plt.xlim([1,800])
plt.plot(x,y)
plt.show()
print(y[1])

        
        
    
    






    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
