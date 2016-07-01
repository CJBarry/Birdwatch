
# coding: utf-8

# In[7]:

# create class for birds


# In[99]:

import numpy as np
import matplotlib.pyplot as plt


# In[85]:

import pandas as pd


# In[100]:

# csv file format
# county, species, mean, rank, % gardens
# imported using pandas - good for large data


# In[135]:

data=pd.read_csv('West_Yorkshire_Birds_2015.csv',sep=',')


# In[132]:

#print(data.species)


# In[124]:

#class Birds(object):
    #def __init__(self,bird_name,mean):


# In[134]:

print(data.columns)


# In[136]:

print(data.rank_birds)


# In[139]:

get_ipython().magic('matplotlib inline')
plt.plot(data.mean_birds)


# In[ ]:



