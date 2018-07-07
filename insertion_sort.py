# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:59:57 2018

@author: DinoBob
"""
def insertion_sort(x):
    for i in range(0,len(x)-1):
        for j in range(0,i):
            if x[i+1] <= x[j]:
                x.insert(j,x[i+1])
                x.pop(i+2)            
            else:
                x.insert(i,x[i+1])
                x.pop(i+2)
    return(x)
print(insertion_sort([3,4,1,11,11,3]))