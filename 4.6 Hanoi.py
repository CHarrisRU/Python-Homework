# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:41:38 2019

@author: carte
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



            
            
#Recursive version:
        
def printMove(fr,to):
	print('move from ', fr, ' to ', to)

def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1,fr, spare, to)
        Towers(1,fr, to, spare)
        Towers(n-1,spare, to, fr)
    
#%%

Towers(3,'A','B','Spare')  
Towers(4,'A','B','Spare')          