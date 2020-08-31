
import pandas as pd
import matplotlib.pyplot as plt
#read in data
df3 = pd.read_csv('df3')
#check the head of dataframe
df3.head()


#plot scatter
df3.plot.scatter(x='a',y='b',c='red',s=50,figsize=(12,3))


#histogram of column 'a'
df3['a'].plot.hist()

#add styling
plt.style.use('ggplot')


df3['a'].plot.hist(alpha=0.5,bins=25)

#box plot comparing columns a and b
df3[['a','b']].plot.box()

#plot the KDE for column D
df3['d'].plot.kde()
#adjusting line with and style
df3['d'].plot.density(lw=5,ls='--')

#area plot for rows until 30
df3.ix[0:30].plot.area(alpha=0.4)

#switch legend to the side of the plot
f = plt.figure()
df3.ix[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
