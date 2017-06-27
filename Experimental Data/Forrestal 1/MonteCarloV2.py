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

VAR_MC_pen_1=np.array([])
AerMet_MC_pen_1=np.array([])

Term1=data['Term1']
Term2=data['Term2']
Term3=data['Term3']
Term4=data['Term4']

Penetration=[]
Penetration_data={}

velocity=[0,200,400,600,800,1000,1200,1400,1600,1800,2000,]

def MC_pen(VAR_mass_mean,VAR_mass_std, x):
    mass_rnd = np.random.normal(VAR_mass_mean, VAR_mass_std)
    density_rnd = ((mass_rnd / 1000) / (math.pi * 0.004 ** 2 * 0.06574522))
    Penetration = (62.52417614*(density_rnd*Term1[x]+density_rnd*Term2[x]*
                                 (Term3[x]+Term4[x])))
    return Penetration

for x in range(0, 11):
    Penetration=[]
    velocity_value = velocity[x]

    for i in range(0,nReps):
        Penetration.append(MC_pen(VAR_mass_mean, VAR_mass_std, x))
        Penetration_data[velocity_value] = Penetration

Penetration_data_pd=pd.DataFrame(Penetration_data)
print(Penetration_data_pd)

