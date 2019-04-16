# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:20:25 2019

@author: swh
"""
'''
扑克牌中的顺子
从扑克中抽出5张牌，判断它是否为顺子
2~10为数字，A为1，J为11，Q为12，K为13，大小王为任意数字
思路：
1.将数组排序，一共才五张，可以接受时间复杂度
2.统计0（大小王）的数量m
3.统计不连续的数量n
4.判断以上两个数量是否满足条件m>=n
'''
def isContinues(nums):
    if not nums or len(nums)<5:#判定是否有五张牌
        return False
    nums.sort()#1，排序
    numofzero,numofgap=0,0#初始化两个数字
    for i in range(len(nums)):
        if nums[i]==0:
            numofzero+=1
    small=numofzero#标记第一个不为0的值
    big=small+1#从第二个不为0的值开始
    while big<len(nums):
        if nums[small]==nums[big]:#有对子，就不可能存在顺子
            return False
        numofgap+=nums[big]-nums[small]-1
        small=big
        big+=1
    if numofzero>=numofgap:
        return True
    else:
        return False
    
if __name__=="__main__":
    a=input()
    if a=='':
        print("输入不规范")
    else:
        k=a.split(',')
        nums=[int(s) for s in k]
        ans=isContinues(nums)
        print(ans)