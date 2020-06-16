# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:46:40 2020

@author: Sofia
"""

'''
Task 1: Calculate the covariance of the two datasets
Task 2: Plot the data on scatter plot and using your previous knowledge comment on whether there is a noticeable relationship between the two variables.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Covariance.csv', delimiter=';')

covariance = df.cov()

plt.figure(figsize=(12,6))
sns.scatterplot(x='Reading', y='Writing', data=df)
sns.scatterplot(x='Writing', y='Reading', data=df)

#Calculate the correlations between Reading and writing
corr = df.corr()
