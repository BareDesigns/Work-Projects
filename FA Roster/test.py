import pandas as pd
import time
import os

file = input('drop the file you want here\n')
timr = time.strftime("%m-%d-%y")

data = pd.read_csv(file, sep='|', header=0, skiprows=8)
data.drop('EMAIL', axis=1, inplace=True)
data.drop(data.index[200:], inplace=True)
data.sort_values(['REGTERM', 'PELL', 'APPTERM'],
                 ascending=[False, False, False], inplace=True)

data.to_csv(timr + '.csv')

print('\nComplete!!!!')
