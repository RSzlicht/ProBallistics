import numpy as np
import pandas as pd
import seaborn as sns

sns.set()
#hey man
# import data from CVS
file1 = 'Forrestal _Rc_36_6.csv'
file2 = 'Forrestal_Rc_39_5.csv'
file3 = 'Forrestal_Rc_ 46_2.csv'

# Define arrays
forrestal_Rc_36_6_data = []
forrestal_Rc_36_6_data_array = []
forrestal_Rc_39_5_data = []
forrestal_Rc_39_5_data_array = []
forrestal_Rc_46_2_data = []
forrestal_Rc_46_2_data_array = []

# Add list and array of data
forrestal_Rc_36_6_data = pd.read_csv(file1, header=0, sep=',', usecols=[2, 3, 4, 6])
forrestal_Rc_39_5_data = pd.read_csv(file2, header=0, sep=',', usecols=[2, 3, 4, 6])
forrestal_Rc_46_2_data = pd.read_csv(file3, header=0, sep=',', usecols=[2, 3, 4, 6])

forrestal_Rc_36_6_data_array = np.array(forrestal_Rc_36_6_data)
forrestal_Rc_39_5_data_array = np.array(forrestal_Rc_39_5_data)
forrestal_Rc_46_2_data_array = np.array(forrestal_Rc_46_2_data)

print(forrestal_Rc_36_6_data.head(0), forrestal_Rc_36_6_data_array)
print(forrestal_Rc_39_5_data.head(0), forrestal_Rc_39_5_data_array)
print(forrestal_Rc_46_2_data.head(0), forrestal_Rc_46_2_data_array)

