#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = list(input())

R = ''
for i in S:
    if i == 'B':
        R = R[:-1]
    else:
        R = R + i

print(R)
