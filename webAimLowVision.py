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
xls = pd.ExcelFile('webAimData/WebAIMMillionTopBottom50000.xlsx')
top = pd.read_excel(xls, 'MillionTop50000')
bottom = pd.read_excel(xls, 'MillionBottom50000')
allDat=pd.concat([top,bottom]).reset_index()
allDat=allDat.drop(columns=['index'])


#select the columns we care about 
top = top[['rank','URL','TLD','accessrank','totalerrors','errordensity',
               'categories']]
bottom = bottom[['rank','URL','TLD','accessrank','totalerrors','errordensity',
               'categories']]
#select the data categorized for shopping
shopTop = top.loc[top['categories'].str.contains('IAB22', na=False)]
shopBottom = bottom.loc[bottom['categories'].str.contains('IAB22', na=False)]
#select all other data for comparisons
otherTop = top.loc[~top['categories'].str.contains('IAB22', na=False)]
otherBottom = bottom.loc[~bottom['categories'].str.contains('IAB22', na=False)]

#combine into one df 
shop = pd.concat([shopTop,shopBottom]).reset_index()
#calculate average accessibility rank by site popularity
print(shopTop['accessrank'].mean())
print(shopBottom['accessrank'].mean())
print(shop['accessrank'].mean())
print(otherTop['accessrank'].mean())
print(otherBottom['accessrank'].mean())
###mean for for the other categories is lower than for shopping so shopping 
###sites are on average less accessible could do some stats to see if this difference is significant

#scatter plot of popularity vs accessibility scores
p=sns.lmplot(x='accessrank',y='rank',data=shopTop,fit_reg=True)
p.set(xlabel='Accessibility ranking', ylabel='Popularity rank',title = 'Top Shopping Sites')
p2=sns.lmplot(x='accessrank',y='rank',data=shopBottom,fit_reg=True) 
p2.set(xlabel='Accessibility ranking', ylabel='Popularity rank',title = 'Bottom Shopping Sites') 
###there doesn't seem to be a correlation of accessibility by the popularity of the website


# bin data and plot 
shopTop.hist(column='accessrank') #trends of accessibility for top shopping sites
#bin data to see any trends for every 100 sites in order of pupularity
shopTop=shopTop.reset_index()
means =[]
labels =[]
for i in range(0,len(shopTop)+100,100):
    if i == 0:
        ind = i 
    else:
        means.append(shopTop[ind:i]['accessrank'].mean())
        labels.append(i)       
binShopTop = pd.DataFrame() 
binShopTop['popularity']  = labels
binShopTop['accessrank_mean']  = means
sns.lmplot(x='popularity',y='accessrank_mean',data=binShopTop,fit_reg=True)

shopBottom=shopBottom.reset_index()
means =[]
labels =[]

for i in range(0,len(shopBottom)+100,100):
    if i == 0:
        ind = i 
    else:
        means.append(shopBottom[ind:i]['accessrank'].mean())
        labels.append(i+95000)      
binShopBottom = pd.DataFrame() 
binShopBottom['popularity']  = labels
binShopBottom['accessrank_mean']  = means
sns.lmplot(x='popularity',y='accessrank_mean',data=binShopBottom,fit_reg=True)
##we see that as popularity ranking decreases so does the accessibility ranking 


#make list of most common ecommerce platforms (https://mopinion.com/most-popular-ecommerce-platforms-an-overview/)
#then calculate average accessibility rank, # of errors and most common errors
platforms = ['shopify.com','bigcommerce.com','magento.com','woocommerce.com',
             '3dcart.com','nopcommerce.com','volusion.com','squarespace.com',
             'wix.com','weebly.com','bigcartel.com','x-cart.com','ionos.com',
             'ecwid.com','123-reg.co.uk','wordpress.com']
foundInd = []
#find the index of all the rows that match in name 
for i in range(len(platforms)):
   temp = (allDat.loc[allDat['URL'].str.match(platforms[i])]).index.tolist()
   foundInd.extend(temp)
#subset new dataframe based on the index
foundSites = allDat.iloc[foundInd]
#drop two rows that do not match
foundSites=foundSites.drop([15272,40460])
#calculate average accessibility rank
foundSites['accessrank'].mean()
foundSites['accessrank'].min()
##I filtered the data for the top e-commerce platforms which 
#hosts the majority of smaller businesses and found that the mean accessibility 
#of these 16 sites was 392,509/1,000,000 or about a 39% accessibility ranking. 
#The most accessible platform is volusion.com with a ranking of 39,635/1,000,000. 
#In comparison, the most popular platform wordpress.com scored an accessibility 
#score of 146,554/1,000,000.

#select all columns that have errors so we can add the total number of errors 
foundSitesErrors = foundSites[foundSites.columns[:36]]
foundSitesErrors['most_common_error']= foundSitesErrors.iloc[:, 14:36].idxmax(axis=1)
sitesTable = foundSitesErrors[['accessrank','URL', 'most_common_error']]
#foundSitesErrors['most_common_error'] = 

##
##focus on amazon 
##do something in terms of error
##heat map based on categories and accessibility
##bin sites based on popularity (every 100?)

