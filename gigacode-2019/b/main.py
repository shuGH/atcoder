#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, X, Y, Z = map(int, input().split())
M=0
for i in range(N):
    A, B = map(int, input().split())
    M += 1 if (A >= X and B >= Y and A + B >= Z) else 0

print(M)
