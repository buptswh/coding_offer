# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:15:37 2019

@author: swh
"""
class Solution:
    def NumberOf1(self, n):
        # write code here负数的补码为其绝对值取反加一
        #-n=~n+1
        mark=1
        if n<0:
            n=~(-n)+1
        return n
if __name__=="__main__":
    line1=int(input())
    s=Solution()
    print(s.NumberOf1(line1))
    
