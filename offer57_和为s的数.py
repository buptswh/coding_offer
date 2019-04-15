# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:15:51 2019

@author: swh
"""

#和为s的数字
'''
输入：一个递增排序的数组，和一个数字s
返回和为s的数组中的两个数，输出任意一对即可
'''
'''
第一个思路：定义两个指针指向的数字，一个在前，一个从后往前
0为不存在这样的组合
'''
class Solution:
    def sumiss(self,nums,s):
        if not nums or s<2*nums[0] or s>2*nums[-1]:
            return 0
        n=len(nums)
        start,end=0,n-1
        while start<end:
            currentsum=nums[start]+nums[end]
            if currentsum>s:
                end-=1
            elif currentsum<s:
                start+=1
            else:
                return [nums[start],nums[end]]
        return 0
    '''
    打印出和为s的连续正数序列
    例如：15,1+2+3+4+5=4+5+6=7+8=15
    '''
    def printnums(self,small,big):
        for i in range(small,big+1):
            print(i)
        print('\n')
    def numss(self,n):
        if n<1:
            return 0
        start=1
        mid=n>>1
        while start<=mid:
            big=start
            currentsum=start
            while currentsum<n:
                big+=1
                currentsum+=big
                if currentsum==n:
                    self.printnums(start,big)
                    break
            start+=1
            
