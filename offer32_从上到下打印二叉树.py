# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:25:54 2019

@author: swh
"""

"""从上到下打印二叉树广度优先遍历"""
class Node:
    def _init(self,x):
        self.val=x
        self.left=None
        self.right=None
def printTreeUd(root):
    if not root:
        return
    nodes=[root]
    while nodes:
        x=[]
        for node in nodes:
            print(node.val)
            if node.left:
                x.append(node.left)
            if node.right:
                x.append(node.right)
                
"""按行打印二叉树
思路：按行打印的时候相当于需要记录两个数值：当行打印剩余的节点数量，下一行要打印的数量 """
class Solution:
    def printinline(self,root):
        if root==None:
            return 
        current=1
        nextfloor=0
        sequence=[root]
        while current !=0 or nextfloor !=0:
            pnode=sequence[0]
            print(pnode.val)
            if pnode.left:
                sequence.append(pnode.left)
                nextfloor+=1
            if pnode.right:
                sequence.append(pnode.right)
                nextfloor+=1
            sequence.pop(0)
            current-=1
            if current==0:
                print('\n')
                current=nextfloor
                nextfloor=0
            
    """之字形打印二叉树
    之字形，也就是一行从左到右，下一行从右到左，
    需求两个栈，一个用来存储当前层的节点
    一个存储下一层的节点
    """
    def zhiprint(self,root):
        floor=[]
        current=0
        nextf=1
        floor[0]=[root]
        floor[1]=[]
        while len(floor[0])!=0 or len(floor[1])!=0:
            node=floor[current][0]
            print(node.val)
            if current==0:#从左往右，压栈
                if node.left!=None:
                    floor[nextf].append(node.left)
                if node.right!=None:
                    floor[nextf].append(node.right)                
            else:
                if node.right!=None:
                    floor[nextf].append(node.right)
                if node.left!=None:
                    floor[nextf].append(node.left)
            floor[current].pop()
            if len(floor[current])==0:
                print('\n')
                current=1-current
                nextf=1-nextf
                
                
            
            