# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:48:11 2019

@author: swh
"""

class ListNode:
    def _init(self,value):
        self.val=value
        self.next=None
#链表中环的入口点
def circlemeet(phead):
    if not phead:
        return None
    slow=phead.next
    if slow==None:
        return None
    fast=slow.next
    while fast!=None and slow!=None:
        if fast==slow:
            return fast
        slow=slow.next
        fast=fast.next
        if fast!=None:
            fast=fast.next
    return None
def corclein(phead):
    meetnode=circlemeet(phead)
    if meetnode==None:
        return None
    node1=phead
    nodesinloop=1
    while node1.next!=meetnode:
        node1=node1.next
        nodesinloop+=1
    node1=phead
    for i in range(nodesinloop):
        node1=node1.next
    node2=phead
    while node1!=node2:
        node1=node1.next
        node2=node2.next
    return node1