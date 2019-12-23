#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append({'X':x, 'Y':y})

ma = 0
for i in range(len(P)):
    p1 = P[i]
    for j in range(i + 1, len(P)):
        p2 = P[j]
        d = (((p1['X'] - p2['X'])** 2) + ((p1['Y'] - p2['Y'])** 2))** 0.5
        ma = d if d > ma else ma

print(ma)
