# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:15:37 2019
复制复杂链表
@author: swh
"""

"""
第一种思路：先遍历一遍链表，复制self.next，然后寻找每一个节点的复杂指向指针o(n^2)
第二种思路：复制一遍链表，把链表复制的对应关系存储起来，<N,N'>hashtable,然后复制o(n)
第三种思路：复制链表的节点直接跟在原链表相同节点的后面，A->A'->B->B'...
再链表分割开来，奇数位置的节点连接起来即为原链表，偶数位的链表连接起来就是复制链表o(n)
"""


class complexlist:
    def _init(self,x):
        self.val=x
        self.next=None
        self.complex=None
        
def copycomplex(phead):
    if not phead:
        return None
    #首先复制节点，并且插入链表中
    clonenode=None
    pnode=phead
    while pnode:
        clonenode.val=pnode.val
        clonenode.next=pnode.next
        clonenode.complex=None
        pnode.next=clonenode
        pnode=clonenode.next
    #复制复杂指针
    complexnode=phead
    while complexnode:
        comclone=complexnode.next
        if complexnode.complex!=None:
            comclone.complex=complexnode.complex.next
        complexnode=comclone.next
    #抽出新的链表
    pnode=phead
    pclone=None
    clonehead=None
    if pnode:
        clonehead=pclone=pnode.next#复制头
        pnode.next=pclone.next#复制到原链表的下一节点
        pnode=pnode.next#遍历下一个原链表的节点
    while pnode:
        pclone.next=pnode.next#得到复制链表的下一节点
        pclone=pclone.next#遍历复制链表的下一节点
        pnode.next=pclone.next#得到原链表的下一节点
        pnode=pnode.next#遍历原链表的下一节点
    return clonehead
        
        
        
        
        