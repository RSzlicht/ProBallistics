import numpy as np
import pandas as pd
import seaborn as sns

sns.set()

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

print(forrestal_VAR_4340_data)
print(forrestal_AerMet_100_data)


