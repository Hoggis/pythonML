
import pandas as pd


#import dataframe
df = pd.read_csv("Salaries.csv")


#check to see what is in df
df.info()

#mean of BasePay
df['BasePay'].mean()
#average of BasePay
df['BasePay'].sum()/df['BasePay'].count()

#max of OvertimePay
df['OvertimePay'].max()


#Job titel of JOSEPH DRISCOLL
df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


#TotalPayBenefits of JOSEPH DRISCOLL
df[df['EmployeeName']=="JOSEPH DRISCOLL"]['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**
#Rows handling max and min work for both
#Max TotalPayBenefits
df.loc[df['TotalPayBenefits'].idxmax()]


#Min TotalPayBenefits remove comment from end of row to return only name
df[df['TotalPayBenefits']== df['TotalPayBenefits'].min()] #['EmployeeName']


#Mean of BasePay for each year
df.groupby('Year').mean()['BasePay']


#Count of unique job titles
df['JobTitle'].nunique()

#5 most common jobs
df['JobTitle'].value_counts().head(5)


#sum of job titles with only single entry
sum(df[df['Year']==2013]['JobTitle'].value_counts() == 1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# number of people that have the word chief in their name
def findChief(text):
    if 'chief' in text.lower().split():
        return True
    else:
        return False


sum(df['JobTitle'].apply(lambda x: findChief(x)))
