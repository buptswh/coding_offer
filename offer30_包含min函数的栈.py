# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:05:42 2019

@author: swh
"""

"""
需求：用栈实现一个min，pop,push函数，时间复杂度都是1
思路：添加一个辅助栈，存储栈内的最小值
时间复杂度：O（1）
空间复杂度：O(n）
"""
class Solution:
    stack=[]
    minstack=[]
    def min(self,minstack,stack):
        if len(minstack)==0:
            return None
        else:
            minstack.peek()
        
    def pop(self,minstack,stack):
        if len(stack)>0 and len(minstack)>0:
            stack.pop()
            minstack.pop()
        else:
            return None
    def push(self,minstack,stack,x):
        if len(stack)==0 and len(minstack)==0:
            stack.push(x)
            minstack.push(x)
        else:
            stack.push(x)
            mincurrent=minstack.peek
            if x<mincurrent:
                minstack.push(x)
            else:
                minstack.push(mincurrent)