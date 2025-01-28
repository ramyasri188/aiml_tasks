#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


data.info()


# In[4]:


print(type(data))
print(data.shape)
print(data.size)


# In[5]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[6]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[7]:


data1[data1.duplicated(keep = False)]


# In[8]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[9]:


data1.rename({'solar.R': 'solar'},axis=1, inplace = True)
data1


# In[10]:


data1.info()


# In[11]:


#Dispaly data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[12]:


#visualize data1 missing values using heat map

cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[13]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of ozone: ", median_ozone)
print("Mean of ozone: ", mean_ozone)


# In[14]:


# Replace the ozone missing values with median values
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# ## 27/01/2025 Monday

# In[16]:


median_solar = data1["Solar.R"].median()
mean_solar = data1["Solar.R"].mean()
print("Median of solar.r: ", median_solar)
print("Mean of solar.r: ", mean_solar)


# In[17]:


data1['Solar.R'] = data1['Solar.R'].fillna(median_solar)
data1.isnull().sum()


# In[18]:


median_month = data1["Month"].median()
mean_month = data1["Month"].mean()
print("Median of month: ", median_month)
print("Mean of month: ", mean_month)


# In[19]:


data1["Month"] = data1["Month"].fillna(median_month)
data1.isnull().sum()


# In[20]:


# Find the mode values of categorical column (weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[21]:


# Impute missing values(Replace NaN with mode etc.) of "weather" using fillba()
data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[22]:


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

# In[25]:


sns.violinplot(data=data1["Ozone"], color='lightgreen')


# In[26]:


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


# In[27]:


sns.violinplot(data=data1["Solar.R"], color='lightgreen')


# ## 28/01/2025 Tuesday

# In[57]:


plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"], vert= False)


# In[59]:


plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data1["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# In[61]:


mu = data1["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]

for x in data1["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)
        


# ### Observations

# #### It is observed that only two outliers are identified using std method
# #### In box plot method more no of outliers are identified 
# #### This is because the assumption of normality is not satisfied in the column

# ## Quantile-Quantile plot for detection of outliers

# In[71]:


import scipy.stats as stats
plt.figure(figsize=(8,6))
stats.probplot(data1["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# #### Observations from Q-Q plot

# #### The data does not follow normal distribution as the data points are deviating significantly away from the red line
# #### The data shows a right-skewed distribution and possible outilers

# In[78]:


sns.violinplot(data=data1 ["Ozone"],color='lightgreen')
plt.title("Violin Plot")


# In[ ]:




