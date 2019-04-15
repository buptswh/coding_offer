# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:29:02 2019

@author: swh
"""

#把数字翻译成字符串
class StrtoNum:
    def gettranslationcount(self,nstr):
        length=len(nstr)
        counts=[0]*length
        for i in range(length-1,-1,-1):
            count=0
            if i < length-1:
                count=counts[i+1]
            else:
                count=1
            if i < length -1:
                digit1=int(nstr[i])
                digit2 = int(nstr[i+1])
                convert=digit1 *10+digit2
                if convert>=10 and convert<=25:
                    if i < length-2:
                        count+=counts[i+2]
                    else:
                        count+=1
            counts[i]=count
        return counts[0]
    
    def numtostr(self,nums):
        if nums<0:
            return 0
        nstr=str(nums)
        return self.gettranslationcount(nstr)
    
if __name__=="__main__":
    ins=int(input())
    s=StrtoNum()
    
    print(s.numtostr(ins))

