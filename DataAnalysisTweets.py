import pandas as pd
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter

data = pd.read_csv('secondresult_clean.csv', sep=';')
print(data)
group_tweet = data.groupby(['_unit_id','date'])['how_would_you_categorize_this_tweet'].mean().reset_index()
group_polarity = data.groupby(['_unit_id','date'])['polarity'].mean().reset_index()
group_google = data.groupby(['_unit_id','date'])['score_google'].mean().reset_index()



#groupday = data.groupby(['date'])['mean'].mean()
group_per_day_tweet = data.groupby(['date'])['how_would_you_categorize_this_tweet'].mean().reset_index()
group_per_day_polarity = data.groupby(['date'])['polarity'].mean().reset_index()

group_per_day_google = data.groupby(['date'])['score_google'].mean().reset_index()

result = pd.merge(group_per_day_tweet, group_per_day_polarity, on='date', how='inner')
result2 = pd.merge(result, group_per_day_google, on='date', how='inner')
print(result2)

writer = pd.ExcelWriter('FinalResults.xlsx', engine='xlsxwriter')
result2.to_excel(writer, sheet_name='Sheet1')
writer.save()