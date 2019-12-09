# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:41:15 2019

@author: carte
"""    

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 8

if isinstance(nterms, int) != True:
    print("Only positive integers are allowed.")
elif nterms <= 0:
    print("Please enter a positive integer")
else:
    for i in range(nterms):
        print(recur_fibo(i))    

#It is significantly slower, as the recursive version is O(2^n) compared to O(n) for the iterative version.   

    



    
    
    
