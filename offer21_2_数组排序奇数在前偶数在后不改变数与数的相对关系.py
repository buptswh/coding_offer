# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:21:47 2019

@author: swh
"""

# -*- coding:utf-8 -*-
def swap(array,i,j):
    temp=array[j]
    array[j]=array[i]
    array[i]=temp
def isodd(num):
    if num%2!=0:
        return True
    return False
def reOrderArray(array):
    # write code here
    oddnum=0
    #oddpos=0
    i=0
    while i < len(array):
        if isodd(array[i]):
            temp=array[i]
            for j in range(i-1,oddnum-1,-1):
                array[j+1]=array[j]
            array[oddnum]=temp
            oddnum+=1
        i+=1
    return array
if __name__=="__main__":
    a=input()
    array=[int(s) for s in a.split(',')]
    print(reOrderArray(array))