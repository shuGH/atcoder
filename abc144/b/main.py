#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

N = int(input())

for i in range(1, 10):
    if N % i != 0:
        continue
    if N / i < 10:
        print('Yes')
        sys.exit()

print('No')
