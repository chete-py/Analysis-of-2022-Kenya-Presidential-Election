#!/usr/bin/env python
# coding: utf-8

# In[454]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[455]:


df = pd.read_excel("COLLINS PROJECT.xlsx")
df.head()


# In[456]:


df.columns


# In[457]:


newdf = df[['COUNTY','RAILA', 'RUTO', 'MWAURE','WAJACKOYA', 'TOTAL VALID VOTES']]
newdf.dropna()
newdf.head()


# In[458]:


ammended_df = newdf.assign(RAILA_PERCENT =newdf['RAILA']/newdf['TOTAL VALID VOTES']*100, RUTO_PERCENT =newdf['RUTO']/newdf['TOTAL VALID VOTES']*100, MWAURE_PERCENT =newdf['MWAURE']/newdf['TOTAL VALID VOTES']*100, WAJACKOYA_PERCENT =newdf['WAJACKOYA']/newdf['TOTAL VALID VOTES']*100)


# In[459]:


ammended_df.head()


# In[460]:


ammended_df.columns


# In[461]:


candidate_percentage = ammended_df[['COUNTY','RAILA_PERCENT', 'RUTO_PERCENT', 'MWAURE_PERCENT', 'WAJACKOYA_PERCENT']]


# In[462]:


round(candidate_percentage, 2).head()


# In[463]:


labels = 'RAILA_PERCENT', 'RUTO_PERCENT', 'MWAURE_PERCENT', 'WAJACKOYA_PERCENT'
sizes  = [48.85, 50.49, 0.23, 0.44]
explode = (0, 0.05, 0.5, 0.5)
plt.figure(figsize=(20,20))
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,autopct='%1.1f%%')
plt.legend(labels, loc="center left", prop={'size': 8})
plt.show()


# In[464]:


newdf.loc[50,"RAILA":"WAJACKOYA"]


# In[465]:


def addlabels(xvalue,yvalue):
    for i in range(len(xvalue)):
        plt.text(i,yvalue[i], yvalue[i], ha = "center")

if __name__ == '__main__':
    fig = plt.figure(figsize=(8,4), dpi = 100)
    xvalue = ['RAILA', 'RUTO', 'MWAURE', 'WAJACKOYA']
    yvalue = [6942930, 7179091, 31987, 61969]
    c = ['blue', 'yellow', 'red', 'green']
    plt.bar(xvalue, yvalue, color = c , width = 0.4)
    addlabels(xvalue,yvalue)
    plt.ylim(0, 8000000)
    plt.title("Total valid vote distribution", fontsize = 15)
    plt.ylabel("Votes in millions", fontsize = 10)
    plt.show()


# In[453]:


top_two_aspirants = candidate_percentage.dropna()
top_two_candidates = top_two_aspirants.drop(index = 50)
top_two_candidates[['COUNTY','RAILA_PERCENT', 'RUTO_PERCENT']]
top_two_candidates.head()


# In[441]:


candidate_1 = np.array(top_two_candidates['RAILA_PERCENT'])
candidate_2 = np.array(top_two_candidates['RUTO_PERCENT'])
cand_1 = candidate_1.tolist()
cand_2 = candidate_2.tolist()
county_name = (top_two_candidates['COUNTY'])


# In[442]:


index = top_two_candidates.index
index


# In[449]:


fig = plt.figure(figsize=(25,10), dpi = 200) 
X_axis = np.arange(len(county_name))
plt.bar(X_axis - 0.1, cand_1 , width = 0.7, label = "RAILA")
plt.bar(X_axis + 0.1, cand_2 , width = 0.7,  label = "RUTO")
plt.legend()
plt.ylabel('percentage votes', fontsize = 20)
plt.title("Kenya Presidential Election Tallying Per County")
plt.xticks(index, county_name, rotation = "vertical")
plt.show()


# In[450]:


list = []
for items in cand_1:
    if items > 25:
        list.append(items)
        cand_1_over_25 = len(list)
        
list_1 = []
for items in cand_1:
    if items > 50:
        list_1.append(items)
        cand_1_over_50 = len(list_1)
        
list_2 = []        
for items in cand_1:
    if items > 75:
        list_2.append(items)
        cand_1_over_75 = len(list_2)  
        
list_3 = []
for items in cand_2:
    if items > 25:
        list_3.append(items)
        cand_2_over_25 = len(list_3)
        
list_4 = []
for items in cand_2:
    if items > 50:
        list_4.append(items)
        cand_2_over_50 = len(list_4)
        
list_5 = []        
for items in cand_2:
    if items > 75:
        list_5.append(items)
        cand_2_over_75 = len(list_5)


# In[451]:


percentage = ['25%', '50%', '75%']
cand_1_tally = [cand_1_over_25, cand_1_over_50, cand_1_over_75]
cand_2_tally = [cand_2_over_25,cand_2_over_50, cand_2_over_75]
labels_1 = ['over_25%', 'over_50%', 'over_75%']


# In[452]:


fig = plt.figure(figsize=(20,10), dpi = 200) 
X_axis = np.arange(len(percentage))
plt.bar(X_axis - 0.2, cand_1_tally , width = 0.4, label = "RAILA")
plt.bar(X_axis + 0.2, cand_2_tally , width = 0.4,  label = "RUTO")
plt.legend()
plt.ylabel('Number of counties', fontsize = 15)
plt.title("Comparison of % of votes in counties")
plt.xticks([0,1,2], labels_1)
plt.show()


# In[ ]:




