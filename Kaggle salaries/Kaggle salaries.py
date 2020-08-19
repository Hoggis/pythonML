#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[2]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[3]:


df = pd.read_csv("Salaries.csv")


# ** Check the head of the DataFrame. **

# In[4]:


df


# ** Use the .info() method to find out how many entries there are.**

# In[5]:


df.info()


# **What is the average BasePay ?**

# In[6]:


df['BasePay'].mean()


# In[7]:


df['BasePay'].sum()/df['BasePay'].count()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


df['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[9]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[10]:


df[df['EmployeeName']=="JOSEPH DRISCOLL"]['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[18]:


#df loc ja df[df[]] rivit toimivat molemmat sekä min että max funktioille
df.loc[df['TotalPayBenefits'].idxmax()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[19]:


df[df['TotalPayBenefits']== df['TotalPayBenefits'].min()] #['EmployeeName']


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[20]:


df.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[21]:


df['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[22]:


df['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[23]:


sum(df[df['Year']==2013]['JobTitle'].value_counts() == 1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[26]:


def findChief(text):
    if 'chief' in text.lower().split():
        return True
    else:
        return False


# In[27]:


sum(df['JobTitle'].apply(lambda x: findChief(x)))


# In[62]:


cdf = df['JobTitle'].apply(lambda x: findChief(x))


# In[63]:


cdf


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[64]:


df['title_len'] = df['JobTitle'].apply(len)


# In[65]:


df[['title_len','TotalPayBenefits']].corr() 


# # Great Job!
