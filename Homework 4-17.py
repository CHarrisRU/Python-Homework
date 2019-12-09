# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:43:42 2019

@author: carte
"""
#%%
from random import *
from time import *

myList = sample(range(10000),5000)

print(myList)

with open('RandomNumberFile2.txt', 'w') as f:
    for item in myList:
        f.write("%s\n" % item)
#%%
        
def readList(l):

    with open('RandomNumberFile2.txt', 'r') as infile:
        for line in infile:
            i = int(line.strip('\n'))
            l.append(i)
            
        
        
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] < pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] > pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark]= \
                         alist[rightmark],alist[leftmark]

    alist[first],alist[rightmark]= \
                   alist[rightmark],alist[first]

    return rightmark



def writeFile(sl,fname):
    with open(fname,'w') as f:
        for item in sl:
            f.write("%s\n" % item)   
list_1 = []
readList(list_1)
print(list_1)
startTime = time()
quickSort(list_1)
stopTime = time()
print(list_1)
print(stopTime - startTime)

writeFile(list_1,"quick_sort.txt") 
#Worst case is O(n^2), average is O(n log n).       
#runs in 0.012 seconds on my pc.  
#%%
            
def readList(l):

    with open('RandomNumberFile2.txt', 'r') as infile:
        for line in infile:
            i = int(line.strip('\n'))
            l.append(i)



def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and \
                alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap] 
            position = position-gap

        alist[position]=currentvalue
            


def writeFile(sl,fname):
    with open(fname,'w') as f:
        for item in sl:
            f.write("%s\n" % item)    
            
list_2 = []
readList(list_2)
print(list_2)
startTime = time()
shellSort(list_2)
stopTime = time()
print(list_2)
print(stopTime - startTime)

writeFile(list_2,"shell_sort.txt")      
#Speed is somewhere between O(n) and O(n^2). Faster than the insertion sort on which it is based.   
#runs in 0.022 seconds on my pc.         
#%%
            
def readList(l):

    with open('RandomNumberFile2.txt', 'r') as infile:
        for line in infile:
            i = int(line.strip('\n'))
            l.append(i)
            
            
            
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax],alist[fillslot] = \
                   alist[fillslot],alist[positionOfMax]            



def writeFile(sl,fname):
    with open(fname,'w') as f:
        for item in sl:
            f.write("%s\n" % item)        
            

list_3 = []
readList(list_3)
print(list_3)
startTime = time()
selectionSort(list_3)
stopTime = time()
print(list_3)
print(stopTime - startTime)

writeFile(list_3,"selection_sort.txt")             
#O(n^2) because of the nested loops. Probably faster than the bubble sort.
#runs in 0.701 seconds on my pc.
#%%            
            









