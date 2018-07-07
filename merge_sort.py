# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:30:47 2018

@author: DinoBob
"""
import numpy as np
import math
def merge_array(x):
    i = 0
    j = 0
    k = 0
    L = x[0 : int(len(x)/2)]
    R = x[int(len(x)/2): len(x)]
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
    
def merge_twoarrays(L,R):
    i = 0
    j = 0
    k = 0
    merged = []
    while j < len(L) and k <len(R):
        if L[j]<=R[k]:
            merged.append(L[j])
            j += 1
        else:
            merged.append(R[k])
            k += 1
           
    if j == len(L):
        merged.extend(R[k:len(R)])
    else:
        merged.extend(L[j:len(L)])
    return(merged)
    
    
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
    sorted_basic = []
    for i in range(math.ceil(len(x)/2)-1): #sort the basic case
        sorted_basic.append(sort_array(x[2*i:2*(i+1)])) 
    sorted_basic.append(sort_array(x[2*(math.ceil(len(x)/2)-1):len(x)]))     
    sorted_result= sorted_basic
    while len(sorted_result) > 1:
        sorted_temp = sorted_result
        sorted_result = []
        if len(sorted_temp)%2 == 0:
            for i in range(math.ceil(len(sorted_temp)/2)):
                sorted_result.append(merge_twoarrays(sorted_temp[2*i],sorted_temp[2*i+1]))
        else:
            for i in range(math.ceil(len(sorted_temp)/2)-1):
                sorted_result.append(merge_twoarrays(sorted_temp[2*i],sorted_temp[2*i+1]))
            sorted_result.append(sorted_temp[-1])
    return(sorted_result)

print(merge_sort([2,5,6,3,2,9,11,109,2,4,5,1]))
