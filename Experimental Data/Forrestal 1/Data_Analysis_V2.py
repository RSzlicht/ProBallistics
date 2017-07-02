import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

# import data
data = pd.ExcelFile('Pen_Data.xlsx')
data = data.parse('csv')
data=pd.DataFrame(data)

VAR_vel=data['velocity (m/s)'][:20]
VAR_mass=data['Mass (g)'][:20]
VAR_mass_mean = np.mean(VAR_mass)
VAR_mass_std = np.std(VAR_mass)
VAR_pen = data['Penetration (mm)'][:20]

AerMet_vel=data['velocity (m/s)'][20:34]
AerMet_mass = data['Mass (g)'][20:34]
AerMet_mass_mean = np.mean(AerMet_mass)
AerMet_mass_std = np.std(AerMet_mass)
AerMet_pen = data['Penetration (mm)'][20:34]

model_vel = data['velocity (m/s)'][34:]
model_pen = data['Penetration (mm)'][34:]

# plot data
plt.plot(VAR_vel, VAR_pen,'.-', label='VAR 4340, Rc = 38.3')
plt.plot(AerMet_vel, AerMet_pen,'.-',label='AerMet 100, Rc = 53.3')
plt.plot(model_vel , model_pen, label= 'Model')
plt.title('Penetrator results')
plt.ylabel('Penetration (mm)')
plt.xlabel('Velocity (m/s)')
plt.legend()
plt.show()

#Distributions
VAR_mass_dist = np.random.normal(VAR_mass_mean,VAR_mass_std, 1000)
AerMet_mass_dist = np.random.normal(AerMet_mass_mean,AerMet_mass_std, 1000)

sns.distplot(VAR_mass_dist, axlabel="mass (g)", kde_kws={"label": "VAR 4340"})
sns.distplot(AerMet_mass_dist, axlabel="mass (g)",kde_kws={"label": "AerMet 100"})
plt.show()
