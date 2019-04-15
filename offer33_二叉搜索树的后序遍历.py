# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:33:08 2019

@author: swh
"""

#二叉搜索树的后序遍历,左右根
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
        
#def postorderBST(root):
#    if not root:
#        return None
#    if root.left:
#        postorderBST(root.left)
#    if root.right:
#        postorderBST(root.right)
#    return root.val

#输入一个数组，判断它是否为一个二叉搜索树的后序遍历
def isBST(nums):
    if not nums:
        return False
    n=len(nums)
    root=nums[n-1]
    i=0
    while i < n-1:
        if nums[i]>root:
            break
        i+=1
    j=i
    for j in range(j,n-1):
        if nums[j]<root:
            return False
    if i>0:
        left = isBST(nums[:i])
    if i< n-1:
        right = isBST(nums[i:n-1])
    return left&right
    