# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 08:14:17 2018

@author: DinoBob
"""
def DFS_recur(G,s):    
    G[s][-1] = 'True'
    for j in G[s][:-1]:
        if G[str(j)][-1] == 'False':
            DFS_recur(G, str(j))
        
        
                
            
            
    
    
graph = {'1':[2,3],'2':[1,4],'3':[1,4,6],'4':[2,3,5,6],'5':[4,6],'6':[3,4,5]}
for i in graph.keys():
        graph[i].append('False')
        
DFS_recur(graph, '1') 