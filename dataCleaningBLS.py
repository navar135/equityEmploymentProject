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
uniVar = df['Category'].unique()
#make two subset dataframes that can be easily plotted
popNoDis =df[df['Category']==uniVar[0]]#population with no disability
popDis = df[df['Category']==uniVar[1]] #population with disability
#initial plots of our data 
#plot the populations
pop = plt.figure()
plt.plot(popNoDis['Year'],popNoDis['Value'], color ='maroon')
plt.plot(popDis['Year'],popDis['Value'], color ='blue')

plt.show()
 