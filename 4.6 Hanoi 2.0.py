# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:23:49 2019

@author: Carter Harris
"""
class Stack():
    def __init__(self, name):
        self.name = name
        self._container = []
        
    def push(self, item):
        self._container.append(item)
        
    def pop(self):
        return self._container.pop()
    
    def __repr__(self):
        return self.name
    
def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
        printMove(begin,end)
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)
        
def printMove(begin,end):
	print(f'Move from {begin} to {end}')
        
if __name__ == "__main__":
    tower_a = Stack("Tower A")
    tower_b = Stack("Spare Tower")
    tower_c = Stack("Tower B")
    num_discs = 4
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    print(tower_a._container)
    print(tower_b._container)
    print(tower_c._container)
    print("Run Hanoi...")
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a._container)
    print(tower_b._container)
    print(tower_c._container)


