# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:30:52 2019

@author: swh
"""
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        if len(rotateArray)==1:
            return(rotateArray[0])
        low,high=0,len(rotateArray)-1
        while low<high:
            mid=(low+high)//2
            if high==low+1:
                if rotateArray[low]>rotateArray[high]:
                    return rotateArray[high]
                else:
                    return rotateArray[low]
            if rotateArray[mid]<rotateArray[low]:
                high=mid
            else:
                low=mid
if __name__=="__main__":
    s=Solution()
    
    a=input()
    if a =="":
        print(0)
    else:
        lis=[int(m) for m in a.split(',')]
        ans=s.minNumberInRotateArray(lis)
        print(ans)
            