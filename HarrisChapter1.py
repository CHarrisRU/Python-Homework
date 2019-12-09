# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:00:17 2019

@author: carte
"""

# Question 1
class Fraction1:
    
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def show(self):
        print(str(self.num) + '/' + str(self.den))
    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

my_f1 = Fraction1(6,2)

my_f1.getNum()

my_f1.getDen()

my_f1.show()

print(my_f1)




#%%

#Question 2   
def gcd(int1, int2):
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)
    
print(gcd(6,8))
 

class Fraction2:
    
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den    



#%%
#Question 3

class Fraction3:
    
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den    
    
    def __add__(self, other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return(Fraction3(newnum // common, newden // common))
    
    def __sub__(self, other):
        nn = self.num*other.den - self.den*other.num
        nd = self.den * other.den
        com_den = gcd(nn,nd)
        return Fraction3(nn // com_den, nd // com_den)
        
        
    def __mul__(self, other):
        nn = self.num * other.num
        nd = self.den * other.den
        com_den = gcd(nn, nd)
        return Fraction3(nn // com_den, nd // com_den)
        
    def __truediv__(self, other):
        nn = self.num * other.den
        nd = self.den * other.num
        com_den = gcd(nn, nd)
        return Fraction3(nn // com_den, nd // com_den)

my_f = Fraction3(2,3)
my_f2 = Fraction3(1,4)

print(my_f + my_f2)
print(my_f - my_f2)
print(my_f / my_f2)
#%% 
#Question 4

class Fraction4:
    
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den    
    
    def __gt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 > num2
        
    def __ge__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 >= num2
        
    def __lt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num2 > num1
        
    def __le__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num 
        return num2 >= num1
        
    def __ne__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 != num2
        
my_f = Fraction4(2,3)
my_f2 = Fraction4(1,4)  

print(my_f > my_f2)
print(my_f >= my_f2)
print(my_f < my_f2)
print(my_f <= my_f2)
print(my_f != my_f2)
#%%        
#Question 5
        
    
class Fraction5:
    def __init__(self, numerator, denominator):
        if isinstance(numerator, int):
            self.num = numerator
        else:
            print("Incorrect numerator data type.")
        if isinstance(denominator, int):
            self.den = denominator
        else:
            print("Incorrect denominator data type.")
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den   
my_n = Fraction5(3,6.1)    
    
#%%

#Summary

def gcd(int1, int2):
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)
    
class Fraction:
    
    def __init__(self, numerator, denominator):
        if isinstance(numerator, int):
            self.num = numerator
        else:
            print("Incorrect numerator data type.")
        if isinstance(denominator, int):
            self.den = denominator
        else:
            print("Incorrect denominator data type.")
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def show(self):
        print(str(self.num) + '/' + str(self.den))

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den   
    
    def __add__(self, other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return(Fraction(newnum // common, newden // common))
    
    def __sub__(self, other):
        nn = self.num*other.den - self.den*other.num
        nd = self.den * other.den
        com_den = gcd(nn,nd)
        return Fraction(nn // com_den, nd // com_den)
               
    def __mul__(self, other):
        nn = self.num * other.num
        nd = self.den * other.den
        com_den = gcd(nn, nd)
        return Fraction(nn // com_den, nd // com_den)
        
    def __truediv__(self, other):
        nn = self.num * other.den
        nd = self.den * other.num
        com_den = gcd(nn, nd)
        return Fraction(nn // com_den, nd // com_den)
    
    def __gt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 > num2
        
    def __ge__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 >= num2
        
    def __lt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num2 > num1
        
    def __le__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num 
        return num2 >= num1
        
    def __ne__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 != num2

#%%    
my_f = Fraction(5,2)

my_f.getNum()

my_f.getDen()

my_f.show()

print(my_f)    
    
print(gcd(6,8))    
    
my_f2 = Fraction(1,4)

print(my_f + my_f2)

print(my_f - my_f2)

print(my_f / my_f2) 
    
print(my_f > my_f2)

print(my_f >= my_f2)

print(my_f < my_f2)

print(my_f <= my_f2)

print(my_f != my_f2)    
    
#%%    
    
#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')    
    
        