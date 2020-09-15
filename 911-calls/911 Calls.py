
# For this capstone project we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:

#imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read in file and store in df
df = pd.read_csv("911.csv")

#check df
df.info()

#head of df
df.head(3)


#top 5 zipcodes for 911 calls
df['zip'].value_counts().head(5)


# top 5 townships

df['twp'].value_counts().head(5)


#unique number of titles
df['title'].nunique()

#create column reason that takes title and splits it
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


#find most common reason
df['Reason'].value_counts()


#countplot of reason
sns.countplot(x='Reason',data=df)

#data type of objects in timestamp
type(df['timeStamp'].iloc[0])

#convert timestamp from string to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])





#get hour month and day of week from datetime
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


#map day of the week to letters
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

#count plot of the day of week column with reason as hue
sns.countplot(x='Day of Week', data = df, hue= 'Reason')
#move legend to the side
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#same for month
sns.countplot(x='Month',data=df,hue='Reason')

#groupby month
byMonth = df.groupby('Month').count()
byMonth.head()

#how many calls per month
# Could be any column
byMonth['twp'].plot()

#linear fit of the number of calls per month
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


#get date from timestamp
df['Date']=df['timeStamp'].apply(lambda t: t.date())


#plot counts for date 
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

#same but create 3 different plots depending on reason
#traffic
df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
#fire
df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
#ems
df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()

#restructure hours to columns and index is day of the week  
dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()

#heatmap for dayHour
plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='inferno')

#clustermap
sns.clustermap(dayHour,cmap='inferno')

#same but month as column
dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()
#heatmap
plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='inferno')
#clustermap
sns.clustermap(dayMonth,cmap='inferno')

