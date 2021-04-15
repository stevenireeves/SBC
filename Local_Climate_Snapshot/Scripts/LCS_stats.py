import os
import pandas as pd

DATA = '../Data/'
def perc_chg(df):
  chg = float(df.iloc[3]['change'])
  base = df.iloc[0]['average']
  #calculates ratio change, multiply by 100 to get percentage
  return ((base+chg)/(base)-1)*100

dataframes = {}
direc = os.listdir(DATA)
direc = sorted(direc)
for file in direc:
  dataframes[file[:-4]] = pd.read_csv(DATA+file)

for i in range(len(direc)):
  direc[i] = direc[i][:-4]

#creates a dictionary for the percentage change
percentage = {}
#creates a dictionary for the raw change
raw = {}
#creates a dictionary for the modeled baseline
baseline = {}

#use one loop for performance
for file in direc:
  df = dataframes[file]
  percentage[file] = perc_chg(df)
  raw[file] = df.iloc[3]['change']
  baseline[file] = df.iloc[0]['average']

final_df = pd.DataFrame(raw, index=[0])
final_df = final_df.append(baseline, ignore_index=True)
final_df = final_df.append(percentage, ignore_index=True)
final_df.index = ['Change', 'Baseline', '%Change']
final_df.to_csv('../Combined_Val.csv')

