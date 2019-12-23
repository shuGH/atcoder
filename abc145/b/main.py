#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N = int(input())
S = list(str(input()))

if N % 2 == 1:
    print("No")
    sys.exit()

m = int(N / 2)
for i in range(m):
    if S[i] != S[m + i]:
        print("No")
        sys.exit()

print("Yes")
