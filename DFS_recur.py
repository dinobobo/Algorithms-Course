# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 08:14:17 2018

@author: DinoBob
"""
def pre(s):
    global clock
    order[s] = [clock]
    clock += 1

def post(s):
    global clock
    order[s].append(clock)
    clock += 1
    
def Explore_recur(G,s):   
    G[s][-1] = True
    pre(s)
    for j in G[s][:-1]:
        if G[str(j)][-1] == False:
            Explore_recur(G, str(j))
    post(s)
'''      
def DFS(G):
    for i in G.keys():
        G[i][-1] = 'False'

    for j in G.keys():
        if G[j][-1] == 'False':
            Explore_recur(G, i)        
'''            
if __name__ == '__main__':   
    graph = {'1':[2,3, False],'2':[1,4, False],'3':[1,4,6, False],'4':[2,3,5,6, False],'5':[4,6, False],'6':[3,4,5, False]}    
    order = {}  
    clock = 1
    Explore_recur(graph, '1')    
#    DFS(graph) 