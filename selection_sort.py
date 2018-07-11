# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:16:24 2018

@author: DinoBob
"""

def sort_array(x):   
    for j in range(len(x)):
        min_idx = j
        for i in range(j+1,len(x)):
            if x[i] <= x[j]:
                min_idx = i
            x[j], x[min_idx] = x[min_idx], x[j]
    return(x)  
print(sort_array([1,2,1,2,7,5,11]))