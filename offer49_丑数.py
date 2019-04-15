# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:17:19 2019

@author: swh
"""

#丑数：只包含因子2，3，5的数称为丑数。求按从小到大的顺序的第1500个丑数，1是第一个丑数
def isugly(num):
    while num%2==0:
        num>>2
    while num%3==0:
        num/=3
    while num%5==0:
        num/=5
    if num==1:
        return True
    else:
        return False

def getuglynum(n):
    if n<=0:
        return 0
    uglyindex,i=0,0
    while uglyindex<n:
        i+=1
        if isugly(i):
            uglyindex+=1
    return i
'''
第二种思路，从1开始，后面的丑数只可能是它的2^x,3^x,5^x倍，
所以建立一个数组存下顺序的丑数值，计算*2能大于当前max值的M2,M3,M5

此方法有O(n)的空间消耗，但是会比上述方法快一些。
'''