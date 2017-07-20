import numpy as np
import math as math

lengthInitialMean = 0.000074
lengthInitialSD = 0

densityProjectileMean = 17300
densityProjectileSD = 0

densityTargetMean = 8000
densityTargetSD = 0

YpMean = 8000
YpSD = 0

RtMean = 3000
RtSD = 0

timeStep = 0.000001

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
    A = 2*((Rt-Yp)*(1-mu**2)/densityTarget)
    hydLimit = (densityProjectile/densityTarget)**0.5

    if vel <= Vc:
        Penetration = (densityProjectile/densityTarget)*np.log(1+((densityTarget*vel**2)/(2*Rt)))
    else:
        Penetration = 5

    return Penetration

Penetration = []
Velocity = []

for vel in range(0,2000,100):
    vel = vel/1000
    pen = MC_pen(lengthInitialMean, lengthInitialSD, densityProjectileMean,
    densityProjectileSD, densityTargetMean, densityTargetSD ,YpMean,
    YpSD,RtMean, RtSD, vel)

    Penetration.append(pen)
    Velocity.append(vel)

print(Penetration)
print(Velocity)


