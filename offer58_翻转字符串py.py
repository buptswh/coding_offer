# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:35:09 2019

@author: swh
"""

#翻转字符串

class Solution:
    '''
    i am a student.-->student. a am i
    首先翻转整个字符串，然后将字符串局部进行翻转
    用指针进行字符串的扫描pdata是字符串的头指针
    python的字符串不能按照a[1]=''赋值，string是一个静态变量
    '''
    def reverse(self,begin,end,s):#s是一个list，eg:['a', 'v', 'c']
        if  begin<0 or begin>len(s)-1 or end>len(s)-1 or end<begin:
            return None
        while begin<end:
            temp=s[begin]
            s[begin]=s[end]
            s[end]=temp
            begin+=1
            end-=1
    def reverseSentense(self,s):
        if s=='':
            return ''
        res=list(s)
        begin,end=0,len(res)-1
        self.reverse(begin,end,res)#整个字符串翻转
        #print("翻转一次"+str(res))
        begin=end=0
        while begin<len(res) and end<len(res):
            if res[begin]==" ":
                begin+=1
                end+=1
            elif end==len(res)-1:
                self.reverse(begin,end,res)
                end+=1
                begin=end
            elif res[end]==" " :
                self.reverse(begin,end-1,res)
                end+=1
                begin=end
            else:
                end+=1
        ans=''.join(res)
        return ans
    '''左旋转字符串
    将字符串前面若干个字符转移到尾部
    eg:
        abcdefg,2-->cdefgab
        先将字符串分为两部分，ab,cdefg，对这两个部分分别翻转，得到bagfedc
        再反正整个字符串即可得到cdefgab'''
        
    def leftreverse(self,begin,end,s):
        if not begin or not end:
            return
        if begin<end:
            temp=s[begin]
            s[begin]=s[end]
            s[end]=temp
            begin+=1
            end-=1
    def leftrotatestring(self,string,n):
        if string=='' or n<0 or n>len(string):
            return None
        length=len(string)
        string=list(string)
        if string and n>0 and n<length:
            firststart=0
            firstend=firststart+n-1
            secondstart=firststart+n
            secondend=length-1
            self.leftreverse(firststart,firstend,string)
            self.leftreverse(secondstart,secondend,string)
            self.leftreverse(firststart,secondend,string)
        ans=''.join(string)
        return ans
if __name__=="__main__":
    ins=input()
    en=Solution()
    print(en.reverseSentense(ins))
    