# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:16:35 2019

@author: swh
"""
class Solution:
    #一数字只出现一次，其他数字都出现了两次
    def onenum(self,nums):
        if not nums:
            return False
        res=0
        return (res^num for num in nums)
    #两个数字只出现了一次，其他数字都出现了两次
    def twonum(self,nums):
        xor,a,b=0,0,0
        for num in nums:
            xor^=num#存储两个只出现一次的数字的异或值
        xor^=-xor#取其最低位的不一致的值，用于分组
    
        for num in nums:
            if num^xor!=0:
                a^num#第一个值
            else:
                b^num#第二个值
        return [a,b]#返回两个只出现一次的值
    #一个数字出现了一次，其他数字出现了三次
    """
    思路是：按照位计算，若果整数出现了三次，肯定%3==0，叠加上只出现一次的值得位，就会%1.
    """
    def oneinthree(self,nums):
        x=1
        res=0
        count=[0]*32#数组记录所有位上出现的次数
        for i in range(32):
            x=x<<1
            count=0
            for num in nums:
                if x&num==1:
                    count[i]+=1
        for i in range(32):   
            res=res<<1        
            res+=count[i]%3
        return res
            
            
            