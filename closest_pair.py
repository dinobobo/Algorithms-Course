# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:29:27 2018

@author: DinoBob
"""
import numpy as np
import math


def distance(x, y):
    return(np.sqrt((x[0]-y[0])**2 + (x[1] - y[1])**2))

def closest_pair(Px, Py):
#####Brute Force#####    
    if len(Px) < 4:
        p,q = Px[0], Px[1]
        delta = distance(Px[0],Px[1])
        for i in range(len(Px)):
            for j in range(i+1,len(Px)):
                if distance(Px[i],Px[j]) < delta:
                    delta = distance(Px[i] , Px[j])
                    p,q = Px[i], Px[j]
        return (p,q, delta)
    else:    
        Lx = Px[0:len(Px)//2]
        Rx = Px[len(Px)//2:len(Px)]
        x_bar = Px[len(Px)//2][0]
        Ly = sorted(Lx, key = lambda x: x[1])
        Ry = sorted(Rx, key = lambda x: x[1])
        (p1, q1, delta1) = closest_pair(Lx, Ly)
        (p2, q2, delta2) = closest_pair(Rx, Ry)
        (pm, qm, deltam) = min((p1, q1, delta1), (p2, q2, delta2), key = lambda x : x[2])
        (p3, q3, delta3) = closest_split_pair(Px, Py, deltam, pm, qm)    
        return min((pm, qm, deltam), (p3, q3, delta3), key = lambda x : x[2])

def closest_split_pair(Px, Py, delta, pm, qm ):
    p3 = pm
    q3 = qm
    x_bar = Px[len(Px)//2][0]
    sy = [x for x in Py if x[0] >= x_bar - delta  and x[0] <= x_bar + delta]
    for j in range(len(sy) - 1):
        for k in range(j + 1, min(j+8, len(sy))):
            if delta >= distance(sy[j],sy[k]):
                delta = distance(sy[j],sy[k])
                p3 = sy[j]
                q3 = sy[k]
    return(p3, q3, delta)            
    
def presort(P):
    Px = sorted(P, key = lambda x: x[0])
    Py = sorted(P, key = lambda x: x[1])
    return Px, Py

Px, Py = presort([[11,2.5],[11,2],[3,1],[11,3],[0.,1],[0.1,1],[55,3],[54.98,3]])       
print(closest_pair(Px, Py))