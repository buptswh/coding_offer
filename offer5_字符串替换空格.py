# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self,s):
        # write code here
        space=0
        for i in range(len(s)):
            if s[i]==' ':
                space+=1
        ans=['0']*(len(s)+2*space)
        i,j=len(s)-1,len(ans)-1
        while i>=0 and j>=0:
            if s[i]==' ':
                ans[j]='%'
                ans[j-1]='0'
                ans[j-2]='2'
                j=j-3
                i=i-1
            else:
                ans[j]=s[i]
                i-=1
                j-=1
        res=''
        for i in ans:
            res+=i
        return res
if __name__=="__main__":
    a=input()
    if not a:
        print('')
    else:
        s=Solution()
        res=s.replaceSpace(a)
        print(res)