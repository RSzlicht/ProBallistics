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
Rt = 2*10e9            # Static target resistance (N/m2)
b = 0.0201          # Plastic flow resistance (g/cm3)
Length = 59.3       # Penetrator length (mm)

# Calculate analytical P/L
vel = (list(range(0, 3050, 50)))

PonL_VAR = []
PonL_AerMet = []

for x in vel:
    PonL_VAR.append((Pp_VAR/(2*b))*math.log(1+((b*x**2)/Rt)))
    PonL_AerMet.append((Pp_AerMet/(2*b))*math.log(1+((b*x**2)/Rt)))

vel = {"Velocity":vel}
vel = pd.DataFrame(vel)

PonL_VAR = {"PonL_VAR":PonL_VAR}
PonL_VAR = pd.DataFrame(PonL_VAR)

PonL_AerMet = {"PonL_AerMet":PonL_AerMet}
PonL_AerMet = pd.DataFrame(PonL_AerMet)

data = pd.concat([vel, PonL_VAR, PonL_AerMet], axis=1)
print(data)

#Plot data
sns.lmplot(x="Striking velocity Vs (m/s)", y="P/L", data=forrestal_Penetration_data, hue="Penetrator", fit_reg=False)
sns.lmplot(x='Velocity', y='PonL_VAR', data=data)
plt.show()