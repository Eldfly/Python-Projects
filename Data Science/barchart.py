# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:30:06 2020

@author: Sofia
"""

'''

Dataset
13
68
165
193
216
228
361
470
500
529
544
602
647
692
696
699
809
892
899
936



Task 1: Create a bar chart with 10 intervals, based on your dataset.


    
'''
### functions
def relative_frequence(dList):
    
    total = 0
    average = 0
    relative_frequence = []
    
    for i in range(len(dList)):
        
        total += dList[i] 
        
    for i in range(len(dList)):
        
        average = round(dList[i] / total, 2) 
        relative_frequence.append(average)
    
    return relative_frequence

def create_intervals(start, intervals, intervals_width):
    
    start = start
    intervals = intervals
    intervals_width = intervals_width
    interval_end = 0
    
    for x in range(0, intervals):
    
        if x == 0:
            interval_end += intervals_width + start
            print(interval_end)
            intervals_list.append([start, interval_end])
            
        else:
            temp_start = interval_end
            temp_end = temp_start + intervals_width
            intervals_list.append([temp_start, temp_end])
            interval_end = temp_end
    
    return intervals_list

######################################################################

import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

data = [13,68,165,193,216,228,361,470,500,529,544,602,647,692,696,699,809,892,
899,936]

intervals_list = []
intervals = 10
intervals_width = math.ceil((max(data) - min (data)) / intervals)
start = 13
intervals_list = create_intervals(start, intervals, intervals_width)
   
df = pd.DataFrame(intervals_list, columns= ['interval_start', 'interval_end'])

frequence_count = []
frequence = []
    

## find out how many times my data is showing up in the interval list
for i in range(len(data)):
    
    for x in range(len(intervals_list)):
    
        if (data[i] >= intervals_list[x][0]) and data[i] <= (intervals_list[x][1]):
            frequence_count.append(intervals_list[x])

##summarize the number of times a number is in a interval and add to new list                        
for items in range(len(intervals_list)):
  
     frequence.append(frequence_count.count(intervals_list[items]))

#add frequence list to my dataframe. 
df['frequence'] = pd.DataFrame(frequence)

##add relative frequence to my df
rf = relative_frequence(frequence)
df['relative frequence'] = pd.DataFrame(rf)


#show data in bar chart
df['intervals'] =df['interval_start'].astype(str) + ' - ' + df['interval_end'].astype(str)

plt.style.use('ggplot')
plt.figure(figsize=(12,6))
ax = df.plot.bar('intervals','frequence')
ax.set_xlabel("Intervals")
ax.set_ylabel("Frequence")