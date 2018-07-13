# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 08:57:27 2018

@author: DinoBob
"""    
import random

def inv_cnt(x):
    if len(x) < 3:
        cnt = 0
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[j] < x[i]:
                    cnt += 1
        x = sorted(x)
        return(cnt, x)
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
x = inv_cnt(data)   