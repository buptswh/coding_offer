# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:28:36 2019

@author: swh
"""

def maxsubsum(nums):
    if not nums:
        return
    if len(nums)==1 and nums[0]<0:
        return nums[0]
    currentsum,maxsum=0,0
    for num in nums:
        if currentsum<0:
            currentsum=0
        currentsum+=num
        if currentsum>maxsum:
            maxsum=currentsum
    return maxsum
if __name__ == "__main__":
    ins=input()
    if len(ins)>0:
        nums=[int(a) for a in ins.split(' ')]
        print(maxsubsum(nums))
    else:
        print("无效输入")