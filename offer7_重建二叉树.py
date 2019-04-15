# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:32:01 2019

@author: swh
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def reConstructBinaryTree(pre, tin):
    # write code here
    if len(pre)<1 or len(tin)<1 or len(pre)!=len(tin):
        return "invalid input"
    return reconstrucrtree(pre,tin)
def reconstrucrtree(pre,tin):
    prestart,preend=0,len(pre)-1
    tinstart,tinend=0,len(tin)-1
    rootval=pre[prestart]
    root = TreeNode(rootval)
    root.left=None
    root.right=None
    
    if prestart==preend:
        if tinstart==tinend and prestart==tinstart:
            return root
        else:
            return "invalid input"
    inorder=tinstart
    while inorder<=tinend and tin[inorder]!=pre[prestart]:
        inorder+=1
    if inorder==tinend and tin[inorder]!=pre[prestart]:
        return "invalid input"
    if inorder>tinstart:
        root.left=reConstructBinaryTree(pre[1:inorder+1],tin[:inorder])
    if inorder<tinend:
        root.right=reConstructBinaryTree(pre[inorder+1:],tin[inorder+1:])
    return root
if __name__=="__main__":
    a = input()
    b = input()
    if not a or not b:
        print("invalid input")
    else:
        pre=[int(s) for s in a.split(',')]
        tin=[int(s) for s in b.split(',')]
        if len(pre)!=len(tin):
            print("invalid input")
        else:
            ans=reConstructBinaryTree(pre,tin)
            print(ans.val)
            print(ans.left.val)
            print(ans.right.val)