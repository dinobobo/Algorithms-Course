# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:16:24 2018

@author: DinoBob
"""

def sort_array(x):   
    for j in range(0,len(x)):
        a = x[j]
        for i in range(j,len(x)):
            if x[i] <= a:
                a = x[i]
                indi = i
        temp = x[indi]     
        x[indi] = x[j]
        x[j] = temp
    return(x)  
print(sort_array([1,7,1,2,2,5,-1]))