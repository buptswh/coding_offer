# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:39:32 2019

@author: swh
"""

"""
二叉树是否对称
"""
class Solution:
    def isSymmetrical(self,root):
        return self.issymme(root,root)
    def issymme(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val!=root2.val:
            return False
        return self.issymme(root1.left,root2.right) and self.issymme(root1.right,root2.left)