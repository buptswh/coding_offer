# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:18:23 2019

@author: swh
"""

#最小的k个数，适用于堆排序
# 最大堆，O(nLogk)
import heapq#python中的堆模块，最小堆
def get_least_numbers_big_data(self, alist, k):
    max_heap = []#最小的k个数
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return
    k = k - 1
    for ele in alist:
        ele = -ele
        if len(max_heap) <= k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)#在堆上推送项目，然后弹出并返回堆中的最小项目 

    return map(lambda x:-x, max_heap)#对数据中的数由小到大排序map(fun,seq)


if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    min_k = get_least_numbers_big_data(l, 3)

    