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

# we know n*m is def a common multiple, but also gcd divides both numbers so
# can divide this multiple
def leastCommonMult(n,m):
    return int((n*m)/euclidGCD(n, m))

a,b=input("Enter two numbers:").split()
a,b=int(a),int(b)

checkBoundaries(a, b)

gcd=euclidGCD(a,b)
lcm=leastCommonMult(a,b)
print("gcd:",gcd)
print("lcm:",lcm)
