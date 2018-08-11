# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 12:54:18 2018

@author: DinoBob
"""

def DFS(G,s):
    for i in G.keys():
        G[i].append('False')
    st = [s]
    while len(st) > 0:
        advance = 'False'
        G[st[-1]][-1] = 'True'
        for j in G[st[-1]][:-1]:
            if G[str(j)][-1] == 'False':
                st.append(str(j))
                advance = 'True'
                break
        if advance == 'False':    
            st.pop()    
                
            
            
    
    
    
graph = {'1':[2,3],'2':[1,4],'3':[1,4,6],'4':[2,3,5,6],'5':[4,6],'6':[3,4,5]}
DFS(graph, '1') 