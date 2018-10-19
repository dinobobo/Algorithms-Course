# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 12:54:18 2018

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
    
def DFS(G,s):
    for i in G.keys():
        G[i].append(False)
    st = [s]
    pre(s)
    while len(st) > 0:
        advance = False
        G[st[-1]][-1] = True
        for j in G[st[-1]][:-1]:
            if G[str(j)][-1] == False:
                st.append(str(j))
                pre(str(j))
                advance = True
                break
        if advance == False:    
            post(str(st.pop()))    
    
    
if __name__ == '__main__':   
    graph = {'1':[2,3],'2':[1,4],'3':[1,4,6],'4':[2,3,5,6],'5':[4,6],'6':[3,4,5]}    
    order = {}  
    clock = 1
    DFS(graph, '1')    