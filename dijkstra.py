# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:17:56 2018

@author: DinoBob
"""
import numpy as np
import csv
from collections import defaultdict
from heapq import heapify, heappush, heappop

class edge:
    def __init__(self, v, w, d):
        self.v = v
        self.w = w
        self.d = d
    def __lt__(self, other):
        return self.d < other.d
    def __str__(self):
        return "({0},{1},{2})".format(self.v,self.w, self.d)
        
        
    
def Dijkstra(graph, s):
    
    dist = defaultdict(int)
    dist[s] = 0
    d_heap = [edge(s, x[0], x[1]) for x in graph[s]]  
    heapify(d_heap)
    while len(d_heap) > 0:
        close_edge = heappop(d_heap)
        if dist[close_edge.w] == 0:
            dist[close_edge.w] = close_edge.d
        for j in graph[close_edge.w]:
            if j[0] not in dist:
                heappush(d_heap, edge(close_edge.w, j[0], j[1] + dist[close_edge.w]))
    return dist


if __name__ == '__main__':
    with open('dijkstraData.txt') as f:
        content = f.readlines()
        data = [x.split() for x in content]
        graph = defaultdict(list)
        for i in data:
            graph[int(i[0])] = [list(map(int, x.split(','))) for x in i[1:]]
    
    test = [[1, [2,1], [8,2]], [2, [1,1], [3,1]], [3, [2,1], [4,1]], [4, [3,1], [5,1]], [5, [4,1], [6,1]],
            [6, [5,1], [7,1]], [7, [6,1], [8,1]], [8, [7,1], [1,2]]]
    test_graph = defaultdict(list)
    for k in test:
        test_graph[k[0]] = [x for x in k[1:]]
    ans = Dijkstra(graph,1)   
