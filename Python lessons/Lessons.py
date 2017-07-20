import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math as math
import plotly
plotly.tools.set_credentials_file(username='RichSzlicht', api_key='QIhnCs8ZDCTXILkM0ZSI')


data = pd.ExcelFile('cylinders.xlsx')
data = data.parse('Sheet1')
data = pd.DataFrame(data)

variance = [data['Strength (MPa)']**2]
data['Variance']=variance[:][0]

print(data)

print('mean: {:.2f}'.format(np.mean(data['Strength (MPa)'])))
print('Var: {:.2f}'.format(np.var(data['Strength (MPa)'])))
print('var^0.5: {:.2f}'.format(np.std(data['Strength (MPa)'])))

