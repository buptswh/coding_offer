# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:50:53 2019

@author: swh
"""

'''
构建乘积数组
A=[A[0],A[1],...,A[n-1]]
构建一个数组B[0,1,2,..,n-1]
其中B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
不能使用除法
思路：分别用1替换A[i]
'''
def savetwoarrays(nums):
    length=len(nums)
    C,D=[0]*length,[0]*length
    for i in range(length):#C[i]=[1,A1,A1A2,...,A1...An-2]
        if i==0:
            C[i]=1
        else:
            C[i]=C[i-1]*nums[i-1]
    for i in range(length-1,-1,-1):#D[i]=[An-1...A2,An-1...A3,...,An-1,1]
        if i==length-1:
            D[i]=1
        else:
            D[i]=D[i+1]*nums[i+1]
    return C,D
            
def multi(nums):
    if not nums:
        return []
    if len(nums)==1:
        return [1]
    C,D=savetwoarrays(nums)
    B=[0]*len(nums)
    for i in range(len(nums)):
        B[i]=C[i]*D[i]
    return B
if __name__=="__main__":
    x=input()
    if x=='':
        print("输入不规范")
    else:
        nums=[int(s) for s in x.split(',')]
        print(multi(nums))
        