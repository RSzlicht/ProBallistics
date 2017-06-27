import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math

# import data
data = pd.ExcelFile('Data.xlsx')
data = data.parse('Sheet4')
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

nReps = 100000
VAR_MC_pen=[]
AerMet_MC_pen=[]

for i in range (0,nReps):
    VAR_mass_rnd = np.random.normal(VAR_mass_mean,VAR_mass_std)
    VAR_density=((VAR_mass_rnd/1000)/(math.pi*0.004**2*0.06574522))
    VAR_MC_pen.append(62.52417614*(VAR_density*0.000191115+VAR_density*0.000166273*
                                 (0.210788537+-0.451507736)))

    AerMet_mass_rnd = np.random.normal(AerMet_mass_mean, AerMet_mass_std)
    AerMet_density=((AerMet_mass_rnd/1000)/(math.pi*0.004**2*0.06574522))
    AerMet_MC_pen.append(62.52417614*(AerMet_density * 0.000191115 + AerMet_density * 0.000166273 *
                                      (0.210788537 + -0.451507736)))

sns.distplot(VAR_MC_pen,kde_kws={"label": "VAR 4340"})
sns.distplot(AerMet_MC_pen,kde_kws={"label": "AerMet 100"})
sns.plt.show()