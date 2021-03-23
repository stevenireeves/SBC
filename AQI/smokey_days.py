import numpy as np
import pandas as pd
import os

def YearlySmokeyDays(df):
  smoke_days = {}
  for i in range(df['Date PM'].iloc[0], df['Date PM'].iloc[-1]+1):
    smoke_days[i] = len(df[df['Date PM'] == i])
  return smoke_days


PATH='AirQual/'

data = os.listdir(PATH)
smokey_dict = {}
for i in range(len(data)):
  #load in AQI data
  print('Processing File ', data[i])
  County_df = pd.read_csv(PATH+data[i])
  name = data[i][:len(data[i])-8]
  if('PM2.5 AQI Value' in County_df):
    if(County_df.columns.values[2] == 'PM2.5 AQI Value'):
      PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[1,2]]
      PM_df['Date PM'] = PM_df['Date PM'].apply(lambda x: x[-4:]).astype(int)
    else:
      PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[3,4]]
      PM_df['Date PM'] = PM_df['Date PM'].apply(lambda x: x[-4:]).astype(int)
    PM_df = PM_df[PM_df['PM2.5 AQI Value'] > 101]
    smokey_dict[name] = YearlySmokeyDays(PM_df)

smokey_df = pd.DataFrame(smokey_dict)
smokey_df = smokey_df.sort_index(axis=0)
smokey_df = smokey_df.sort_index(axis=1)
smokey_df.to_csv('smokey_days2.csv')

  
