import pandas as pd

#The data for this excercise has been created at random.
#The ideas for this data exploration are from a Udemy course.
#More information from the README

ecom = pd.read_csv('Ecommerce Purchases')
ecom.head(2)

#Basic exploration
#Rows
ecom.info()
# Mean purchase price
ecom['Purchase Price'].mean()
#max
ecom['Purchase Price'].max()
#min
ecom['Purchase Price'].min()


#Count of people who have selected english as their language
ecom[ecom['Language']=='en'].count()

#Count of people who are lawyers
ecom[ecom['Job']=='Lawyer'].count()

#Check how many purchases were made AM and PM
ecom['AM or PM'].value_counts()

#Five most common job titles
ecom['Job'].value_counts().head(5)


#Purchase price made from Lot "90 WT"
ecom[ecom['Lot']=="90 WT"]['Purchase Price']

#Email address of the person with CC num 4926535242672853
ecom[ecom['Credit Card']== 4926535242672853]['Email']

## CC Provider is American Express and Purchase made is over 95$
sum(ecom[ecom['CC Provider']=='American Express']['Purchase Price']>95)

#How many people have a credit card expiring 2025

def exp2025(ccexp):
    #25 has to be in "" or it will be int and slice wont work
    if ccexp[-2:] == "25":
        return True
    else:
        return False

#intermediate result
ecom['CC Exp Date'].apply(exp2025)

#the final sum, what the question asks
sum(ecom['CC Exp Date'].apply(lambda x: exp2025(x)))

#most common email domains from data
def domainGet(email):
    return email.split('@')[-1]

ecom['Email'].apply(lambda x: domainGet(x)).value_counts().head(5)