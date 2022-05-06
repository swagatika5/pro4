#Maxwell's speed distribution function at different temperature

import numpy as np
import matplotlib.pyplot as plt

#constants
k = 1.38e-23
N = 6.022e23
pi = 4*np.arctan(1.0)

def f(T,V): #Distribution function
    return 4*pi*((M/(2*pi*k*T))**(3/2))*((V)**2)*(np.exp((-M*((V)**2))/(2*k*T)))

m = int(input("molar mass of gas(g/mole) = "))
M = m/(N*1000)

def plotgraph(x,y,xlabelstr,ylabelstr,titlestr):
    plt.plot(x, y, lw = 3)
    plt.xlabel(xlabelstr, size = 12)
    plt.ylabel(ylabelstr, size = 12)
    plt.title(titlestr)
    
print("Plotting Maxwell's speed distribution func at diff temperature")
print(" ")
v = np.linspace(0,2000,2001) #taking v from 0-2000 m/s

#at T = 300k
y1 = np.zeros(2001)
for i in range(2001):
    y1[i] = f(300,v[i])
plotgraph(v,y1,"vel","distribution function","maxwell speed distribution function")

max_y1 = max(y1)
Vmp1 = v[y1.argmax()]
Vav1 = ((4/pi)**(1/2))*Vmp1
Vrms1 = ((3/2)**(1/2))*Vmp1
print("AT T = 300K")
print("Most probable speed : ",Vmp1," m/s")
print("Average speed : ",Vav1," m/s")
print("RMS speed : ",Vrms1," m/s")
print(" ")

#at T = 600k
y2 = np.zeros(2001)
for i in range(2001):
    y2[i] = f(600,v[i])
plotgraph(v,y2,"vel","distribution function","maxwell speed distribution function")

max_y2 = max(y2)
Vmp2 = v[y2.argmax()]
Vav2 = ((4/pi)**(1/2))*Vmp2
Vrms2 = ((3/2)**(1/2))*Vmp2
print("AT T = 600K")
print("Most probable speed : ",Vmp2," m/s")
print("Average speed : ",Vav2," m/s")
print("RMS speed : ",Vrms2," m/s")
print(" ")

#at T = 900k
y3 = np.zeros(2001)
for i in range(2001):
    y3[i] = f(900,v[i])
plotgraph(v,y3,"vel","distribution function","maxwell speed distribution function")

max_y3 = max(y3)
Vmp3 = v[y3.argmax()]
Vav3 = ((4/pi)**(1/2))*Vmp3
Vrms3 = ((3/2)**(1/2))*Vmp3
print("AT T = 900K")
print("Most probable speed : ",Vmp3," m/s")
print("Average speed : ",Vav3," m/s")
print("RMS speed : ",Vrms3," m/s")

plt.plot(v,y1)
plt.plot(v,y2)
plt.plot(v,y3)
plt.legend(["300K","600K","900K"])
plt.show()