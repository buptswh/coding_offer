# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:54:34 2019

@author: swh
"""

#数据流中的中位数
#笨方法
#！左边一个最大堆，右边一个最小堆
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.nums = []
    def Insert(self, num):
        self.nums.append(num)
    def GetMedian(self, fuck):
        self.nums.sort()
        if len(self.nums) % 2 == 1:
            return self.nums[(len(self.nums) - 1) / 2]
        else:
            return (self.nums[len(self.nums) / 2] + self.nums[len(self.nums) / 2 - 1]) / 2.0
 '''       

import heapq

class Solution2:
    nums = []
    def Insert(self, num):
        heapq.heappush(self.nums, num)

    def GetMedian(self):
        mid = len(self.nums)>>1
        return (heapq.nlargest(mid, self.nums)[-1] + heapq.nsmallest(mid, self.nums)[-1])/2.0
    #[:mid]两个函数的作用区间
if __name__=="__main__":
    heap=Solution2()
    while True:
        s=input()
        if s=='':
            break
        else:
            heap.Insert(int(s))
    ans=heap.GetMedian()
    print(ans)
        
