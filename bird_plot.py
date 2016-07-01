
# coding: utf-8

# In[8]:

# create class for birds


# In[9]:

import numpy as np
import matplotlib.pyplot as plt


# In[10]:

import pandas as pd


# In[11]:

# csv file format
# county, species, mean, rank, % gardens
# imported using pandas - good for large data


# In[46]:

data=pd.read_csv('West_Yorkshire_Birds_2015.csv',sep=',')


# In[47]:

#print(data.species)


# In[48]:

#class Birds(object):
    #def __init__(self,bird_name,mean):


# In[49]:

print(data.columns)


# In[50]:

my_xticks = [data.species]
plt.xticks(data.rank_birds, my_xticks)


# In[51]:

get_ipython().magic('matplotlib inline')
plt.plot(data.rank_birds,data.mean_birds)


# In[52]:

plt.pie(data.Percent_gardens)


# In[71]:


selected_values=data.mean_birds > 1.00
labels=data.species[selected_values]
mean_birds=data.mean_birds[selected_values]

def make_autopct(mean_birds):
    def my_autopct(pct):
        total = sum(data.mean_birds)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct

plt.pie(mean_birds,labels=labels)


# In[ ]:




# In[ ]:



