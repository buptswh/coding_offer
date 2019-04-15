# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:05:28 2019

@author: swh
"""

#最长不含重复字符的子字符串的长度
"""给定一个字符串，假设字符串只包含'a'~'z'，
思路是记下每个字符出现的最新的位置index，计算当前字符与该字符上一次出现的位置的距离
距离大于当前长度，则说明字符不在当前字符串里出现过,所以当前长度+1
反之，则出现过，当前长度就需要更新为d
"""
def longestsubstr(s):
    if not s:
        return 0
    maxlength,currentlength=0,0
    lis=list("abcdefghijklmnopqrstuvwxyz")
    position={}
    for i in lis:
        position[i]=-1#先把所有字符设定为-1，未出现过
    for i in range(len(s)):
        preindex=position[s[i]]
        if preindex<0 or i-preindex>currentlength:
            currentlength+=1
        else:
            if currentlength>maxlength:
                maxlength=currentlength
            currentlength=i-preindex
        position[s[i]]=i
    if currentlength>maxlength:
        maxlength=currentlength
    return maxlength

if __name__=="__main__":
    ins=input()
    print(longestsubstr(ins))
        
        