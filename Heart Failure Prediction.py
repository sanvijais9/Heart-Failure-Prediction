#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[8]:


data = pd.read_csv("C:\\Users\\shashi\\Desktop\\python project\\heart failure.csv")
data.head()


# In[9]:


#describing the data
data.describe()


# In[10]:


#Exploratory data analysis


len_live = len(data['DEATH_EVENT'][data['DEATH_EVENT'] == 0])
len_death = len(data['DEATH_EVENT'][data['DEATH_EVENT'] == 1])

arr = np.array([len_live, len_death])
labels = ['LIVING','DIED']

print(f'Total number of Living case:- {len_live}')
print(f'Total number of Death case:- {len_death}')

plt.pie(arr, labels = labels, explode=[0.2,0.0], shadow = True)
plt.show()


# In[11]:


##Seeing the distribution of age


sns.distplot(data['age'])


# In[28]:


## Selecting columns that are above age 50 and seeing died or not


age_above_50_not_died = data['DEATH_EVENT'][data.age >=50][data.DEATH_EVENT == 0]
age_above_50_died = data['DEATH_EVENT'][data.age >= 50][data.DEATH_EVENT == 1]

len_died = len(age_above_50_died)
len_not_died = len(age_above_50_not_died)

arr1 = np.array([len_died, len_not_died])
labels =['DIED','NOT DIED']

print(f'Total number of Died:- {len_died}')
print(f'Total number of Not Died:- {len_not_died}')

plt.pie(arr1, labels=labels, explode = [0.2, 0.0], shadow= True)
plt.show()


# In[29]:


patient_nhave_diabetes_0 = data['DEATH_EVENT'][data.diabetes == 0][data.DEATH_EVENT ==0]
patient_have_diabetes_1 = data['DEATH_EVENT'][data.diabetes == 1][data.DEATH_EVENT == 1]

len_d_died = len(patient_have_diabetes_1)
len_d_alive = len(patient_nhave_diabetes_0)

arr2 = np.array([len_d_died, len_d_alive])
labels = ['Died with diabetes', 'Not died with diabetes']

print(f'Total number of Died with diabetes:- {len_d_died}')
print(f'Total number of Not died with diabetes: {len_d_alive}')

plt.pie(arr2, labels=labels, explode = [0.2,0.0], shadow = True)
plt.show()


# In[35]:


##Checking correlation of our variables
##  -1 indicates a perfectly negative linear correlation between two variables
##  0 indicates no linear correlation between two variables
##  1 indicates a perfectly positive linear correlation between two variables

corr = data.corr()
plt.subplots(figsize=(15,10))
sns.heatmap(corr, annot=True)


# In[4]:


data.corr().style.background_gradient(cmap='coolwarm')


# In[ ]:





# In[ ]:




