#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

mx = max(A)
mn = min(A)

R = -1
for i in range(mn, mx + 1):
    s = 0
    for a in A:
        s += (i - a)** 2
    R = s if R < 0 or s < R else R

print(R)

