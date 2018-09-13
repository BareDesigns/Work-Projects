import pandas as pd
from progress.bar import IncrementalBar
import time
import os

# os.chdir("G:\Enrollment Management Center\FA Roster")
os.chdir("/Volumes/Groups/Enrollment Management Center/FA Roster")

file = input('Drop the file you want here:\n')
timr = time.strftime("%m-%d-%y")  # Sets the file name to current date
bar = IncrementalBar(max=15)

try:
    for i in range(15):
        data = pd.read_csv(file, sep='|', header=0, skiprows=5)
        data.drop('EMAIL', axis=1, inplace=True)  # Deletes Email column
        data.drop(data.index[200:], inplace=True)  # Limits rows to 200
        data.sort_values(['REGTERM', 'PELL', 'APPTERM'],  # Sort order
                         ascending=[False, False, False], inplace=True)

        data.to_excel(timr + '.xlsx', index=False)

        time.sleep(0.2)
        bar.next()
    bar.finish()
    print('\nComplete!!!!')

# If user didn't remove quotes or spaces
except FileNotFoundError:
    print('\nMake sure there are no spaces or quotes and try again\n')
