# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:40:21 2019

@author: carte
"""

def factorial(n):
   if isinstance(n, int) != True:
       print("Only integers are allowed.") 
   elif n <1 and n >= 0:   
       return 1
   elif n < 0:
       return ValueError("You can't have a factorial of a negative number")
   else:
       returnNumber = n * factorial( n - 1 )  
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

factorial(6)



