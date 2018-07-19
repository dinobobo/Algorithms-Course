# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:10:27 2018

@author: DinoBob
"""
import numpy as np
import random
def quick_sort(P,l,r,counting):
    if r-l+1 < 2:
        return(sorted(P[l:r+1]))
    else:
        pivot = r
        #pivot = l
        #pivot = random.randint(l,r)
        '''
        pivot = 0
        pivot_sample = np.array([[P[l],l], [P[r],r], [P[(r+l)//2],(r+l)//2]], dtype = int)
        pivot_value = np.median(pivot_sample[:,0])
        for i in range(3):
            if pivot_sample[i,0] == pivot_value:
                pivot = pivot_sample[i,1]
        '''
        print(P[pivot])
        counting.append(r-l)
        P[pivot], P[l] = P[l], P[pivot]
        i = l 
        for j in range(l+1, r+1):
            if P[j] <= P[l]:
                P[j], P[i+1] = P[i+1], P[j]
                i += 1 
        P[l], P[i] = P[i], P[l]
        #Partiton the arrary with the pivot point
        P[l:i] = quick_sort(P,l,i-1,counting)
        P[i+1:r+1] = quick_sort(P,i+1,r,counting) 
        return(P[l:r+1]) 
#P = random.sample(range(10),8)
#P = [1, 4, 3, 0, 9, 7, 5, 8]
data = np.loadtxt('QuickSort.txt')
P = data.tolist()
counting = []
print(P)
print(quick_sort(P,0,len(P)-1,counting))
print(sum(counting))
