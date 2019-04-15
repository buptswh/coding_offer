# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:29:22 2019

@author: swh
"""
'''两个栈完成一个队列
队列先进先出，栈后进先出'''

class Queue:
    def __init__(self):
        self.stockA=[]
        self.stockB=[]
    def push(self, node):
        self.stockA.append(node)
    def pop(self):
        if self.stockB==[]:
            if self.stockA==[]:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()
    
if __name__=="__main__":
    s=Queue()
    while True:
        a=input()
        if a !="":
            s.push(int(a))
        else:
            print(s.pop())