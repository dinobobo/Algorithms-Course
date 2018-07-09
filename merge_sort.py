# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:30:47 2018

@author: DinoBob
"""
import numpy as np
import math
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
    
def merge_sort(x):
    if len(x) < 3:
        sort_array(x)
    else:
        L = x[0 : int(len(x)/2)]
        R = x[int(len(x)/2): len(x)]
        L = merge_sort(L)
        R = merge_sort(R)
        i = 0
        j = 0
        k = 0
        for i in range(len(x)):
            if j < len(L) and k <len(R):
                if L[j]<=R[k]:
                    x[i] = L[j]
                    j += 1
                else:
                    x[i] = R[k]
                    k += 1
                   
            else:
                if j == len(L):
                    x[i] = R[k]
                    k += 1
                else:
                    x[i] = L[j]
                    j += 1 
    return(x)
    
print(merge_sort([2,5,6,3,2,9,11,109,2,4,5,1]))
