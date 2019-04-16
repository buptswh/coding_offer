# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:40:24 2019

@author: swh
"""

'''
队列的最大值
'''
'''
滑动窗口的最大值，给定窗口大小和数组，返回最大值的数组'''
def slidemax(nums,k):
    if not nums or k<=0:
        return []
    if len(nums)==1 or k>len(nums):
        return nums
    temp=[0]
    res,length=[],len(nums)
    for i in range(length):
        # 判断第 i 个元素是否可以加入 temp 中
        # 如果比当前最大的元素还要大，清空 temp 并把该元素放入数组
        # 首先判断当前最大的元素是否过期
        if i -temp[0] > k-1:
            temp.pop(0)
        # 将第 i 个元素与 temp 中的值比较，将小于 i 的值都弹出
        while (len(temp)>0 and nums[i] >= nums[temp [-1]]):
            temp.pop(-1)
        # 如果现在 temp 的长度还没有达到最大规模，将元素 i 压入
        if len(temp)< k-1:
            temp.append(i)
        # 只有经过一个完整的窗口才保存当前的最大值
        if i >=k-1:
            res.append(nums[temp [0]])
    return res
"""
定义一个队列，并实现函数max得到队列里的最大值，要求函数max、pushback、popfront的
时间复杂度都是O(1)
"""
class InternalData:
    def _int(self,x,currentindex):
        self.val=x
        self.index=currentindex
class DefinQueue:
    data=[]
    maximums=[]
    currentindex=0#给一个index值
    
    def push_back(self,number):
        while len(self.maximums)>0 and number>self.maximums[-1]:
            #把小于当前值的元素都弹出
            self.maximums.pop()
        internaldata=InternalData._int(number,self.currentindex)#数据结构，存值和索引
        self.data.append(internaldata)
        self.currentindex+=1#每次压入一个新的值都更新一次
    def pop_front(self):
        if len(self.maximums)==0:
            raise Exception("queue is empty")
        if self.maximums[-1].index==self.data[0].index:
            #如果弹出的值和当前值的索引一致，就更新最大值栈里的值
            self.maximums.pop(0)
        self.data.pop(0)#此时data里面不可能出来
    def maxpeek(self):
        if len(self.maximums)==0:
            raise Exception("queue is empty")
        return self.maximums[-1].val
            
        

if __name__=="__main__":
    a=input().split(',')
    x=input()
    if x !='' and a!='':
        k=int(x)
        nums=[int(s) for s in a]
        res=slidemax(nums,k)
        print(res)
    else:
        print([])
     
    
    
