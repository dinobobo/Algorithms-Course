# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:43:42 2018

@author: DinoBob
"""
import random
def random_selection(P, l, r, i):
    '''
    selects i th smallest number in array P
    '''
    if r-l+1 < 2:
        return P[l]
    else:
        i_stat = 0
        pivot = random.randint(l,r)
#        print(P[pivot])
        P[pivot], P[l] = P[l], P[pivot]
        k = l 
        for j in range(l+1, r+1):
            if P[j] <= P[l]:
                P[j], P[k+1] = P[k+1], P[j]
                k += 1 
        P[l], P[k] = P[k], P[l]
        if k == i-1:
            i_stat = P[k]
        elif k < i-1:
            i_stat = random_selection(P, k+1, r, i-1-k)        
        else:
            i_stat = random_selection(P, l, k-1, i)
        return i_stat
P = random.sample(range(20),10)
print(P)
answer = random_selection(P,0,len(P)-1,3)