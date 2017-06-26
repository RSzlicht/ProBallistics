import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import data from CVS
file1 = 'AerMet 100 Rc 53.csv'
file2 = 'VAR 4340 Rc 38.csv'

# Define arrays
forrestal_AerMet_100_data = []
forrestal_AerMet_100_data_array = []
forrestal_VAR_4340_data = []
forrestal_VAR_4340_data_array = []

# Add list and array of data
forrestal_AerMet_100_data = pd.read_csv(file1, header=0, sep=',')
forrestal_VAR_4340_data = pd.read_csv(file2, header=0, sep=',')

forrestal_AerMet_100_data_array = np.array(forrestal_AerMet_100_data)
forrestal_VAR_4340_data_array = np.array(forrestal_VAR_4340_data)

# Get statistical parameters
AerMet_mass_mean, AerMet_mass_sd, \
AerMet_Rc_mean, AerMet_Rc_sd = (np.mean(forrestal_AerMet_100_data["Mass (g)"]),
                                np.std(forrestal_AerMet_100_data["Mass (g)"]),
                                np.mean(forrestal_AerMet_100_data["Hardness Rc"]),
                                np.std(forrestal_AerMet_100_data["Hardness Rc"]))

VAR_mass_mean, VAR_mass_sd, \
VAR_Rc_mean, VAR_Rc_sd = (np.mean(forrestal_VAR_4340_data["Mass (g)"]),
                                np.std(forrestal_VAR_4340_data["Mass (g)"]),
                                np.mean(forrestal_VAR_4340_data["Hardness Rc"]),
                                np.std(forrestal_VAR_4340_data["Hardness Rc"]))

fig=plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

ax1.scatter(forrestal_AerMet_100_data["Striking velocity Vs (m/s)"],
            forrestal_AerMet_100_data["P/L"])
ax1.scatter(forrestal_VAR_4340_data["Striking velocity Vs (m/s)"],
            forrestal_VAR_4340_data["P/L"])

ax2.hist(forrestal_AerMet_100_data["Mass (g)"])
ax2.hist(forrestal_VAR_4340_data["Mass (g)"])

plt.show()