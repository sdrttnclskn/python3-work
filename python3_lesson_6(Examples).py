#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:39:51 2018

@author: sdrttnclskn
"""

# 1 den 100 kadar olan asal sayıları

asalList = []
for i in range(1,100): 
    for b in range(2,i):
        if (i%b == 0):
            break
    else:
         asalList.append(i)
print(asalList)
      
#############################
asalList2 = []
for x in range(1,100):
    flag = 0;
    for y in range(2,x):
        if(x%y == 0):
            flag =1
            break
    if(flag != 1):
          asalList2.append(x)
print(asalList2)
        
    
        
