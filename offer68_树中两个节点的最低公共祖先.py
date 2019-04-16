# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:33:48 2019

@author: swh
"""
'''
求树中两个节点的最低公共祖先
树：什么树，二叉树，二叉搜索树，普通的树
最低公共祖先：
链表的公共节点
辅助内存的申请？
便利到一个节点的时间复杂度O(n)
一条路径的长度普遍是O(logn),最差在O(n)
'''
class Treenode:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
        
def LowestParent(root,p,q):
    stack=[root]
    par_child={root:None}
    while stack:
        node=stack.pop()
        if node.left:
            par_child[node.left]=node
            stack.append(node.left)
        if node.right:
            par_child[node.right]=node
            stack.append(node.right)
    res=set()
    while p:
        res.add(p)
        p=par_child[p]
    while q not in res:
        q=par_child[q]
    return q

