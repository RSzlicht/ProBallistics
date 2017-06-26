import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

# import data from CVS
file1 = 'Penetration_data.csv'

# Add list and array of data
forrestal_Penetration_data = pd.read_csv(file1, header=0, sep=',')

forrestal_AerMet_mass = pd.read_csv(file1, header=0, sep=',', nrows=14, usecols=[3])
forrestal_AerMet_vel = pd.read_csv(file1, header=0, sep=',', nrows=14, usecols=[1])
forrestal_AerMet_PonL = pd.read_csv(file1, header=0, sep=',', nrows=14, usecols=[6])

forrestal_VAR_mass_data = pd.read_csv(file1, header=0, sep=',', skiprows=range(1,15),usecols=[3])
forrestal_VAR_vel = pd.read_csv(file1, header=0, sep=',',skiprows=range(1,15), usecols=[1])
forrestal_VAR_PonL = pd.read_csv(file1, header=0, sep=',', skiprows=range(1,15), usecols=[6])

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

#Plot data
plt.subplot(2, 1, 1)
plt.plot(vel_pd, PonL_VAR_pd, label='Poncelet')
plt.plot(forrestal_VAR_vel, forrestal_VAR_PonL,'.-', label= 'Forrestal et al')
plt.title('VAR penetrator results')
plt.ylabel('P/L')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(vel_pd, PonL_AerMet_pd, label='Poncelet')
plt.plot(forrestal_AerMet_vel, forrestal_AerMet_PonL, '.-', label = 'Forrestal et al.')
plt.title('AerMet penetrator results')
plt.xlabel('Velocity (m/s)')
plt.ylabel('P/L')
plt.legend()
plt.show()

plt.show()
