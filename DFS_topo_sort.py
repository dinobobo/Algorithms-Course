# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 11:46:57 2018

@author: DinoBob
"""
import numpy as np
from collections import defaultdict


# reverse all the edges of a directed graph
def rev_dg(G):
    rev_G = defaultdict(list)
    for i in G.keys():
        rev_G[i]
        for j in G[i]:               
            rev_G[j].append(i)
    return rev_G

############################ DFS ###################################
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
        if G[j][-1] == False:
            Explore_recur(G, j)
    post(s)


            
def Explore_iter(G,s):
    st = [s]
    pre(s)
    while len(st) > 0:
        advance = False
        G[st[-1]][-1] = True
        for j in G[st[-1]][:-1]:
            if G[j][-1] == False:
                st.append(j)
                pre(j)
                advance = True
                break
        if advance == False:    
            post(st.pop())         

def DFS(G):
    for i in G.keys():
        G[i].append(False)
    for j in G.keys():
        if G[j][-1] == False:
            Explore_iter(G, j) 
            
def Explore_iter_counting(G,s):
    st = [s]
    v_num = 0
    while len(st) > 0:
        advance = False
        G[st[-1]][-1] = True
        for j in G[st[-1]][:-1]:
            if G[j][-1] == False:
                st.append(j)
                pre(j)
                advance = True
                break 
        if advance == False:
            st.pop()
            v_num += 1
    return v_num
    
    
if __name__ == '__main__':

    graph = defaultdict(list)

    scc_data = np.loadtxt('SCC.txt')
    for i in range(len(scc_data)):
        graph[int(scc_data[i][0])].append(int(scc_data[i][1]))

    #graph = {1:[4], 2:[8], 3:[6], 4:[7], 5:[2], 6:[9], 7:[1], 8:[5,6], 9:[7,3]}
    #graph = {1:[2], 2:[3,4,5], 3:[6], 4:[5,7], 5:[2,6,7], 6:[3,8], 7:[8,10], 8:[7], 9:[7], 10:[9,11],11:[12],12:[10]}
    rev_G = rev_dg(graph)       
    for k in rev_G.keys():
        if k not in graph.keys():
            graph[k]
    clock = 1
    v_num = []
    order = {}
    DFS(rev_G)
    order_list = sorted(order.items(), key = lambda x : x[1][1])
    order_list.reverse()
    for j in graph.keys():
        graph[j].append(False)
        
        
    for j in order_list:
        if graph[j[0]][-1] == False:
            exp_num = Explore_iter_counting(graph, j[0])
            v_num.append(exp_num)        
    v_num = sorted(v_num) 
    v_num.reverse()
        
        
        
        
        
    
