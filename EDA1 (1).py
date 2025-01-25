#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[37]:


data.info()


# In[39]:


print(type(data))
print(data.shape)
print(data.size)


# In[41]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[43]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[45]:


data1[data1.duplicated(keep = False)]


# In[47]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[49]:


data1.rename({'solar.R': 'solar'},axis=1, inplace = True)
data1


# In[51]:


data1.info()


# In[53]:


#Dispaly data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[59]:


#visualize data1 missing values using heat map

cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[63]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of ozone: ", median_ozone)
print("Mean of ozone: ", mean_ozone)


# In[69]:


# Replace the ozone missing values with median values
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[75]:


median_solar = data1["Solar.R"].median()
mean_solar = data1["Solar.R"].mean()
print("Median of solar.r: ", median_solar)
print("Mean of solar.r: ", mean_solar)


# In[77]:


data1['Solar.R'] = data1['Solar.R'].fillna(median_solar)
data1.isnull().sum()


# In[ ]:




