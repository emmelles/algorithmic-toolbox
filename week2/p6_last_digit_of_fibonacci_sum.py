#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:19:12 2020

@author: mls
"""
def check_boundary(x,min,max):
    if not min<=x<=max:
        sys.exit("Input out of range (range is",min,"to",max)

##############################################
# this works perfectly well but I think they want me to do something else
# def fibonacciLastList(n):
#     # maybe not table is best? 
#     ls=[0,1]
#     current, previous= ls[1],ls[0]
#     for i in range(2,n+1):
#         current, previous=(current+previous)%10,current
#         ls.append(current)
#     return ls

# print(sum(fibonacciLastList(100)))
# print(sum(fibonacciLastList(100))%10)
##############################################

# looking at table of fibonacci nos and sums of, see a pattern
# sum_i^n F_n = F_(n+2) -1


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


def sumFibonacci(n):
    return fibonacci(n+2)-1

n=input()
n=int(n)
check_boundary(n, 1, 10000)

sumfb=sumFibonacci(n%pisanoPeriod(10))%10
print(sumfb)


