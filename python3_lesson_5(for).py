#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:17:00 2018

@author: sdrttnclskn
"""

l1 = [1,2,3,4,6,78,9]
toplam = 0
for i in l1:
    toplam = toplam+i
    print(i)
    
print("toplam dizi değeri: " + str(toplam))
    
l2 = range(17)
print (l2)
for x in l2:
    print(x)

#range(baslangıc,bitis,artış deger)
for y in range(2,16,4):
    print(y)

#break,continue
    
for i in range(1,25):
    if (i%5 == 0):
        continue
    print(i)
    
for i in range(1,25):
    if (i%5 == 0):
        break
    print(i)