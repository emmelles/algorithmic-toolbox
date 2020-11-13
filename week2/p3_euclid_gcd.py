# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

def checkBoundaries(x,y):
    if not 0<x<10000001 or not 0<y<10000001 :
        sys.exit("Entries out of range (range is 1 to 10^7)")
        

def euclidGCD(n,m):
    if m==0:
        return n
    q=n%m
    return euclidGCD(m,q)


a,b=input("Enter two numbers:").split()
a,b=int(a),int(b)
checkBoundaries(a,b)
gcd=euclidGCD(int(a),int(b))
print("gcd:",gcd)

