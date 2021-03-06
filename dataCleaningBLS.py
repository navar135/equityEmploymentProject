#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:16:03 2021

This script will clean the Bureau of labor statistics dataset 
It is being downloaded from https://beta.bls.gov/dataViewer/view/8557bf4914a64d34b80e947dda69a486
We selected which variables we wanted to downloaded and recoded the series id for the name of the variable
@author: Karen T Navarro 
@contributors: Nicole Neequaye, Magical Sparkles, and Adedolapo Aishat Toye 
"""
#import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import base64
import os
import csv

#gchange path to be where your folder is in 
os.chdir("/Users/navar135/Documents/GitHub/equityEmploymentProject/")#change this for your personal path (use pwd)
#import dataset 
with open('rawData/StatBureau/statBureau_raw.csv') as f:
    df=pd.read_csv(f, delimiter=',')
#import recoded names as a dictionary
with open('rawData/StatBureau/seriesIDrenamed.csv', mode='r') as inp:
    reader = csv.reader(inp)
    idDict= {rows[0]:rows[1] for rows in reader}
#delete the headingin the dictionary
del idDict['Series ID']
#create an empty list
category = [0]*len(df)
#for every series id add to our list the name of that series
for i in range(len(df)): 
    if df['Series ID'][i] in idDict.keys(): 
        category[i] = idDict[df['Series ID'][i]]
#add the completed list as a column in our dataframe
df['Category']=category 
#find all the unique categories so we can plot them
uniVar = list(df['Category'].unique())
#remove dataset without a pair 
df =df[df['Category']!=uniVar[6]]#Employed - With a disability, Men
df =df[df['Category']!=uniVar[9]]
df =df[df['Category']!=uniVar[10]]
df =df[df['Category']!=uniVar[15]]
df =df[df['Category']!=uniVar[16]]
uniVar = list(df['Category'].unique())


#initial plots of our data 
#plot the populations
for i in range(len(uniVar)):
    if i%2==0:
        noDis =df[df['Category']==uniVar[i]]#population with no disability
        dis = df[df['Category']==uniVar[i+1]] #population with disability
        pop = plt.figure()
        plt.plot(noDis['Year'],noDis['Value'], color ='maroon', label =uniVar[i])
        plt.plot(dis['Year'],dis['Value'], color ='blue', label =uniVar[i+1])
        plt.legend()
        label = uniVar[i]+ ' vs. '+ uniVar[i+1]
        plt.title(label)
        plt.show()
#average across years
avgVal= df.groupby(['Category','Year']).mean()
avgVal.reset_index(inplace=True)
popNoDis = avgVal[avgVal['Category']==uniVar[0]].reset_index()
popDis = avgVal[avgVal['Category']==uniVar[1]].reset_index()

for i in range(2,len(uniVar)):
    if i%2==0:
        #find the ratefor each category 
        noDis =avgVal[avgVal['Category']==uniVar[i]].reset_index()#population with no disability
        dis = avgVal[avgVal['Category']==uniVar[i+1]].reset_index() #population with disability
        noDis['Population'] = popNoDis['Value']
        noDis['Rate']=noDis['Value']/noDis['Population'] 
        dis['Population'] = popDis['Value']
        dis['Rate']=dis['Value']/noDis['Population'] 
        #plot the rates for each category as a bar chart
        plotdf = pd.concat([noDis, dis], axis=0, ignore_index=False)
        #sns.set(font_scale = 0.05)
        p = sns.factorplot(x='Category', y='Rate', hue='Category', kind='bar', data=plotdf)
        p.set_xticklabels(['No Disability','Disability'])
        plt.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5), borderaxespad=0)
   