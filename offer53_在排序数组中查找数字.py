# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:27:39 2019

@author: swh
"""
"""在排序数组中查找数字"""
"""思路，二分查找第一个出现的index和最后一个index，总的时间复杂度依然是O(logn)"""
class SearchinArray:
    
    #数字在排序数组中出现的次数
    def timesinarray(self,nums,target):
        if not nums:
            return 0
        first,last=-1,-1
        #找第一个出现target的index
        start,end=0,len(nums)-1
        while start<=end:
            mid=(end+start)>>1
            if nums[mid]==target:
                if (mid>0 and nums[mid-1]!=target) or mid==0:
                    first=mid
                    break
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        #找最后一个出现target的index
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)>>1
            if nums[mid]==target:
                if (mid<len(nums)-1 and nums[mid+1]!=target) or mid==len(nums)-1:
                    last=mid
                    break
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        print("first="+str(first))
        print("last="+str(last))
        if first>-1 and last>-1:
            return last-first+1
        else:
            return 0
    
    def test(self,nums,target):
        ans=0
        for num in nums:
            if num==target:
                ans+=1
        return ans


            
            
    #0~n-1中缺失的数字,长度为n-1的递增排序的数组中所有的数都是唯一的，每个数字都在0~n-1范围内
    def missingnumber(self,nums):
        if not nums:
            return -1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)>>1
            if nums[mid]!=mid:
                if mid==0 or nums[mid-1]==mid-1:
                    return mid
                else:
                    end=mid-1
            else:
                start=mid+1
        if start==len(nums):
            return len(nums)
            
    #数组中数值和下标相等的元素,数组单调递增，且每个元素唯一
    def equalasindex(self,nums):
        if not nums:
            return -1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)>>1
            if nums[mid]==mid:
                return mid
            elif nums[mid]>mid:
                end=mid-1
            else:
                start=mid+1
        return -1
if __name__=="__main__":
    x=input()
    if x=='':
        print("invalid input")
    else:
        s=[int(a) for a in x.split(',')]
    #    target=int(input())
        ins=SearchinArray()
    #    print(ins.test(s,target))
    #    print(ins.timesinarray(s,target))
        #print(ins.missingnumber(s))
        print(ins.equalasindex(s))
        
        
##在排序数组中查找数字
#'''
#数字在排序数组中出现的次数
#考虑利用二分法得到数组中的第一个k和最后一个k
#'''
#def getfirstk(nums,k):
#    if not nums or len(nums)==0:
#        return
#    start,end=0,len(nums)-1
#    mid=(start+end)>>2
#    if nums[mid]>k:
#        start=mid-1
#    elif nums[mid]<k:
#        end=mid+1
#    else:
#        if (mid>0 and nums[mid-1]!=k) or mid==0:
#            return mid
#        else:
#            end=mid-1
#        
#    
#def getlastk(nums,k):
#    if not nums or len(nums)==0:
#        return
#    n=len(nums)
#    start,end=0,n-1
#    mid=(start+end)>>2
#    if nums[mid]>k:
#        end=mid-1
#    elif nums[mid]<k:
#        start=mid+1
#    else:
#        if (mid<n-1 and nums[mid+1]!=k) or mid==n-1:
#            return mid
#        else:
#            start=mid+1
#def getnumsofk(nums,k):
#    num=0
#    if nums and len(nums)>0:
#        first=getfirstk(nums,k)
#        last=getlastk(nums,k)
#        if first>-1 and last>-1:
#            num=last-first+1
#    return num