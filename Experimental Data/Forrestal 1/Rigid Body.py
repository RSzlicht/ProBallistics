import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

df = pd.DataFrame()
vel_array = list(range(0, 3050, 200))
vel = {"velocity": vel_array}   #m/s
df = pd.DataFrame(vel)

# Poncelet
a = 2*10**9     #Pa
b= 0.0201       #g/cm3
density_projectile =  7830  #kg/m3
Poncelet = []
# Calculat P/L IAW Poncelet equation
for x in vel_array:
    Poncelet.append((density_projectile/(2*b))*math.log(1+((b*x**2)/a)))
df['Poncelet']= pd.DataFrame(Poncelet)

# Spherical cavity expansion
#Target parameters
density_target = 2710   #kg/m3
Y = 276*10**6   #Pa
A = 5.04
B = 0.983
C = 0.94

#Projectile parameters
length_projectileBody = 59.3    #mm
length_projectileHead = 11.8    #mm
diameter_projectile = 7.11      #mm
radius_projectile = diameter_projectile / 2     #mm
psi = 3     #calibre radius head
#Dimensionless parameters
k = (4*psi**2-(4*psi/3)+(1/3))*()

print(df)
