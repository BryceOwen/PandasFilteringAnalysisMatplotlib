#!/usr/bin/env python
# coding: utf-8

# # Assignment 4: Pandas

# * Section: Sec01
#     
# * Name: Bryce Owen
#     
# * Due date:  29 February 2020
#     
# * Purpose:  Pandas data filtering and analysis with groupby, crosstab, pivot_table and matplot lib

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


wage = pd.read_csv('http://barney.gonzaga.edu/~chuang/data/wage.csv')


# In[3]:


wage.head()


# ## No groupby(), crosstab(), or pivot_table()

# In[23]:


#How many employees are in the Finance department?

wage[wage['Department'] == 'Finance'].count()[0]


# In[7]:


# What is the mean of working hours of employees in the Production department?  

round(wage[wage['Department'] == 'Production']['Hours'].mean(),2)


# In[22]:


# How many male employees are in the Sales department?

wage[(wage['Department'] == 'Sales') & (wage['Sex'] == 'Male')].count()[0]


# In[19]:


# What is the mean of weekly wages of female employees in the Marketing department?

wage = wage.assign(WeeklyWages = wage['BaseRate'] * wage['Hours'])
round(wage[(wage['Department'] == 'Marketing') & (wage['Sex'] == 'Female')]['WeeklyWages'].mean(),2)


# ## Groupby(), crosstab(), or pivot_table() allowed

# In[25]:


# What are the totals of weekly wages of female and male employees?

wage.groupby('Sex')[['WeeklyWages']].sum()    


# In[29]:


# What are the numbers of male and female employees in the Marketing, Production, and Human Resources Departments? 

wage_MPHR = wage[(wage['Department'] == 'Marketing') | (wage['Department'] == 'Production') | (wage['Department'] == 'Human Resources')]
pd.crosstab(index = wage_MPHR['Department'], columns = wage_MPHR['Sex'], values = wage_MPHR['LastName'], aggfunc = 'count')


# In[34]:


# What are the means of weekly wages of the Marketing, Production and Engineering departments?

wage_MPE = wage[(wage['Department'] == 'Marketing') | (wage['Department'] == 'Production') | (wage['Department'] == 'Engineering')]
wage_MPE.pivot_table(index = 'Department', values = 'WeeklyWages', aggfunc = 'mean')


# In[37]:


# What are the totals of weekly wages of male and female employees across departments using Pivot_table()?

wage.pivot_table(index = 'Department', columns = 'Sex', values = 'WeeklyWages', aggfunc = 'sum')


# # Matplotlib

# In[59]:


# How are mean wages different between females and males?  

mean_wages = wage['WeeklyWages'].groupby(wage['Sex']).mean()
x1 = mean_wages.index
y1 = mean_wages.values
plt.bar(x1, y1, align = 'center', color = 'red')


# In[57]:


# How are mean wages different between departments?  

mean_wages = wage['WeeklyWages'].groupby(wage['Department']).mean()
x1 = mean_wages.index
y1 = mean_wages.values
plt.barh(x1,y1, align = 'center', color = 'red')


# In[ ]:




