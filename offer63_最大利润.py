# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:13:09 2019

@author: swh
"""

'''
股票的最大利润
把股票的价格按照时间顺序存在一个数组中
'''
#购买一次的最大利润
def oneexchange(nums):
    if len(nums)<2:
        return 0
    maxsum=nums[1]-nums[0]
    minprice=nums[0]
    for i in range(2,len(nums)):
        if nums[i-1]<minprice:#更新最小的价格值
            minprice=nums[i-1]
        current=nums[i]-minprice#计算该天能够得到的最大利润
        if current > maxsum:#更新最大利润
            maxsum=current
    return maxsum

if __name__=="__main__":
    x=input()
    if x=='':
        print("输入不规范")
    else:
        nums=[int(s) for s in x.split(',')]
        print(oneexchange(nums))
        