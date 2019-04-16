# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:09:54 2019

@author: swh
"""

'''
把字符串换成整数eg:'123'-->123 
'''
#空指针，字符串不存在，非法输入，溢出
class Solution:
    def StrToInt(self, s):
        res,mult,flag = 0,1,1
        if not s:
            return res
        if s[0] == '-' or s[0] == '+':#判定符号
            if s[0] == '-':
                flag = -1
            s = s[1:]
        for i in range(len(s)-1, -1, -1):
            if '9' >= s[i] >= '0':
                res += (ord(s[i]) - 48)*mult#'0'的Unicode是48，转换为正整数
                mult = mult * 10
            else:
                return 0
        return res*flag