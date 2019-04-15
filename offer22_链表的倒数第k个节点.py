# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:22:36 2019

@author: swh
"""

#链表倒数第k个节点
#思想是定义两个指针，一个指针先走k-1步
#，然后两个指针一起走，直到第一个指针指向最后一个节点的时候，返回第二个指针指向的值
class ListNode:
    def _init(self,value):
        self.val=value
        self.next=None
def kinlist(phead,k):
    if phead==None or k<1:
        return
    first,sec=phead,phead
    for i in range(k):
        if first.next:
            first=first.next
        else:
            return
    while first.next!=None:
        first=first.next
        sec=sec.next
    return sec





        
    
    
    
                   