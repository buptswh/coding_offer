# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:21:52 2019
@author: swh
"""

#数组中出现次数超过一半的数字,快速排序后数组的中位数
"""
整个过程中保留两个值，一个是value，一个是count。当value的值再次出现则count值+1，
如果count>0的时候,遇到一个和value值不同的数就可以将count-1.
当count=0又碰到了和value值不一样的值就可以将value更新为新的值，并且把count设为1.
时间复杂度为O(n)
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        checkNum = numbers[0]
        count = 1
        for n in numbers[1:]:
            if n == checkNum or count == 0:
                count += 1
                checkNum = n
            else:
                count -= 1
        return checkNum
    
if __name__=="__main__":
    ins=input()
    entry=Solution()
    if ins=='':
        print("invalid input")
    else:
        numbers=[int(a) for a in ins.split(',')]
        print(entry.MoreThanHalfNum_Solution(numbers))
    
    