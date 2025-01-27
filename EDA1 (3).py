#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[65]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[67]:


data.info()


# In[69]:


print(type(data))
print(data.shape)
print(data.size)


# In[71]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[73]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[75]:


data1[data1.duplicated(keep = False)]


# In[77]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[79]:


data1.rename({'solar.R': 'solar'},axis=1, inplace = True)
data1


# In[81]:


data1.info()


# In[83]:


#Dispaly data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[85]:


#visualize data1 missing values using heat map

cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[86]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of ozone: ", median_ozone)
print("Mean of ozone: ", mean_ozone)


# In[87]:


# Replace the ozone missing values with median values
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# ## 27/01/2025 Monday

# In[92]:


median_solar = data1["Solar.R"].median()
mean_solar = data1["Solar.R"].mean()
print("Median of solar.r: ", median_solar)
print("Mean of solar.r: ", mean_solar)


# In[94]:


data1['Solar.R'] = data1['Solar.R'].fillna(median_solar)
data1.isnull().sum()


# In[96]:


median_month = data1["Month"].median()
mean_month = data1["Month"].mean()
print("Median of month: ", median_month)
print("Mean of month: ", mean_month)


# In[98]:


data1["Month"] = data1["Month"].fillna(median_month)
data1.isnull().sum()


# In[100]:


# Find the mode values of categorical column (weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[102]:


# Impute missing values(Replace NaN with mode etc.) of "weather" using fillba()
data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[126]:


# create a figure with two subplots, stacked vertically
fig, axes=plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios':[1,3]})

# plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Ozone"], ax=axes[0], color='skyblue', width=0.5, orient='h')
axes[0].set_title('Boxplot')
axes[0].set_xlabel("Ozone Levels")

# plot the histogram with KDE curve in the second (bottom) subplot
sns.histplot(data1['Ozone'],kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")

# Adjust layout for better spacing
plt.tight_layout()

# showmthe plot
plt.show()


# # Observations

# ### The ozone column has extreme values beyond 81 as seen from box plot
# ### The same is confirmed from the below right_skewed histogram

# In[130]:


sns.violinplot(data=data1["Ozone"], color='lightgreen')


# In[135]:


# create a figure with two subplots, stacked vertically
fig, axes=plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios':[1,3]})

# plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Solar.R"], ax=axes[0], color='skyblue', width=0.5, orient='h')
axes[0].set_title('Boxplot')
axes[0].set_xlabel("Solar.R")

# plot the histogram with KDE curve in the second (bottom) subplot
sns.histplot(data1['Ozone'],kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Solar.R")
axes[1].set_ylabel("Frequency")

# Adjust layout for better spacing
plt.tight_layout()

# showmthe plot
plt.show()


# In[137]:


sns.violinplot(data=data1["Solar.R"], color='lightgreen')


# In[ ]:




