# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:40:54 2019

@author: carte
"""


def Reversal (lst):
     list_Len = len(lst)
     if list_Len == 1:
        return lst
     return [lst[-1]] + Reversal(lst[:-1])

list_words = ["hi", "there", 7]

print(Reversal(list_words))


    
    












