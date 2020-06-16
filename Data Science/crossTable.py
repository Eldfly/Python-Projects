# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:01:01 2020

@author: Sofia
"""

''

'''
Background: 
    You have employment data about country X. 
    You have been asked to prepare a cross-table showing that data.
    
    60% of 18 to 25-year-olds are employed
    85% of 25 to 35-year-olds are employed
    5% of 35 to 45-year-olds are unemployed
    3% of 45 to 55-year-olds are unemployed
    All 65+ are employed. 
   
    Note: the definition of unemployed is:
    without a job, but actively searching for one. 
    That's probably why all 65+s are employed.
    
    Task 1: Create a cross table summarizing the data you have been given.
    Task 2: Create a side-by-side bar chart (it is called clustered column chart in Excel), 
    in order to visually enhance your summary.

'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

employment = [['18 -25', 60, 40],['25 - 35', 85, 15],['35 - 45', 95, 5], ['45 - 55', 97, 3], ['65+', 100, 0]]

df = pd.DataFrame(employment, columns=['Age', 'Employment %', 'Unemploymend %'])

#show data in bar chart
plt.style.use('ggplot')
plt.figure(figsize=(12,6))
ax = df.plot.bar('Age','Employment %')
ax.set_xlabel("Age")
ax.set_ylabel("Employment")

