# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:11:42 2018

@author: DinoBob
"""
import numpy as np
from collections import defaultdict
def bsearch(i,j, s_arr, q):
    if j - i == 1:
        return i
    mid = i + len(s_arr[i:j])//2 
    if s_arr[mid] == q:
        return mid
    elif s_arr[mid] > q:
        return bsearch(i, mid, s_arr, q)
    else:
        if mid == j - 1:
            return mid
        else:
            return bsearch(mid+1, j, s_arr, q)
        
        
with open('twosum.txt') as f:
    content = f.readlines()
    data = [int(x.split()[0]) for x in content]
data = list(set(data))
data = sorted(data)
#data =sorted([-3,-1,1,2,9,11,7,6,2])


low_bd = -10000
high_bd = 10000
ans = defaultdict(int)
for j in range(len(data)): 
    low_idx = bsearch(0, len(data), data, low_bd - data[j])
    if data[low_idx] < low_bd - data[j]:
        low_idx += 1
    high_idx = bsearch(0, len(data), data, high_bd - data[j])
    if data[high_idx] > high_bd - data[j]:
        high_idx -= 1
    if high_idx >= low_idx:
        if low_idx <= j <= high_idx:
            for k in range(low_idx, j):
                ans[data[j] + data[k]]
            for l in range(j+1, high_idx + 1):
                ans[data[j] + data[l]]
        else:
            for k in range(low_idx, high_idx + 1):
                ans[data[j] + data[k]]
