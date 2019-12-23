#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

R = 0
for i in range(N):
    R += 1.0 / A[i]

print(1.0 / R)
