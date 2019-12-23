#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

R = 0
for i in range(N):
    R += X if i < K else Y

print(R)
