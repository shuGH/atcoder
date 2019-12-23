#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
D = list(map(int, input().split()))

R = 0
for i in range(N):
    for j in range(i + 1, N):
        R += D[i] * D[j]

print(R)
