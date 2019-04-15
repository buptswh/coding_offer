# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:46:43 2019

@author: swh
"""
"""
需求：求中序遍历的二叉树的下一个节点
输入：树节点有左节点指针、右节点指针、父节点指针
思路：
    对当前节点进行分类讨论：
        有右子树的情况：下一个节点就是右子树的最左子节点
        没有右子树的情况：下一个节点是为一个节点的左子节点的父节点
        
"""
class TreeNode:
    def _init_(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.parent=None
        
class Solution:
    def nextnode(self,pnode):
        if pnode==None:
            return None
        pnext=None
        if pnode.right!=None:
            pright=pnode.right
            while pright.left!=None:
                pright=pright.left
            pnext=pright
        elif pnode.parent!=None:
            parent=pnode.parent
            current=pnode
            while parent!=None and current==parent.right:
                current=parent
                parent=parent.parent
            pnext=parent
        return pnext
