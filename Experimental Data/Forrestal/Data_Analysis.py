import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# import data from CVS
file1 = 'Forrestal_Rc_39_5.csv'

# Define arrays
forrestal_Rc_39_5_data = []
forrestal_Rc_39_5_data_array = []

# Add list and array of data
forrestal_Rc_39_5_data = pd.read_csv(file1, header=0, sep=',', usecols=[2, 3, 4, 6])
forrestal_Rc_39_5_data_array = np.array(forrestal_Rc_39_5_data)

print(forrestal_Rc_39_5_data.head(0), forrestal_Rc_39_5_data_array )

# Display histogram of variables
fig, axs = plt.subplots(ncols=3)
sns.distplot(forrestal_Rc_39_5_data["Projectile mass m(g)"], ax=axs[0], axlabel="mass (mg)")
sns.distplot(forrestal_Rc_39_5_data["Projectile hardness Rc"], ax=axs[1], axlabel="Projectile hardness Rc)")
sns.distplot(forrestal_Rc_39_5_data["Striking velocity Vs (m/s)"], ax=axs[2], axlabel="Striking velocity Vs (m/s)")

sns.plt.show()

