# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:40:05 2019

@author: swh
"""

#礼物的最大价值
def maxValue(values):
    if not values:
        return 0
    m,n=len(values),len(values[0])
    maxvalues=[[0]*n]*m
    for i in range(m):
        for j in range(n):
            right,down=0,0
            if i>0:
                down=maxvalues[i-1][j]
            if j >0 :
                right=maxvalues[i][j-1]
            maxvalues[i][j]=max(right,down)+values[i][j]
    return maxvalues[-1][-1]
    
    