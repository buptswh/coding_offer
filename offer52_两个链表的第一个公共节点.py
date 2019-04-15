# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:47:51 2019

@author: swh
"""
#两个链表的第一个公共节点
"""
思路：从链表尾部开始，从后往前，但是链表只能从头结点开始读取
所以先遍历得到链表的长度，取长度差k，定义两个指针，一个先走k步
"""
class ListNode:
    def _init(self,x):
        self.val=x
        self.next=None
class Solution:       
    #先得到两个链表的长度，先在长的链表上多走几步
    def listlength(self,list1):
        length=0
        while list1.next:
            length+=1
            list1=list1.next
        return length
    def firstcommon(self,list1,list2):
        if not list1 or not list2:
            return
        len1,len2=self.listlength(list1),self.listlength(list2)
        dif=len1-len2
        common=None
        if dif > 0:
            for i in range(dif):
                list1=list1.next
        else:
            for i in range(dif):
                list2=list2.next
                
        if not list1 or list2:#再次判断是否为空
            return
        while list1 and list1.next:
            if list1.val == list2.val:
                common=list1
        return common
    