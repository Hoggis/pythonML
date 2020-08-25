import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# set style
sns.set_style('whitegrid')
#load dataset
titanic = sns.load_dataset('titanic')

# see the data
titanic.head()

# create jointplot with fare and age
sns.jointplot(x='fare', y='age', data=titanic)

# distplot with fare in titanic
sns.distplot(titanic['fare'],kde=False,bins=30)

# boxplot with passenger class and age style with pallette
sns.boxplot(x="class", y="age",data=titanic, palette="coolwarm")

#same as previous but swarmplot
sns.swarmplot(x="class", y="age", data=titanic)

# count the number of people per gender
sns.countplot(x='sex',data=titanic)

# create a heatmap of titanic
sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')

# creates two separate histograms (male and female) sorted by age
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
