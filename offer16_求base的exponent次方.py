# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:26:55 2019

@author: swh
"""
'''给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base==0:
            if exponent>0:
                return 0
            else:
                return 
        else:
            if exponent==0:
                return 1
            elif exponent>0:
                result=1
                for i in range(exponent):
                    result=result*base
                return result
            else:
                result=1
                for i in range(-exponent):
                    result=result*base
                return 1/result
if __name__=="__main__":
    a=input()
    [base,exponent]=[int(s) for s in a.split(',')]
    s=Solution()
    print(s.Power(base,exponent))