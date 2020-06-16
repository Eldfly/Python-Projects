# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:32:55 2020

@author: Sofia
"""

import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('scatterplot.csv', delimiter=';')

plt.figure(figsize=(12,6))
sns.scatterplot(x='Apple', y='Alphabet', data=df)
sns.scatterplot(x='Apple', y='Bank of America', data=df)

