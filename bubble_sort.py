# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:29:00 2018

@author: DinoBob
"""

def bubble_sort(x):
    sort_count = 1
    while sort_count >=1:
        sort_count = 0
        for i in range(0,len(x)-1):
            if x[i+1] < x[i]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
                sort_count += 1 
    return(x)
print(bubble_sort([3,4,1,11,11,3]))