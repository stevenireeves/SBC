import numpy as np
import pandas as pd
import os

# Compute the total, 10-year, and 5-year averages for the Sierra Region warm nights

PATH='/home/steven/SBC/warm_nights/warm_nights_data/'
OUTPATH='/home/steven/SBC/warm_nights/'  

data = os.listdir(PATH)
data = sorted(data)
avg_total      = {}
avg_5          = {}
avg_10         = {}

for i in range(len(data)):
  #load in Precip data
  print('Processing File ', data[i])
  df = pd.read_csv(PATH+data[i])
  df['date'] = df['date'].apply(lambda x: x[11:15]) #gets year only 
  name = data[i][:-4].replace('_',' ')
  count = df.groupby(['date']).size()
  avg_5[name]    = count[:-5].mean()
  avg_10[name]      = count[:-10].mean()
  avg_total[name]     = count.mean()

final_df = pd.DataFrame(avg_total, index=[0])
final_df = final_df.append(avg_10, ignore_index=True)
final_df = final_df.append(avg_5, ignore_index=True)
final_df.index = ['Total Average Warm Nights per Year (Day/Yr)',
                  'Last 10 Years Average Warm Nights per Year (Day/Yr)', 
                  'Last 5 Years Average Warm Nights per Year (Day/Yr)']
final_df.to_csv(OUTPATH + 'warm_nights_avgs.csv')

  
