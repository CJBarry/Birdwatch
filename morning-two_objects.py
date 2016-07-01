
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

data = np.loadtxt(fname='data/temperature-01.csv',delimiter=',')


# In[3]:

type(data)


# In[40]:

data.min()


# #### class-capitalise to distinguish from variable

# In[41]:

class Student(object):
    
    def __init__(self, first_name, second_name):
        self.name = first_name + " " + second_name
        self.yr1_mark = None
        self.yr2_mark = None
        self.yr3_mark = None
        
    def classification(self):
        mean_mark = (self.yr2_mark + self.yr3_mark) / 2.0
        degree_class = "Unclassified"
        if mean_mark > 70.0:
            degree_class = "First"
        elif mean_mark > 60.0:
            degree_class = "Upper Second, 2:1"
        elif mean_mark > 50.0:
            degree_class = "Lower Second, Desmond 2:2"
        return degree_class


# In[42]:

student_1 = Student("Andrew", "Walker")


# In[43]:

print(student_1.name)


# In[44]:

student_1.yr1_mark = 64
student_1.yr2_mark = 64
student_1.yr3_mark = 52


# In[45]:

student_1.classification()


# In[46]:

print(student_1.yr1_mark)


# In[56]:

student_2 = Student("Oliver", "Sanford")
student_2.yr2_mark = 65
print("year 2 mark - ",student_2.name,": ",student_2.yr2_mark,"%, Classification: ",student_1.classification())

