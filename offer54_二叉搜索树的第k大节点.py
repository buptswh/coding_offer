# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:46:51 2019

@author: swh
"""

#中序遍历即得
class TreeNode:
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def inorder(root,k):
        if not root or k <=0:
            return None
        return Solution.kthnode(root,k)
    def kthnode(node,k):
        target=None
        if node.left:
            target=Solution.kthnode(node.left,k)
        if target == None:
            if k==1:
                target=node
            k-=1
        if node.right and target==None:
            target = Solution.kthnode(node.right,k)
        return target
        
            