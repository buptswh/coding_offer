# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:56:31 2019

@author: swh
"""

#二叉树中和为n的路径(从根节点到叶节点的一条路)
"""递归思想，把复杂的树简化成一颗简单的树，则进行递归"""
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None


def function(root,target_number): 
    result = [] 
    if not root: 
        return result 
#  如果只有根节点或者找到叶子节点，我们就把其值返回 
    if not root.left and not root.right and root.val == target_number: #对当前节点进行判断
        return [[root.val]] 
    else: 
#  如果不是叶子节点，我们分别对根节点的左子树、右子树进行递归，注意修改变量: 
        left = function(root.left,target_number - root.val) 
        right = function(root.right,target_number - root.val) 
        for item in left+right:
          result.append([root.val]+item) 
        return result
    