# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:15:53 2019

@author: swh
"""

'''
n个骰子的点数
把n个骰子仍在地上，朝上一面的点数之和为s，输入n,打印出s所有可能的值的出现的概率
思路：用两个数组存储骰子点数的每个总数出现的次数
n为可能出现的点数，f(n)是该点数出现的次数
所以f(n)=f(n-1)+f(n-2)+f(n-3)+f(n-4)+f(n-5)+f(n-6)
'''
gmax=6#一个骰子有的最大值
def probability(n):
    if n<1:
        return 
    pro=[0]*2
    pro[0]=[]
    pro[1]=[]
    pro[0]=[0]*(gmax*n+1)
    pro[1]=[0]*(gmax*n+1)
    flag=0
    for i in range(1,gmax+1):#1~6位置(就是最后的值)，一个骰子出现的次数，1~6都可能出现一次
        pro[flag][i]=1
    for k in range(2,n+1):#开始加骰子，一直到 n个骰子
        for i in range(k):
            pro[1-flag][i]=0#把前从第k个骰子之前的标志位清空（为了更新）
        for i in range(k,gmax*k+1):
            pro[1-flag][i]=0#先把该位置清0，然后计算f(n)
            for j in range(1,min(i,gmax)+1):#如果i<=6的情况，就是i值了
                pro[1-flag][i]+=pro[flag][i-j]
        flag=1-flag#轮换一次
    total=gmax**n#一共会出现的情况总量
    for i in range(n,gmax*n+1):
        ratio=pro[flag][i]/total#打印概率，最小是n,最大是gmax*n
        print(i,ratio)
    
if __name__=="__main__":
    x=input()
    if x !='':
        k=int(x)
        probability(k)
    else:
        print('输入不规范')    