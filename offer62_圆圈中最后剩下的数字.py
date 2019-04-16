# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:44:01 2019

@author: swh
"""

'''
圆圈中最后剩下的数字
0，1，2，...,n-1这n个数字排成一圈，
每次从这个圆圈里删除第m个数字，
求圆圈里最后剩下的数字
映射关系p(x)=(x-k-1)%n
逆映射为h(x)=(x+k+1)%n
根据k=(m-1)%n
f(n,m)=h(f(n-1,m)=(f(n-1,m)+k+1)%n
得到
f(n,m)=[f(n-1,m)+m]%n
'''

class Solution:
    def LastRemainingSolution(self,n,m):
        if n < 1:
            return -1
        con = range(n)
        final = -1
        start = 0
        while con:#直到这个n个值没有了
            k = (start + m - 1) % n#第m个就是start+m-1
            final = con.pop(k)#记录弹出的值
            n -= 1
            start = k#产出之后更新为这个值开始
        return final

if __name__=="__main__":
    x=input()
    if x!='':
        [n,m]=[int(s) for s in x.split(',')]
        ans=Solution.LastRemainingSolution(n,m)
        print(ans)
    else:
        print("输入不规范")