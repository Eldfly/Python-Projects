# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:30:06 2020

@author: Sofia
"""

'''

Dataset
8
30
30
50
86
94
102
110
169
170
176
236
240
241
242
255
262
276
279
282


Task 1: Given that we want to divide the numbers into 6 
intervals of equal width, calculate that interval width. 
Round up to the nearest whole number, 
bigger than the result that you obtain

Task 2: Create a frequency distribution table that shows 

        1. The intervals 
        2. The absolute frequency of each interval
        3.  The relative frequency of each interval

    
'''

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

import pandas as pd

data = [8,30,30,50,86,94,102,110,169,170,176,236,240,241,242,
255,262,276,279,282]


intervals = 6
intervals_width = round((max(data) - min (data)) / intervals)

intervals_list = [[8,54], [54,100], [100,146], [146,192], [192,238], [238,284]]

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
