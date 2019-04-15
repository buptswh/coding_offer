# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:29:04 2019

@author: swh
"""
"""
需求：合并两个递增排序的链表
输入：两个链表的头结点
输出：合并链表的头结点
思路：递归：先判断链表的存在，并比较大小
"""
class ListNode:
    def _init(self,x):
        self.val=x
        self.next=None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        mergehead=None
        if pHead1==None:
            return pHead2
        elif pHead2==None:
            return pHead1
        else:
            if pHead1.val < pHead2.val:
                mergehead=pHead1
                self.Merge(pHead1.next,pHead2)
            else:
                mergehead=pHead2
                self.Merge(pHead1,pHead2.next)
            return mergehead
            