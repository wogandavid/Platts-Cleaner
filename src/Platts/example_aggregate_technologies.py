import pandas as pd
import numpy as np 

data = {"Economy": ["BD", "BD", "BD", "BD", "BD", "BD", "INA", "INA", "INA", "INA", "INA", "INA"],
		"Tech": ["Hydro", "Hydro", "Hydro", "GT", "GT", "GT", "Hydro", "Hydro", "Hydro", "GT", "GT", "GT"],
		"Capacity": [24, 28, 40, 22, 29, 33, 31, 26, 21, 36, 25, 31]}
df = pd.DataFrame(data)

#Total sum per row: 
bins= [0,30,40,100]
labels = ['Hydro-Small','Hydro-Medium','Hydro-Large']
df['binned'] = df['Tech']
dff = df.loc[(df['Economy']=='INA') & (df['Tech']=='Hydro')]
df['binned'] = pd.cut(dff['Capacity'], bins=bins, labels=labels)

df['binned'] = np.where(df['binned'].isnull(), df['Tech'], df['binned'])
