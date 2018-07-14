# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:10:27 2018

@author: DinoBob
"""
import random
def quick_sort(P,l,r):
    if r-l+1 < 4:
        return(sorted(P[l:r+1]))
    else:
        pivot = np.random.randint(l,r+1)
        print(P[pivot])
        P[pivot], P[l] = P[l], P[pivot]
        i = l 
        for j in range(l+1, r+1):
            if P[j] <= P[l]:
                P[j], P[i+1] = P[i+1], P[j]
                i += 1 
        pivot = P.pop(l)
        P.insert(i,pivot)
        #Partiton the arrary with the pivot point
        P[l:i] = quick_sort(P,l,i-1)
        P[i+1:r+1] = quick_sort(P,i+1,r) 
        return(P[l:r+1])
P = [3,5,1,11,4]   
P = random.sample(range(100),50)
print(P)
print(quick_sort(P,0,len(P)-1))
