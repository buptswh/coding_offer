# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:17:17 2019

@author: swh
"""

"""
需求：输入两个整数序列，第一个序列是栈的压入顺序，判断第二个是不是栈的弹出顺序
注意：栈的弹出操作中中可能存在压入动作
"""
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack=[]
        while len(popV)!=0:
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
                
if __name__=="__main__":
    push=input()
    pushV=push.split(',')
    pop=input()
    popV=pop.split(',')
    c=Solution()
    print(c.IsPopOrder(pushV,popV))