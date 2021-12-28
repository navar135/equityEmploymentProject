#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:16:03 2021

This script will clean the CDC dataset 
It is being downloaded from https://data.census.gov/mdat/#/search?ds=ACSPUMS1Y2019
We will be using the person weighted data not the housing unit weighted data
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

#gchange path to be where your folder is in 
os.chdir("/Users/navar135/Documents/GitHub/equityEmploymentProject/")#change this for your personal path (use pwd)
#import dataset
with open('rawData/ACSPUMS1Y2019_2021-12-15T133639/ACSPUMS1Y2019_2021-11-17T095929.csv') as f:
    df=pd.read_csv(f, delimiter=';')