# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:10:36 2019

@author: swh
"""
"""
第一个只出现一次的字符
字符串中第一个只出现一次的字符
思路：hashtable:key值在存储空间中是保留其添加顺序的
"""
class Solution:
    def firstchar(string):
        dic={}
        for i in string:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            if dic[i]==1:
                return i
        return ''
"""字符流中第一个只出现一次的字符
"""
class firstinstream:
    dic={}
    index=0
    for i in range(256):
        dic[i]=-1
    def insert(self,ch):
        if self.dic[ord(ch)]==-1:
            self.dic[ord(ch)]=self.index
            self.index+=1
    def firstchar(self):
        ch=''
        for i in self.dic:
            if self.dic[i]>=0 and self.dic[i]<self.index:
                ch=i
        return ch
    