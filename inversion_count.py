# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 08:57:27 2018

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
    
def inv_cnt(x):
    if len(x) < 4:
        cnt = 0
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[j] < x[i]:
                    cnt += 1
        x = sort_array(x)
    else:               
        xl = x[0:int(len(x)/2)]
        xr = x[int(len(x)/2):len(x)]
        xl_cnt, xl = inv_cnt(xl)
        xr_cnt, xr = inv_cnt(xr)
        i,j,k = 0,0,0
        cross_cnt = 0
        for k in range(len(x)):
            if i < len(xl) and j < len(xr):
                if xl[i] <= xr[j]:
                    x[k] = xl[i]
                    i += 1
                else:
                    x[k] = xr[j]
                    j += 1
                    cross_cnt += len(xl) - i
            else:
                if i == len(xl):
                    x[k] = xr[j]
                    j += 1
                else:
                    x[k] = xl[i]
                    i += 1
        cnt = xl_cnt + xr_cnt + cross_cnt
    return(cnt, x)
   