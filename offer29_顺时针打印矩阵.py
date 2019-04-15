# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:46:13 2019

@author: swh
"""
"""
需求：顺时针打印矩阵
输入：矩阵，
输出：顺时针打印的list
"""
class solution:
    
    def printarrayincircle(self,array):
        if not array:
            return None
        rows,cols=len(array),len(array[0])
        start=0
        while 2*start<rows and 2*start<cols:
            self.printout(array,start)
            start+=1
    def printout(self,array,start):
        xend=len(array[0])-1-start
        yend=len(array)-1-start
        if start<=xend and start<=yend:
            for i in range(start,xend+1):#从左到右打印
                print(array[start][i])
        if start<yend:
            for i in range(start+1,yend+1):#从上到下打印
                print(array[i][xend])
        if start<xend and start<yend:
            for i in range(xend-1,start-1,-1):#从右往左
                print(array[yend][i])
        if start<xend and start<yend-1:
            for i in range(yend-1,start,-1):#从下往上
                print(array[i][start])
                
if __name__=="__main__":
    line0=input()
    nums=line0.split(' ')
    array=[]
    array.append(nums)
    while True:
        s=input()
        if s=='':
            break
        line=s.split(' ')
        if len(line)!=len(nums):
            print("invalid input")
        else:
            array.append(line)
    examp=solution()
    examp.printarrayincircle(array)
    
        