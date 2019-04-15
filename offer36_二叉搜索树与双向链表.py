# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:44:02 2019

@author: swh
"""
#二叉搜索树与双向链表,排序，不能创建新的节点，只调整树指针的指向
#BST的双向，中序遍历，拆分成根节点，左子树，右子树。
#有左子树就把左子树的最后一个节点和根节点连接起来
#记录上一个最后的节点（即为根节点），递归处理右子树
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
        

def convertnode(root):
    if not root:
        return 
    current=root
    if current.left:
        lastnode=convertnode(current.left)
    current.left=lastnode#与左子树的最大节点连接起来，当前节点的左指针指向左子树最大节点
    if lastnode:
        lastnode.right=current#双向，最大节点的右指针指向根节点
    lastnode=current#最后的节点更新为根节点
    if root.right:#递归右子树
        convertnode(current.right)
        
def treetolist(root):
    lastnode=None
    lastnode=convertnode(root)
    firstnode=lastnode
    while firstnode and firstnode.left:#循环一遍找到最左侧的头结点。
        firstnode=firstnode.left
    return firstnode
