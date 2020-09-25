import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#read in data
ecomCust_df = pd.read_csv('Ecommerce Customers')


#basic checks
ecomCust_df.head()
ecomCust_df.info()
ecomCust_df.describe()


#three jointplots with different axis
sns.jointplot(ecomCust_df['Time on Website'], ecomCust_df['Yearly Amount Spent'])

sns.jointplot(ecomCust_df['Time on App'], ecomCust_df['Yearly Amount Spent'])

sns.jointplot(ecomCust_df['Time on Website'], ecomCust_df['Length of Membership'], kind = "hex" )
#create pairplot
sns.pairplot(ecomCust_df)

#length of membership and yearly amount spent seem to be the most correlated

sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data =ecomCust_df )
#check columns of ecomCust_df for split
ecomCust_df.columns

from sklearn.model_selection import train_test_split
X = ecomCust_df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = ecomCust_df['Yearly Amount Spent']

#split data according to X and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


from sklearn.linear_model import LinearRegression


#instantiate Linear Regression model
lm = LinearRegression()


# fit the model
lm.fit(X_train,y_train)

#print out coefficients
print(lm.coef_)


# create predictions based on X_test
predictions = lm.predict(X_test)


# Create scatterplot with real test values and predicted values
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')


from sklearn import metrics


#MAE MSA and RMSE
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


#check for residuals if residuals (y_test minus the predictions) are normally distributed then the model is good
sns.distplot((y_test-predictions),bins=50)


# ## Conclusion
# We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important.  Let's see if we can interpret the coefficients at all to get an idea.
# 
# ** Recreate the dataframe below. **

# In[56]:

#print out coeffs 
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df


# ** How can you interpret these coefficients? **

#An increase of an unit increases the other attributes by the amount of the coefficient

# **Do you think the company should focus more on their mobile app or on their website?**

# They should invest in the app and also strive to retain their customers as it provides the greatest
# increase in revenue