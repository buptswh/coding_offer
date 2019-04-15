# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:48:51 2019

@author: swh
"""

class ListNode:
    def _init(self,value):
        self.val=value
        self.next=None
#反转链表
def reverselistnode(phead):
    reversehead=None
    pnode=phead
    prev=None
    if phead == None:
        return None
    if phead and phead.next==None:
        return phead
    while pnode!=None:
        pnext=pnode.next
        if pnext==None:
            reversehead=pnode
        pnode.next=prev
        pnode=pnext
        prev=pnode
    return reversehead