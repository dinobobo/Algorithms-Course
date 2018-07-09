# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 08:57:27 2018

@author: DinoBob
"""

def inv_cnt(x):
    xl = x[0:int(len(x)/2)]
    xr = x[int(len(x)/2):len(x)]
    xl_cnt = inv_cnt(xl)
    xr_cnt = inv_cnt(xr)
    