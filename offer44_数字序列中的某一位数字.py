# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:11:20 2019

@author: swh
"""
#数字序列中某一位的数字01234567891011121314...
#计算所有的位数之间的数字序列量
class Solution:
    def countofintergers(self,digits):#digits为位数
        if digits==1:
            return 10#一位数字有十个
        count=9*10**(digits-1)#大于一位数字的有3位数有900个
        return count
    
    def beginnumber(self,digits):#n位数的起始数值为1*10**（digits-1），eg:3位数的起始值为100
        if digits==1:
            return 0
        return 10^(digits-1)
    
    def atindex(self,index,digits):
        number = self.beginnumber(digits)+index/digits
        indexfromright=digits-index%digits#为了得到真正的结果，结果是从右移的
        for i in range(1,indexfromright):#除以10的次数，eg:370/10,
            number/=10
        return number%10
    
    def digitatindex(self,index):
        if index<0:
            return -1
        digits=1
        while True:
            nums = self.countofintergers(digits)
            if index < nums*digits:
                return self.atindex(index,digits)#找到了位数
            index -= digits*nums
            digits += 1
        return -1

    
