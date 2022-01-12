#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


# In[2]:


#reading the data file
df = pd.read_csv("Downloads/csv_pus/psam_pusa.csv") 


# In[3]:


df.info() #obtaining basic information about the data


# In[4]:


df.columns #getting an overview of the columns in the data


# In[5]:


df.shape #an idea of the shape of the data which shows the rows and columns


# In[6]:


df.sample(5) #gives a random sample of the data


# In[7]:


def remove_housing_RT(df):
    """
    removes all rows that consis of the value H in the column RT
    Arguments:
    'df': A pandas DataFrame
    Outputs
    'df': A pandas DataFrame containing only the person record types
    """
    df['RT'] = df['RT'].str.strip()
    df_P_copy = df[df.RT != ("H")]
    df = df_P_copy
    return df


# In[8]:


remove_housing_RT(df).sample(5)


# In[9]:


len(df)


# In[10]:


Var_of_int = df.loc[:, ["REGION","DIVISION", "ST", "AGEP", "COW", "DEYE", "NWAV", "NWLA", "NWLK", "SCH", "SCHG", "SCHL", 
           "SEX", "WKL", "DIS", "ESR", "FOD1P", "FOD2P", "HICOV", "INDP", "NAICSP", "OCCP", "PERNP", "PINCP",
          "POWSP", "RAC1P", "RAC2P", "RAC3P", "RACAIAN", "RACASN", "RACBLK", "RACWHT", "SCIENGP", "SCIENGRLP",
          "SOCP", "FDEYEP", "PWGTP1" ]]


# In[11]:


type(Var_of_int)


# In[12]:


Var_of_int.shape


# In[13]:


Var_of_int.sample(5)


# In[14]:


Var_of_int.info()


# In[15]:


Var_of_int.describe(include=object)


# In[16]:


Var_of_int.describe()


# In[18]:


grouped = Var_of_int.groupby(['ST', 'DEYE']).size()
print(grouped)


# In[19]:


Var_of_int["DEYE"].value_counts()


# In[20]:


deye = {1: 'yes', 2:'no'}
Var_of_int["DEYE"] = Var_of_int["DEYE"].map(deye) 


# In[21]:


Var_of_int.head()


# In[22]:


Var_of_int['DEYE'].value_counts()


# In[23]:


Var_of_int["ST"].value_counts()


# In[24]:


st = {1: 'Alabama', 2: 'Alaska', 4: 'Arizona', 5: 'Arkansas', 6: 'California', 8: 'Colorado', 9: 'Connecticut',
      10: 'Delaware', 11: 'District of Columbia', 12: 'Florida', 13: 'Georgia', 15: 'Hawaii', 16: 'Idaho', 17: 'Illinois',
      18: 'Indiana', 19: 'Iowa', 20: 'Kansas', 21: 'Kentucky', 22: 'Louisiana', 23: 'Maine', 24: 'Maryland', 
      25: 'Massachusetts', 26: 'Michigan', 27: 'Minnesota', 28: 'Mississippi', 29: 'Missouri', 30: 'Montana', 31: 'Nebraska',
      32: 'Nevada', 33: 'New Hampshire', 34: 'New Jersey', 35: 'New Mexico', 36: 'New York', 37: 'North Carolina',
      38: 'North Dakota', 39: 'Ohio', 40: 'Oklahoma', 41: 'Oregon', 42: 'Pennsylvania', 44: 'Rhode Island',45: 'South Carolina',
      46: 'South Dakota', 47: 'Tennessee', 48: 'Texas', 49: 'Utah', 50: 'Vermont', 51: 'Virginia', 53: 'Washington',
      54: 'West Virginia', 55: 'Wisconsin', 56: 'Wyoming', 72: 'Puerto Rico'}

Var_of_int["ST"] = Var_of_int["ST"].map(st) 


# In[25]:


Var_of_int["ST"].value_counts()


# In[26]:


region = {1: 'Northeast', 2: 'Midwest', 3: 'South', 4: 'West', 9: 'Puerto Rico'}
Var_of_int["REGION"] = Var_of_int["REGION"].map(region)


# In[27]:


Var_of_int["REGION"].value_counts()


# In[28]:


state_dis = Var_of_int.groupby(Var_of_int["ST"]).size()

#plt
#Var_of_int.plot.bar(x=["ST"], rot=0, color ='r')
#plt.title('State distribution ')
#plt.ylabel('States')


# In[29]:


state_dis.plot.bar(x=["ST"], color = 'r')


# In[46]:


agep = Var_of_int.groupby(Var_of_int["AGEP"]).size()
print(agep)


# In[52]:





# In[ ]:




