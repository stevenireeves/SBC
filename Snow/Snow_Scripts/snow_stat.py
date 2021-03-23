import numpy as np
import pandas as pd
import os

# Compute the total, 10-year, and 5-year averages for the Sierra Region for Annual Precipitation

PATH='/home/steven/SBC/Snow/Snow_Data/'
OUTPATH='/home/steven/SBC/Snow/'

  

data = os.listdir(PATH)
avg_5_depth        = {}
avg_5_swe          = {}
avg_5_dens         = {}
avg_total_depth    = {}
avg_total_swe      = {}
avg_total_dens     = {}
recording_stations = {}

for i in range(len(data)):
  #load in Precip data
  print('Processing File ', data[i])
  df = pd.read_csv(PATH+data[i])
  name = data[i][:-4].replace('_',' ')
  avg_total_depth[name]    = df['Snow Depth (in)'].mean()
  avg_total_swe[name]      = df['Snow Water Equivalent (in)'].mean()
  avg_total_dens[name]     = df['Snow Density (pct)'].mean()
  avg_5_depth[name]        = df[(2013 <= df['Water Year']) & (df['Water Year'] >= 2018)]['Snow Depth (in)'].mean()
  avg_5_swe[name]          = df[(2013 <= df['Water Year']) & (df['Water Year'] >= 2018)]['Snow Water Equivalent (in)'].mean()
  avg_5_dens[name]         = df[(2013 <= df['Water Year']) & (df['Water Year'] >= 2018)]['Snow Density (pct)'].mean()
  recording_stations[name] = len(df['Station Name'].unique())  

final_df = pd.DataFrame(avg_total_depth, index=[0])
final_df = final_df.append(avg_total_swe, ignore_index=True)
final_df = final_df.append(avg_total_dens, ignore_index=True)
final_df = final_df.append(avg_5_depth, ignore_index=True)
final_df = final_df.append(avg_5_swe, ignore_index=True)
final_df = final_df.append(avg_5_dens, ignore_index=True)
final_df = final_df.append(recording_stations, ignore_index=True)
final_df.index = ['Total Average Snow Depth (in)',
                  'Total Average Snow Water Equivalent (in)', 
                  'Total Average Snow Density (pct)',
                  'Last 5 Years Average Snow Depth (in)', 
                  'Last 5 Years Average Snow Water Equivalent (in)', 
                  'Last 5 Years Average Snow Density (pct)',
                  'Number of Recording Stations in County']
final_df.to_csv(OUTPATH + 'Snow_Avgs.csv')

  
