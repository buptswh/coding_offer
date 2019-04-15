# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:15:01 2019

@author: swh
"""

#序列化二叉树
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
#序列化    前序遍历
def Serializepre(self, root):
    if not root:
        return '$'
    return str(root.val) +',' + self.Serializepre(root.left) +','+ self.Serializepre(root.right)

#反序列化
def Deserialize(self, s):
    lis = s.split(',')
    return self.deserializeTree(lis)
 
def deserializeTree(self, lis):
    if len(lis)<=0:
        return None
    val = lis.pop(0)
    root = None
    if val != '$':
        root = Node(int(val))
        root.left = self.deserializeTree(lis)
        root.right = self.deserializeTree(lis)
    return root

    