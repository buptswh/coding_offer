# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:32:32 2019

@author: swh
"""

"""
需求：求一棵二叉树的镜像
"""
class TreeNode:
    def _int(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def mirror(self,root):
        if root==None:
            return
        if root.left==root.right and root.left==None:
            return
        ptemp=root.left
        root.left=root.right
        root.right=ptemp
        if root.left:
            self.mirror(root.left)
        if root.right:
            self.mirror(root.right)