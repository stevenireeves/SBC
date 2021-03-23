import numpy as np
import pandas as pd
import os

# Compute the total, 10-year, and 5-year averages for the Sierra Region for Annual Precipitation

PATH='/home/steven/SBC/Precip/Sierra_Annual_Precip/'
OUTPATH='/home/steven/SBC/Precip/'


data = os.listdir(PATH)
avg_5     = {}
avg_10    = {}
avg_total = {}
for i in range(len(data)):
  #load in Precip data
  print('Processing File ', data[i])
  df = pd.read_csv(PATH+data[i])
  name = data[i][:-11]
  avg_total[name] = df[df['label']=='Observed']['average'].mean()
  avg_10[name]    = df[df['label']=='Observed']['average'][-10:].mean()
  avg_5[name]     = df[df['label']=='Observed']['average'][-5:].mean()
  

final_df = pd.DataFrame(avg_total, index=[0])
final_df = final_df.append(avg_10, ignore_index=True)
final_df = final_df.append(avg_5, ignore_index=True)
final_df.index = ['Total Observed Avg', 'Last 10 Years Avg', 'Last 5 Years Avg']
final_df.to_csv('Precip_avgs.csv')

  
