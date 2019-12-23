#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

R = 0
i = -100
for a in A:
    R += B[a - 1]
    R += C[a - 1] if a == i + 1 else 0
    i = a

print(R)
