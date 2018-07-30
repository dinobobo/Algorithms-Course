# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 08:30:57 2018

@author: DinoBob
"""
import csv
import numpy as np


def r_contraction(adj_list):
    while len(adj_list) > 2:
        #find two vertices on the edge
        r_ver_idx = np.random.randint(len(adj_list))
        r_ver = adj_list[r_ver_idx][0]
        r_ver2_idx = np.random.randint(1,len(adj_list[r_ver_idx]))
        r_ver2 = adj_list[r_ver_idx][r_ver2_idx]
        
        #find the row index of the second vertex
        ver2_r = 0
        for i in range(len(adj_list)):
            if adj_list[i][0] == r_ver2:
                ver2_r = i
        
        
        # remove the redundent vertices or self loops 

        k = 1
        while k < len(adj_list[r_ver_idx]):
            if adj_list[r_ver_idx][k] == r_ver2:
                adj_list[r_ver_idx].pop(k)
            else:
                k += 1
                
        for j in range(1,len(adj_list[ver2_r])):
            if adj_list[ver2_r][j] != r_ver and adj_list[ver2_r][j] != r_ver2:
               adj_list[r_ver_idx].append(adj_list[ver2_r][j])                
               
        #replace vertex2 to vertex 1
        for i in range(len(adj_list)):
            if i != r_ver_idx:
                for j in range(len(adj_list[i])):
                    if adj_list[i][j] == r_ver2:
                        adj_list[i][j] = r_ver  
        adj_list.pop(ver2_r)
    return(adj_list) 


        
        
        
        
    
    
with open('kargerMinCut.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
data = [[int(x) for x in line[0:-1]] for line in d]
#data = [[1,2, 3, 4, 7],[2, 1, 3, 4],[3, 1, 2, 4],[4 ,1, 2, 3 ,5],[5, 4 ,6 ,7, 8],[6 ,5 ,7, 8],[7, 1, 5, 6, 8],[8, 5 ,6, 7]]
result = r_contraction(data)
print(len(result[0]))
print(len(result[1]))