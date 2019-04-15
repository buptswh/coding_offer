# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:11:00 2019

@author: swh
"""

"""
把数组排成最小的数
需求：输入一个整数数组，把数组里所有的数字拼接起来排成一个最小的数，
     打印能拼接出来的所有数字中最小的一个
输入：一个整数数组
输出：最小的数
思路：重新定义一个排序规则：连接两个数（转换成字符串后），比较mn和nm
"""
class Solution:
    def swap(self,nums,i,j):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
    def compare(self,num1,num2):
        strnum1,strnum2=str(num1),str(num2)
        s1=strnum1+strnum2
        s2=strnum2+strnum1
        if s1<=s2:
            return True
        return False
    def quicksort(self,nums,start,end):
        if start<end:
            i,j=start,end
            base=nums[start]
            while i<j:
                while i<j and self.compare(base,nums[j]):
                    j-=1
                nums[i]=nums[j]
                while i<j and self.compare(nums[j],base):
                    i+=1
                nums[j]=nums[i]
            nums[i]=base
            self.quicksort(nums,start,i-1)
            self.quicksort(nums,j+1,end)
        return nums
    def concat_min_num(self,nums):
        if len(nums)<1:
            return ''
        elif len(nums)==1:
            return nums[0]
        else:
            res=self.quicksort(nums,0,len(nums)-1)
            ans=''
            for num in res:
                ans+=str(num)
            return ans
if __name__=="__main__":
    s=input()
    if s!='':
        nums=s.split(',')
        ins=Solution()
        print(ins.concat_min_num(nums))
    else:
        print("invalid input")
            