import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Simulate outcome variable
Y = pd.read_csv('pen.csv')
sns.distplot(Y)

from pymc3 import Model, Normal, HalfNormal

basic_model = Model()

with basic_model:

    # Priors for unknown model parameters
    mass = Normal('mass', mu=0.004, sd=0.000012)
    vel = Normal('vel', mu=815, sd=11.6)
    me = Normal('me', mu=0.5, sd = 10)
    sigma = HalfNormal('sigma', sd=1)

    # Expected value of outcome
    pen = 1000*(vel**2)*me*(((3*mass+0.00053)/95855.41)/5.283)

    # Likelihood (sampling distribution) of observations
    Y_obs = Normal('Y_obs', mu=pen, sd=sigma, observed=Y)

from pymc3 import find_MAP

map_estimate = find_MAP(model=basic_model)

print(map_estimate)

from pymc3 import NUTS, sample
from pymc3 import Slice
from scipy import optimize

with basic_model:

    # obtain starting values via MAP
    start = find_MAP(fmin=optimize.fmin_powell)

    # instantiate sampler
    step = Slice(vars=[sigma])

    # draw 5000 posterior samples
    trace = sample(5000, step=step, start=start)

from pymc3 import traceplot, summary

trace['me'][-5:]
traceplot(trace)
summary(trace)
plt.show()