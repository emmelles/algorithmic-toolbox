#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:54:00 2020

@author: mls
"""

# just keeping the two I need
def fibonacci(n):
    # maybe not table is best? 
    fl=[0,1]
    i=1
    while i<n:
        fl.append((fl[0]+fl[1])%10)
        del fl[0]        
        i+=1
    return fl[-1]

n=int(input())
if 0<=n<=10000000:
    lastdg=fibonacci(n)%10
    print(lastdg)
else:
    print("Number too large or small (must be 0<=n<=10^7)")
