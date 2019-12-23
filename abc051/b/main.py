#!/usr/bin/env python3
# -*- coding: utf-8 -*-

K, S = map(int, input().split())

r = 0
for i in range(K + 1):
    for j in range(K + 1):
        k = S - i - j
        if k >= 0 and k <= K:
            r += 1

print(r)
