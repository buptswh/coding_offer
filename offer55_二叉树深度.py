# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:17:50 2019

@author: swh
"""

#二叉树的深度
#从最简单的开始分析：只有root 值为1；只有左子树，左子树+1；只有右子树，右子树+1,既有左子树又有右子树，较大值+1
class TreeNode:
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def depthoftree(self,root):
        if not root:
            return 0
        nleft=Solution.depthoftree(root.left)
        nright=Solution.depthoftree(root.right)
        if nleft>nright:
            return nleft+1
        else:
            return nright+1
        
    #平衡二叉树的判定
    def height(self,root):
        if not root:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        if left == -1 or right == -1 or left-right > 1 or right-left > 1:
            #不平衡的条件，子树不平衡或者自身不平衡
            return -1 
        return max(left,right) + 1#子树的最大深度
    def isbalanced(self,root):
        ans=self.height(root)
        return ans!=-1
        