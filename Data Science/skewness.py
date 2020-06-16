# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:46:40 2020

@author: Sofia
"""

'''
Identify the skewness of dataset 1. You may use the formula from the lesson, the skewness formula in excel (=SKEW) or you can plot it on a graph												
Identify the skewness of dataset 2. You may use the formula from the lesson, the skewness formula in excel (=SKEW) or you can plot it on a graph												


'''

import pandas as pd
import numpy as np

df = pd.read_csv('skewness.csv', delimiter=';')

skewValue = df.skew(axis=0)

