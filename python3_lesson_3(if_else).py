#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:31:18 2018

@author: sdrttnclskn
"""

x = int(input("bir sayi giriniz: "))
print(x)
if x<20:
    print("küçük")
    x = 25
elif x>25:
    print("büyük")
    
else: 
   print("ortda")
   
print("x'in yeni değeri:" +str(x))