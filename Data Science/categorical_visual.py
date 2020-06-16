# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:35:36 2020

@author: Sofia
"""

'''
Categorical variables. Visualization techniques

Background: There is an ice cream shop, that is operating in New York, 
LA and San Francisco.

Data: You have sold 12,327 ice creams in New York; 
17,129 in LA and 19,923 in San Francisco.

Task 1: Order the data in a frequency distribution table.

Task 2: Create a bar chart, representing the data. 

Task 3: Create a new column in your table, representing the relative frequency of input. 
You can choose to express it in percentages or as a decimal.

Task 4: Create a pie chart, representing the share of each city to the sales of your company.

Task 5: Create a Pareto Diagram, 
Order the table by frequency.
Create a bar (column) chart representing the ordered data.
In a new column, calculate the cumulative frequency of the data. 
On a second axis in the same chart, represent the cumulative frequency of the data.

'''

#####################FUNCTIONS#######################
def relative_frequence(dList):
    
    total = 0
    average = 0
    frequence = []
    
    for i in range(len(dList)):
        
        total += dList[i][1] 
        
    for i in range(len(dList)):
        
        average = round(dList[i][1] / total, 2) 
        frequence.append(average)
    
    return frequence

def cumulative_frequence(df):
    
    cumulative = 0
    cf_list = []

    for i in range(len(df)):
        
               
        cumulative += df.loc[i]['Relative Frequency'] 
        cf_list.append(cumulative)
        
    df['cf'] = cf_list
    return df

#####################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


data = [['Los Angeles', 17129], ['New York', 12327], ['San Francisco', 19923]]

df = pd.DataFrame(data)
df = df.rename(columns={0: "Cities", 1: "Frequency"})

relative_frequency = relative_frequence(data)

df['Relative Frequency'] = relative_frequency

df = df.sort_values(by='Frequency', ascending=False)
##plot data in barchart showing cities and frequence   
sns.barplot(x='Cities', y='Frequency', data=df )

#creating a pie chart
labels = df['Cities']
values = df['Relative Frequency']

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

### create the Pareto diagram
df = df.sort_values(by=['Frequency'], ascending=False )

new_df = cumulative_frequence(df)

df.index = df['Cities']

fig, ax = plt.subplots()
ax.bar(df.index, df["Frequency"], color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cf"]*100, color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.show()