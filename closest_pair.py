# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:29:27 2018

@author: DinoBob
"""
import numpy as np
import math
def sort_array_pairs(x,axis = 0):   
    for j in range(len(x)):
        min_idx = j
        for i in range(j+1,len(x)):
            if x[i,axis] <= x[j,axis]:
                min_idx = i
        x[j], x[min_idx] = x[min_idx].copy(), x[j].copy() #when assign a list to variable, use copy so it will not be changed      
    return(x) 
   
def merge_sort_pairs(x, axis = 0):
    if len(x) < 3:
        sort_array_pairs(x,axis)
    else:
        L = x[0 : int(len(x)/2)].copy()
        R = x[int(len(x)/2): len(x)].copy()
        L = merge_sort_pairs(L)
        R = merge_sort_pairs(R)
        i = 0
        j = 0
        k = 0
        for i in range(len(x)):
            if j < len(L) and k <len(R):
                if L[j,axis]<=R[k,axis]:
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

def distance(x, y):
    return(np.sqrt((x[0]-y[0])**2 + (x[1] - y[1])**2))

def closestpair(a):
    if len(a) < 4:
        delta = distance(a[0],a[1])
        pair = [a[0],a[1]]
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if distance(a[i],a[j]) < delta:
                    d = distance(a[i] , a[j])
                    pair = [a[i],a[j]]
        return (pair,delta)
    sorted_x = merge_sort_pairs(a.copy())
    sorted_y = merge_sort_pairs(a.copy(),1)
    Lx = sorted_x.copy()[0:int(len(a)/2)]
    Rx = sorted_x.copy()[int(len(a)/2):len(a)]
    Lx_pair = closestpair(Lx.copy())
    Rx_pair = closestpair(Rx.copy())
    delta, x_bar = min(Lx_pair[1], Rx_pair[1]), sorted_x[int(len(a)/2)][0]
    if Lx_pair[1] < Rx_pair[1]:
        pair = Lx_pair[0]
    else:
        pair = Rx_pair[0]
    sy = []
    for i in range(len(sorted_y)):
        if x_bar - delta <= sorted_y[i,0] <= x_bar + delta:
            sy.append(sorted_y[i])
    for j in range(len(sy) - 1):
        for k in range(j + 1, min(j+7, len(sy))):
            if delta <= distance(sy[j],sy[k]):
                delta = distance(sy[j],sy[k])
                pair = [sy[j],sy[k]]
    return (pair,delta)
    
print(closestpair(np.array([[11,3],[2,14],[5,5],[300,1],[3,14],[11,3]])))