#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N, Y = map(int, input().split())

# 千
for i in reversed(range(N + 1)):
    # 万
    for j in reversed(range(N + 1 - i)):
        # 5千
        k = ((Y / 1000) - (i + 10 * j)) / 5
        if k % 1 != 0.0:
            continue
        if k >= 0 and k <= N - (i + j):
            print("{} {} {}".format(j, int(k), i))
            sys.exit()

print("{} {} {}".format(-1, -1, -1))
