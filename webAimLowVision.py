#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code will make figures based on the data copied from the two surveys 
conducted by webAim in 2013 https://webaim.org/projects/lowvisionsurvey/ and 
in 2018 https://webaim.org/projects/lowvisionsurvey2/

It will also analyze raw data accessed from webAIM on the accessibility of the
the top sites
Created on Fri Jan 21 13:17:50 2022

@author: navar135
"""

#import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import base64
import os
import csv

os.chdir("/Users/navar135/Documents/GitHub/equityEmploymentProject/")#change this for your personal path (use pwd)
#import internetProficiency dataset 
df = pd.read_excel (r'webAimData/internetProficiency.xlsx')

#plot the data comparing the proficiency by year
p=sns.factorplot(x='proficiency', y='%ofRespondents', hue='year', kind='bar', data=df)
p.set(xlabel="Proficiency", ylabel = "% of Respondents", title = "Internet Proficiency",)
plt.gcf().set_size_inches(10, 7)
plt.show()

#import feelingOnWebAccess dataset
df2 = pd.read_excel (r'webAimData/feelingOnWebAccess.xlsx')
#plot the data comparing the proficiency by year
p=sns.factorplot(x='response', y='%ofRespondents', hue='year', kind='bar', data=df2)
p.set(xlabel="Response", ylabel = "% of Respondents", title = "Accessibility of Web Content ",)
p.set_xticklabels(['More Accessible','No Change', 'Less Accessible'])
plt.gcf().set_size_inches(10, 7)
plt.show()

#import raw data on web accessibility 
xls = pd.ExcelFile('webAimData/WebAIMMillionTopBottom1000.xlsx')
top1000 = pd.read_excel(xls, 'MillionTop1000')
bottom1000 = pd.read_excel(xls, 'MillionBottom1000')

#select the columns we care about 
top1000 = top1000[['rank','URL','TLD','accessrank','totalerrors','errordensity',
               'totalalerts','categories']]
bottom1000 = bottom1000[['rank','URL','TLD','accessrank','totalerrors','errordensity',
               'totalalerts','categories']]

shopTop1000 = top1000.loc[top1000['categories'].str.contains('IAB22', na=False)]
shopBottom1000 = bottom1000.loc[bottom1000['categories'].str.contains('IAB22', na=False)]


