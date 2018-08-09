# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 07:27:58 2018

@author: DinoBob
"""
from collections import deque
def BFS(G, s):
    for i in G.keys():
        G[i].append('False')
    G[s][-1] = 'True'
    q = deque([s])
    while len(q) != 0:
        v = q.popleft()
        for j in G[v]:
            if G[j][-1] == 'False':
                G[j][-1] = 'True'
                q.append(j)
            
            
    
graph = {'1':[2,3],'2':[1,4],'3':[1,4,6],'4':[2,3,5,6],'5':[4,6],'6':[3,4,5]}
    