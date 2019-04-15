# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:49:28 2019

@author: swh
"""

class ListNode:
    def _init(self,value):
        self.val=value
        self.next=None

#合并两个排序的链表
def ordertwolistnode(phead1,phead2):
    if phead1==None and phead2==None:
        return None
    if phead1 and not phead2:
        return phead1
    if phead2 and not phead1:
        return phead1
    mergehead=None
    while phead1!=None and phead2!=None:
        if phead1.val > phead2.val:
            mergehead=phead2
            ordertwolistnode(phead1,phead2.next)
        else:
            mergehead=phead1
            ordertwolistnode(phead1.next,phead2)
    return mergehead
            