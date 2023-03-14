#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:20:56 2023

@author: user
"""

n = int(input())

data = [tuple(input().split()) for _ in range(n)]
ant = []
for i in range(n):
    print(*data[i])
    if '5' in data[i] or '4' in data[i]:
        ant.append(data[i])
        
print()

for i in range(len(ant)):
    print(*ant[i])
