#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
S, T = map(str, input().split())
S = list(S)
T = list(T)

R = ''
for i in range(N):
    R += S[i] + T[i]

print(R)
