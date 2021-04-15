import os
import pandas as pd 

combined_df = pd.read_csv('../Combined_Val.csv')
data_org_df = pd.read_csv('../LCS_Data_Org.csv')
ordering = list(data_org_df['Counties'].combine_first(data_org_df['Cities']))
columns = combined_df.columns

#split the combined dataframe
daymaxprecip = list(filter(lambda k: '_1dayMaxPrecip' in k, columns))
avgburned = list(filter(lambda k: '_AnnualAvgAreaBurned' in k, columns))
maxtemp = list(filter(lambda k: '_AnnualAvgMaxTemp' in k, columns))
precip = list(filter(lambda k: '_AnnualPrecip' in k, columns))
exheat = list(filter(lambda k: '_ExtremeHeatDays' in k, columns))
warm = list(filter(lambda k: '_WarmNights' in k, columns))

mprecdf = combined_df[daymaxprecip]
burndf = combined_df[avgburned]
tempdf = combined_df[maxtemp]
precipdf = combined_df[precip]
exheatdf = combined_df[exheat]
warmdf = combined_df[warm]


# rename the columns
mprecdf.columns = mprecdf.columns.str.replace('_1dayMaxPrecip','')
mprecdf.columns = mprecdf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')
burndf.columns = burndf.columns.str.replace('_AnnualAvgAreaBurned','')
burndf.columns = burndf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')
tempdf.columns = tempdf.columns.str.replace('_AnnualAvgMaxTemp','')
tempdf.columns = tempdf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')
precipdf.columns = precipdf.columns.str.replace('_AnnualPrecip','')
precipdf.columns = precipdf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')
exheatdf.columns = mprecdf.columns.str.replace('_ExtremeHeatDays','')
exheatdf.columns = mprecdf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')
warmdf.columns = mprecdf.columns.str.replace('_WarmNights','')
warmdf.columns = mprecdf.columns.str.replace(r'\b([A-Z]{1,2})([A-Z][a-z])', r'\1 \2')

# reorder the columns to reflect the proper order
mprecdf = mprecdf.reindex(columns=ordering)
burndf = burndf.reindex(columns=ordering)
tempdf = tempdf.reindex(columns=ordering)
precipdf = precipdf.reindex(columns=ordering)
exheatdf = exheatdf.reindex(columns=ordering)
warmdf = warmdf.reindex(columns=ordering)


final_df = mprecdf
final_df = final_df.append(tempdf, ignore_index=True)
final_df = final_df.append(precipdf, ignore_index=True)
final_df = final_df.append(exheatdf, ignore_index=True)
final_df = final_df.append(warmdf, ignore_index=True)
final_df = final_df.append(burndf, ignore_index=True)

# transpose dataframes so that juristiction is row
final_df = final_df.transpose()

final_df.columns = data_org_df.columns[2:]
final_df = final_df.rename(columns={"Projected Max Length of Dry Spell - Mid Century Change from Baseline High Emissions Scenario":
'Projected Average Max Temperature - Mid Century Change from Baseline High Emissions Scenario', 
'Modeled Baseline Max Length of Dry Spell': 'Modeled Baseline Average Max Temperature', 
'% change in max length of dry spell (change from baseline/baseline)':
'% Change in Average Max Temperature ((change from baseline)/baseline)'})
final_df.to_csv('../Local_Climate_Snapshot.csv')


