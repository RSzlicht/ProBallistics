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

nReps = 1000

VAR_MC_pen_1=np.array([])
AerMet_MC_pen_1=np.array([])

Term1=data['Term1']
Term2=data['Term2']
Term3=data['Term3']
Term4=data['Term4']

Penetration_data={}
Penetration_velocity = []
velocity = [0,200,400,600,800,1000,1200,1400,1600,1800,2000]

def MC_pen(VAR_mass_mean,VAR_mass_std, x):
    mass_rnd = np.random.normal(VAR_mass_mean, VAR_mass_std)
    density_rnd = ((mass_rnd / 1000) / (math.pi * 0.004 ** 2 * 0.06574522))
    Penetration = (62.52417614*(density_rnd*Term1[x]+density_rnd*Term2[x]*
                                 (Term3[x]+Term4[x])))
    return Penetration

for x in range(0, 11):
    Penetration=[]
    Velocity1=[]
    velocity_value = velocity[x]

    for i in range(0,nReps):
        Penetration.append(MC_pen(VAR_mass_mean, VAR_mass_std, x))
        Velocity1.append(velocity_value)
        Penetration_data[velocity_value] = (Velocity1, Penetration)

Penetration_data_pd=pd.DataFrame(Penetration_data)
print(Penetration_data_pd[200][:][1])

# plot data
plt.plot(VAR_vel, VAR_pen,'.-', label='VAR 4340, Rc = 38.3', color = 'g')
plt.plot(AerMet_vel, AerMet_pen,'.-',label='AerMet 100, Rc = 53.3', color='b')
plt.plot(model_vel , model_pen, label= 'Model', color = 'y')

for x in velocity:
    plt.plot(Penetration_data_pd[x][:][0],Penetration_data_pd[x][:][1], label = x, color='r')

plt.title('Penetrator results')
plt.ylabel('Penetration (mm)')
plt.xlabel('Velocity (m/s)')
plt.legend()
plt.show()

