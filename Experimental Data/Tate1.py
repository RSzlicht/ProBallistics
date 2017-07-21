import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

expVelocity = [0.496,0.572,0.781,0.821,0.841,0.932,0.967,1.037,1.193,1.337,1.515,1.802,2.052,2.204,2.777,3.075]
expPenetration = [37.6,48.1,72.7,84.3,91.4,96.5,94.4,64.6,50.7,61.8,76,94.3,113.9,124.6,147,151]

lengthInitialMean = 0.000074
lengthInitialSD = 0

densityProjectileMean = 17300
densityProjectileSD = 0

densityTargetMean = 7000
densityTargetSD = 0

YpMean = 7570
YpSD = 0

RtMean = 4000
RtSD = 0

dt = 0.000001
Penetration_data={}
Velocity_data={}

def MC_pen(lengthInitialMean, lengthInitialSD, densityProjectileMean,
    densityProjectileSD, densityTargetMean, densityTargetSD ,YpMean,
    YpSD,RtMean, RtSD, vel):

    lengthInitial = np.random.normal(lengthInitialMean, lengthInitialSD)
    densityProjectile = np.random.normal(densityProjectileMean, densityProjectileSD)
    densityTarget = np.random.normal(densityTargetMean, densityTargetSD)
    Yp = np.random.normal(YpMean, YpSD)
    Rt = np.random.normal(RtMean, RtSD)

    Vc = (2*((Yp-Rt)/densityTarget))**0.5
    mu = (densityTarget/densityProjectile)**0.5
    A = 2*((Rt-Yp)*(1-mu**2))/densityTarget
    hydLimit = (densityProjectile/densityTarget)**0.5

    if vel <= Vc:
        Penetration = lengthInitial*((densityProjectile/densityTarget)*np.log(1+((densityTarget*vel**2)/(2*Rt))))
    else:
        pen = 0
        length = lengthInitial
        while True:
            if length <= 0 or vel <= Vc:
                break
            U = (1/(1-mu**2))*(vel-mu*(vel**2 + A)**0.5)
            dldt = -(vel-U)
            dl = dldt * dt
            dvdt = -Yp/(densityProjectile*length)
            dv = dvdt * dt

            length = length + dl
            vel = vel + dv
            dp = U * dt
            pen = pen + dp

        Penetration=pen

    return Penetration * 10 ** 6

Penetration = []
Velocity = []

nReps = 2

for vel in range(0,3500,100):
    vel = vel / 1000
    for i in range(0, nReps):
        pen = MC_pen(lengthInitialMean, lengthInitialSD, densityProjectileMean,
                    densityProjectileSD, densityTargetMean, densityTargetSD ,YpMean,
                    YpSD,RtMean, RtSD, vel)

        Penetration.append(pen)
        Velocity.append(vel)

        Penetration_data[vel] = Penetration
        Velocity_data[vel] = Velocity

Penetration_data_pd = pd.DataFrame([Penetration])

print(Penetration_data_pd)

#Write data into excel
writer = pd.ExcelWriter('Data1.xlsx')
Penetration_data_pd.to_excel(writer,'Data1')
writer.save()