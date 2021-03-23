import numpy as np
import pandas as pd
import os

#Function for computing the ten year average Ozone AQI
def ave_ozone_10(df):
  sum_aqi = 0
  num_aqi = 0
  for i in range(len(df)):
    if df['Date Oz'].iloc[i] >= 2008 and df['Date Oz'].iloc[i] <= 2018:
      sum_aqi += df['Ozone AQI Value'].iloc[i]
      num_aqi += 1
  if num_aqi > 0:
    return sum_aqi/num_aqi
  return 0

#Function for computing the five year average Ozone AQI
def ave_ozone_5(df):
  sum_aqi = 0
  num_aqi = 0
  for i in range(len(df)):
    if df['Date Oz'].iloc[i] >= 2013 and df['Date Oz'].iloc[i] <= 2018:
      sum_aqi += df['Ozone AQI Value'].iloc[i]
      num_aqi += 1
  if num_aqi > 0:
    return sum_aqi/num_aqi
  return 0
     
#Function for computing the ten year average PM2.5 AQI
def ave_pm25_10(df):
  sum_aqi = 0
  num_aqi = 0
  for i in range(len(df)):
    if df['Date PM'].iloc[i] >= 2008 and df['Date PM'].iloc[i] <= 2018:
      sum_aqi += df['PM2.5 AQI Value'].iloc[i]
      num_aqi += 1
  if num_aqi > 0:
    return sum_aqi/num_aqi
  return 0

#Function for computing the five year average PM2.5 AQI
def ave_pm25_5(df):
  sum_aqi = 0
  num_aqi = 0
  for i in range(len(df)):
    if df['Date PM'].iloc[i] >= 2013 and df['Date PM'].iloc[i] <= 2018:
      sum_aqi += df['PM2.5 AQI Value'].iloc[i]
      num_aqi += 1
  if num_aqi > 0:
    return sum_aqi/num_aqi
  return 0

PATH='AirQual/'

data = os.listdir(PATH)
year_oz_5  = {}
year_oz_10 = {}
year_pm_5  = {}
year_pm_10 = {}

for i in range(len(data)):
  #load in AQI data
  print('Processing File ', data[i])
  County_df = pd.read_csv(PATH+data[i])
  name = data[i][:len(data[i])-8]
  if(County_df.columns.values[2] == 'Ozone AQI Value'):
    Ozone_df = County_df[County_df['Ozone AQI Value'].values>0].iloc[:,[1,2]]
    Ozone_df['Date Oz'] = Ozone_df['Date Oz'].apply(lambda x: x[-4:]).astype(int)
    year_oz_5[name] = ave_ozone_5(Ozone_df)
    year_oz_10[name] = ave_ozone_10(Ozone_df)
  else:
    PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[1,2]]
    PM_df['Date PM'] = PM_df['Date PM'].apply(lambda x: x[-4:]).astype(int)
    year_pm_5[name] = ave_pm25_5(PM_df)
    year_pm_10[name] = ave_pm25_10(PM_df)
  if(len(County_df.columns) > 3):
    PM_df = County_df[County_df['PM2.5 AQI Value'].values>0].iloc[:,[3,4]]
    PM_df['Date PM'] = PM_df['Date PM'].apply(lambda x: x[-4:]).astype(int)
    year_pm_5[name] = ave_pm25_5(PM_df)
    year_pm_10[name] = ave_pm25_10(PM_df)

final_df = pd.DataFrame(year_oz_5, index=[0])
final_df = final_df.append(year_oz_10, ignore_index=True)
final_df = final_df.append(year_pm_5, ignore_index=True)
final_df = final_df.append(year_pm_10, ignore_index=True)
final_df.index = ['5 year avg Ozone', '10 year avg Ozone', '5 year avg PM2.5', '10 year avg PM2.5']
final_df.to_csv('AQI_avgs.csv')

  
