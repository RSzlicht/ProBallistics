import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

# import data from CVS
file1 = 'Penetration_data.csv'

# Add list and array of data
forrestal_Penetration_data = pd.read_csv(file1, header=0, sep=',')

forrestal_AerMet_mass_data = pd.read_csv(file1, header=0, sep=',', nrows=14, usecols=[3])
forrestal_VAR_mass_data = pd.read_csv(file1, header=0, sep=',', skiprows=range(1,15),usecols=[3])

#Analytical analysis

Pp_AerMet = 7890        #Density kg/m3
Pp_VAR = 7830        #Density kg/m3
Rt = 2000000000            # Static target resistance (N/m2)
b = 0.0201          # Plastic flow resistance (g/cm3)
Length = 59.3       # Penetrator length (mm)

# Calculate analytical P/L
vel = (list(range(0, 3050, 200)))

PonL_VAR = []
PonL_AerMet = []

for x in vel:
    PonL_VAR.append((Pp_VAR/(2*b))*math.log(1+((b*x**2)/Rt)))
    PonL_AerMet.append((Pp_AerMet/(2*b))*math.log(1+((b*x**2)/Rt)))

vel = {"Velocity":vel}
vel_pd = pd.DataFrame(vel)

PonL_VAR = {"PonL_VAR":PonL_VAR}
PonL_VAR_pd = pd.DataFrame(PonL_VAR)

PonL_AerMet = {"PonL_AerMet":PonL_AerMet}
PonL_AerMet_pd = pd.DataFrame(PonL_AerMet)

data_pd = pd.concat([vel_pd, PonL_VAR_pd, PonL_AerMet_pd], axis=1)
print(data_pd)

#Plot data

plt.scatter(vel_pd, PonL_AerMet_pd, color='r')
plt.scatter(vel_pd, PonL_VAR_pd, color='b')
plt.scatter(forrestal_Penetration_data["Striking velocity Vs (m/s)"],forrestal_Penetration_data["P/L"], color='g')
plt.xlabel("Velocity")
plt.ylabel("P/L")
plt.show()