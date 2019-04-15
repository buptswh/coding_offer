# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:47:42 2019
@author: swh
"""

#字符串的所有排列
from copy import deepcopy

def isduplicate(li, n, t):
    """
    从li的位置n到位置t-1，有没有和li[t]相等的数字
    """
    while n < t:
        if li[n] == li[t]:
            return True
        n += 1
    return False

def swap(li, i, j):
    if i == j:
        return
    temp = li[j]
    li[j] = li[i]
    li[i] = temp

def permutation(li, size, n, result):
    """
    [n,size]位置的数字全排
    :param li:字符串数组
    :param size: 字符串长度
    :param n: 要交换的位置
    :param result: 保留结果
    :return:
    """

    if n == size - 1:
        result.append(deepcopy(li))
        return
    for i in list(range(n, size)):  # 分别把(size-n)个数字固定到位置n
        if isduplicate(li, n, i):  # 如果位置n出现过数字li[i]，跳过
            continue
        swap(li, i, n)  # 把s[n]和s[i]交换，把s[i]固定到位置n
        permutation(li, size, n + 1, result)  # [n+1,size-1]位置的数字全排
        swap(li, i, n)  # 把s[n]和s[i]交换回来
        
        
if __name__ == '__main__':
    li = [1, 2, 2, 3]
    if li==None:
        print([])
    size = len(li)
    n = 0
    result = []
    permutation(li, size, n, result)
    for i in result:
        print(i)

        