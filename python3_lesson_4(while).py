#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:47:08 2018

@author: sdrttnclskn
"""

i = 1
while i<13:
    print(i)
    i = i+1    
print("bitti")


# 1,1,2,3,5,8,13,21
# a,b
#     c
#   a,b
#fibonacci serisi

a,b = 1,1
while a<22:
    print(a)
    c = a+b
    a = b
    b = c
    
print("fibonacci dizisinin sonu ")

a,b = 1,1
while  a<22:
    print(a)
    a,b = b,a+b
print("dizi sonu")