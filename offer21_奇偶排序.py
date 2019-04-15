# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:02:40 2019

@author: swh
"""

#奇偶排序数组
def order(nums):
    if not nums:
        return 
    start,end=0,len(nums)-1
    while start<end:
        while start < end and not func(nums[start]):
            start+=1
        while start < end and func(nums[end]):
            end-=1
        if start > end:
            temp=start
            start=end
            end=temp
def func(n):
    if n&1==0:
        return True
    else:
        return False            
        