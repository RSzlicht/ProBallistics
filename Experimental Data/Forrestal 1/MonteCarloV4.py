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

nReps = 10000

VAR_MC_pen_1=np.array([])
AerMet_MC_pen_1=np.array([])

Term1=data['Term1']
Term2=data['Term2']
Term3=data['Term3']
Term4=data['Term4']

velPoints = [0,200,400,600,800,1000,1200,1400,1600,1800,2000]

def MC_pen(VAR_mass_mean,VAR_mass_std, x):
    mass_rnd = np.random.normal(VAR_mass_mean, VAR_mass_std)
    density_rnd = ((mass_rnd / 1000) / (math.pi * 0.004 ** 2 * 0.06574522))
    Penetration = (62.52417614*(density_rnd*Term1[x]+density_rnd*Term2[x]*
                                 (Term3[x]+Term4[x])))
    return Penetration

Penetration_data={}
Velocity_data={}
columns=[]
comb_vel=[]
comb_pen=[]

for x in range(0, 11):
    Penetration=[]
    Velocity=[]
    velocity_value = velPoints[x]
    df=[]

    for i in range(0,nReps):
        pen = (MC_pen(VAR_mass_mean, VAR_mass_std, x))

        Penetration.append(pen)
        Velocity.append(velocity_value)

        Penetration_data[velocity_value] = Penetration
        Velocity_data[velocity_value] = Velocity

        comb_vel.append(velocity_value)
        comb_pen.append(pen)

Penetration_data_pd=pd.DataFrame(Penetration_data)

Velocity_Headings=['vel_1 (m/s)','vel_2 (m/s)','vel_3 (m/s)','vel_4 (m/s)','vel_5 (m/s)','vel_6 (m/s)',
                   'vel_7 (m/s)','vel_8 (m/s)','vel_9 (m/s)','vel_10 (m/s)','vel_11 (m/s)']

Penetration_Headings=['Pen_1 (mm)','Pen_2 (mm)','Pen_3 (mm)','Pen_4 (mm)','Pen_5 (mm)','Pen_6 (mm)','Pen_7 (mm)',
                    'Pen_8 (mm)','Pen_9 (mm)','Pen_10 (mm)','Pen_11 (mm)','Pen_12 (mm)']

# Create columns from each velocity point
df = {'velocity':Velocity_data[0], 'Penetration':Penetration_data[0]}
df = pd.DataFrame(df, columns=('velocity', 'Penetration'))

for x in range(1, 11):
    velocity_value = velPoints[x]
    V_Heading = Velocity_Headings[x]
    P_Heading = Penetration_Headings[x]

    df[V_Heading] = pd.DataFrame(Velocity_data[velocity_value])
    df[P_Heading] = pd.DataFrame(Penetration_data[velocity_value])

# Create combined DateFrame
df_comb = {'velocity':comb_vel, 'Penetration':comb_pen}
df_comb = pd.DataFrame(df_comb, columns=('velocity', 'Penetration'))


#Write data into excel
writer = pd.ExcelWriter('Data.xlsx')
df.to_excel(writer,'Data')
writer.save()

sns.lmplot(x='velocity', y='Penetration', data=df_comb, x_jitter=.05, order=2, markers='+')
sns.plt.show()