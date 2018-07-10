# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 07:22:36 2018

@author: DinoBob
"""
import numpy as np
def even_matrix(x, even = True):
    if len(x)%2 == 1:
        x_temp = np.zeros((len(x)+1,len(x)+1), dtype = int)
        x_temp[:len(x),:len(x)] = x
        even  = False
        return x_temp, even
    else:
        return x, even
def strassen(x , y):
    x = np.array(x)
    y = np.array(y)
    z = np.zeros((len(x),len(x)), dtype = int)
    if len(x) < 3:
        for i in range(len(x)):
            for j in range(len(y)):
                z[i,j] = sum(x[i,:]*y[:,j])
        return z
    else:
        x, even = even_matrix(x)
        y = even_matrix(y)[0]
        z = np.zeros((len(x),len(x)), dtype = int)
        x11 = x[:int(len(x)/2),:int(len(x)/2)]
        x12 = x[:int(len(x)/2), int(len(x)/2):len(x)]
        x21 = x[int(len(x)/2):len(x),:int(len(x)/2)]
        x22 = x[int(len(x)/2):len(x),int(len(x)/2):len(x)]
        y11 = y[:int(len(x)/2),:int(len(x)/2)]
        y12 = y[:int(len(x)/2), int(len(x)/2):len(x)]
        y21 = y[int(len(x)/2):len(x),:int(len(x)/2)]
        y22 = y[int(len(x)/2):len(x),int(len(x)/2):len(x)]
        s1 = strassen(x11+x22,y11+y22)
        s2 = strassen(x21+x22,y11)
        s3 = strassen(x11,y12-y22)
        s4 = strassen(x22,y21-y11)
        s5 = strassen(x11+x12,y22)
        s6 = strassen(x21-x11,y11+y12)
        s7 = strassen(x12-x22,y21+y22)
        z[:int(len(x)/2),:int(len(x)/2)] = s1 + s4 - s5 +s7
        z[:int(len(x)/2), int(len(x)/2):len(x)] = s3 + s5
        z[int(len(x)/2):len(x),:int(len(x)/2)] = s2 +s4
        z[int(len(x)/2):len(x),int(len(x)/2):len(x)] = s1 - s2 + s3 + s6
        if even == True:
            return z
        else:
            return z[:len(z)-1,:len(z)-1]
print(strassen(np.arange(16).reshape(4,4),np.arange(16).reshape(4,4)))