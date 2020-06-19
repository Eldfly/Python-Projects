'''

Harry Potter - 
Predict which house someone will be in. 

'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


df_main = pd.read_csv('steam.csv')
df_description = pd.read_csv('steam')


merged_data