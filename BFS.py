# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 07:27:58 2018

@author: DinoBob
"""
from collections import deque
    
def BFS(G, s):
    global dist
    for i in G.keys():
        G[i].append(False)
    G[s][-1] = True
    q = deque([s])
    dist[s] = 0 
    while len(q) != 0:
        v = q.popleft()
        for j in G[v][:-1]:
            if G[str(j)][-1] == False:
                G[str(j)][-1] = True
                q.append(str(j))
                dist[str(j)] = dist[v] + 1
            
            
    
graph = {'1':[2,3],'2':[1,4],'3':[1,4,6],'4':[2,3,5,6],'5':[4,6],'6':[3,4,5]}
dist = {}
BFS(graph, '1')    