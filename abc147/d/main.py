#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

N = int(input())
A = np.array(map(int, input().split()))

s = 0
b = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 + 7
m = []
for i in range(1 - 1, N - 1):
    for j in range(i + 1 - 1, N + 1 - 1):
        s += A[i] ^ A[j]
        s = s % b

print(s)
