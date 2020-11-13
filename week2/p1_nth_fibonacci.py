#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:54:00 2020

@author: mls
"""

# generate the list of fibonacci numbers up to n as a list.
# Here n<45 so can just keep whole list:
def fibonacciList(n):
    fl=[0,1]
    for i in range(2,n+1):
        fl.append(fl[i-1]+fl[i-2])
    return fl[-1]

n=int(input())
print(fibonacciList(n))
