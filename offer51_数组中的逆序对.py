# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:36:43 2019

@author: swh
"""

#数组中的逆序对
#思路：归并排序，将数组从中间拆分成两个子数组，分别排序，计算逆序对，再比较相邻的子数组
class Solution:
    def InversePairs(self, data):
        if not data:
            return 0
        copy = []
        for i in data:
            copy.append(i)
        count=self.InversePairsCore(data,copy,0,len(data)-1)
        return count
    
    def InversePairsCore(self,data,copy,start,end):
        if start==end:
            copy[start]=data[start]
            return 0
        mid=(end-start)>>1
        left = self.InversePairsCore(data,copy,start,start+mid)
        right = self.InversePairsCore(data,copy,start+mid+1,end)
        
        i=start+mid
        j=end
        indexcopy=end
        count=0
        while i >= start and j >= start+mid+1:
            if data[i]>data[j]:
                copy[indexcopy]=data[i]
                i-=1
                indexcopy-=1
                count += j-start-mid
                #右边的子数组已经排好序了，若比data[j]大，就是比j左侧的数都大
            else:
                copy[indexcopy]=data[j]
                j-=1
                indexcopy-=1
        while i >= start:
            copy[indexcopy]=data[i]
            i-=1
            indexcopy-=1
        while j >=start+mid+1:
            copy[indexcopy]=data[j]
            j-=1
            indexcopy-=1
        return left+right+count
if __name__=="__main__":
    ins=input()
    data=[int(s) for s in ins.split(',')]
    en=Solution()
    ans=en.InversePairs(data)
    print(ans)



