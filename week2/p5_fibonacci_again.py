#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:54:00 2020

@author: mls
"""

# \ at end of line is line continuation!

import sys

def check_boundary(x,min,max):
    if not min<=x<=max:
        sys.exit("Input out of range (range is",min,"to",max)
        
       
'''
I want a definition for the pisano period for m. Notice the sequence of prime 
mod m is sum of two previous mod m -- always true by defn, for next prime 
summing the two previous primes with the two previous remainders.
Know it always starts with 01, does it only ever contain 01 at the start? 
Yes, because then the next remainder is sum 0+1 as the beginning and the 
summing will loop, i.e. 01 tells me I've come back around.
'''
def pisanoPeriod(m):
    #ps="01"
    prev,curr=1,1
    pisanolength=2
    while prev+curr>1:
        #ps+=str(curr)
        prev,curr=curr,(curr+prev)%m
        pisanolength+=1
        #print(ps)
    return pisanolength

# this is using naive but we will make itty bitty primes
def fibonacci(n):
    prev,curr=0,1
    if n<=1: return n
    # they use this odd syntax I didnt know (_)
    for _ in range(2,n+1):
        prev,curr=curr,prev+curr
    return curr

n,m=input().split()
n,m=int(n),int(m)
check_boundary(n, 1, 100000000000000)
#check_boundary(m,2,1000)
fnmodm=(fibonacci(n%pisanoPeriod(m))%m)

print(fnmodm)
