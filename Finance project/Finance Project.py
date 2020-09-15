from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import plotly
import cufflinks as cf
import matplotlib.pyplot as plt


#set style
sns.set_style('whitegrid')


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


#Bank of america
BAC = data.DataReader('BAC', 'yahoo', start, end)
#CitiGroup
C = data.DataReader('C', 'yahoo', start, end)
#Goldman Sachs
GS = data.DataReader('GS', 'yahoo', start, end)
#JPMorgan Chase
JPM = data.DataReader('JPM', 'yahoo', start, end)
#Morgan Stanley
MS = data.DataReader('MS', 'yahoo', start, end)
#Wells Fargo
WFC = data.DataReader('WFC', 'yahoo', start, end)




#list of ticker symbols
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


#concatenate bank dataframes together
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)


#set levels for column names
bank_stocks.columns.names = ['Bank Ticker','Stock Info']


#Max close price for each bank's stock for data available
bank_stocks.xs(key='Close', axis = 1, level = 'Stock Info').max()


#create dataframe returns
returns = pd.DataFrame()



#calculate pct_change() for each of the tickers and set is in returns
for tick in tickers:
    returns[tick+'Return']= bank_stocks[tick]['Close'].pct_change()

#check data
returns.head()


#create pairplot of returns
#you must put [1:0], since first row is NaN
sns.pairplot(returns[1:])

#worst single day return
returns.idxmin()

#max single day return
returns.idxmax()


#standard deviation for returns
returns.std()

#std for 2015
returns.loc['2015-01-01':'2015-12-31'].std()



#distplot for morgan stanley returns in 2015
sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MSReturn'])


#distplot for CitiGroup in 2008
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['CReturn'])




# Optional Plotly Method Imports

cf.go_offline()


# ** Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) to get a cross section of the data.)**

#line plot for close price for each bank using for loop
for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick, figsize = (15,5))
plt.legend()


#same as previous, but with cross section
bank_stocks.xs(key ='Close', axis = 1, level = 'Stock Info').plot()


#same as previous, but with cufflinks
bank_stocks.xs(key ='Close', axis = 1, level = 'Stock Info').iplot()


# plots 30 day rolling average against the close price for BAC's stock in 2008
plt.figure(figsize = (15,5))
BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label = '30 day moving average')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC Close')
plt.legend()


#creates heatmap of correlation between stocks close price
sns.heatmap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)

#same but with clustermap
sns.clustermap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)

#set previous into variable closeCorr
closeCorr = bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr()

#generate heatmap
closeCorr.iplot(kind = 'heatmap')

#candle plot of BAC's stock in 2015
bacDataFor2015 = BAC[['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01']
bacDataFor2015.iplot(kind = 'candle')

#Simple Moving Averages (SMA) for Morgan Stanley in 2015
MS['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study = 'sma', periods = [13,21,55])

#Bollinger Band Plot (boll) for BAC's in 2015 
BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')
