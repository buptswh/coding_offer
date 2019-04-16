# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:38:23 2019

@author: swh
"""
"""
写一个函数，求两个整数之和，要求在函数体内不能使用+-*/四则运算符号
思路：位运算
"""
def sumor(m,n):
    sume=m^n
    carry=(m&n)<<1
    while n!=0:
        m=sume
        n=carry
    return m
if __name__=="__main__":
    ins=input()
    if ins=="" or len(ins)<3:
        raise Exception("invalid input")
    [m,n]=[int(i) for i in ins.split(',')]
    print(sumor(m,n))