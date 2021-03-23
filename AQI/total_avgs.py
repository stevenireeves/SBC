import numpy as np
import pandas as pd
import os

#Function for computing the average Ozone AQI
def ave_ozone(df):
  return df['Ozone AQI Value'].mean()

#Function for computing the ten year average PM2.5 AQI
def ave_pm25(df):
  return df['PM2.5 AQI Value'].mean()

PATH='AirQual/'

data = os.listdir(PATH)
oz_ave = {}
pm_ave = {}

for i in range(len(data)):
  #load in AQI data
  print('Processing File ', data[i])
  County_df = pd.read_csv(PATH+data[i])
  name = data[i][:len(data[i])-8]
  if(County_df.columns.values[2] == 'Ozone AQI Value'):
    Ozone_df = County_df[County_df['Ozone AQI Value'].values>0].iloc[:,[1,2]]
    oz_ave[name] = ave_ozone(Ozone_df)
  else:
    PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[1,2]]
    pm_ave[name] = ave_pm25(PM_df)
  if(len(County_df.columns) > 3):
    PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[3,4]]
    pm_ave[name] = ave_pm25(PM_df)

final_df = pd.DataFrame(oz_ave, index=[0])
final_df = final_df.append(pm_ave, ignore_index=True)
final_df.index = ['Total Ozone AQI Average', 'Total PM2.5 AQI Average']
final_df = final_df.sort_index(axis=1)
final_df.to_csv('Total_AQI_avgs.csv')

  
