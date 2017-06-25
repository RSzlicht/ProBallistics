import Data_Import as di
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Simulate outcome variable
Y = di.forrestal_Rc_39_5_data_array[:, 2]

sns.distplot(Y, bins=len(Y))

from pymc3 import Model, Normal

basic_model = Model()

with basic_model:

    # Priors for unknown model parameters
    vel = Normal('vel', mu=1000, sd=11.6)
    sigma = Normal('sigma', mu=np.mean(di.forrestal_Rc_39_5_data_array[:, 3]),
                   sd = np.std(di.forrestal_Rc_39_5_data_array[:, 3] ))
    # Expected value of outcome
    pen = 1000*(vel**2)*0.42*(((3*0.004+0.00053)/95855.41)/5.283)

    # Likelihood (sampling distribution) of observations
    Y_obs = Normal('Y_obs', mu=pen, sd=sigma, observed=Y)

from pymc3 import find_MAP

map_estimate = find_MAP(model=basic_model)

print(map_estimate)

from pymc3 import sample
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

trace['vel'][-5:]
traceplot(trace)
summary(trace)
plt.show()

print(np.mean(Y), np.std(Y))