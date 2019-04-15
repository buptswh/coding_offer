# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:50:15 2019

@author: swh
"""

#树的子结构判定
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
def isSubTree(root1,root2):
    if root1 == None:
        return False
    if root2 == None:
        return True
    result=False
    while root1!=None and root2!=None:
        if root1.val==root2.val:
            result=equtree(root1,root2)
        if not result:
            result=isSubTree(root1.left,root2)
        if not result:
            result=isSubTree(root1.right,root2)
            
            
def equtree(tree1,tree2):
    if tree2==None:
        return True
    if tree1==None:
        return False
    if tree1.val!=tree2.val:
        return False
    return equtree(tree1.left,tree2.left)&equtree(tree1.right,tree2.right)
        