#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

# 1から順番に並べられたらOK
a = 1
c = 0
for i in range(N):
    if A[i] == a:
        # 確定した扱い
        a += 1
    else:
        # 取り除いた扱い
        c += 1

print(c if a > 1 else -1)
