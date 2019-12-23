#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(str(input()))

S.sort()

print(''.join(S))
