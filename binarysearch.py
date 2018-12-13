# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:15:11 2018

@author: DinoBob
"""

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
        
s_arr = list([1,2,3,4,5])
ans = bsearch(0,len(s_arr),s_arr, 6)