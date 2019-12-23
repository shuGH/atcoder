#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = list(map(int, input().split()))

R = 0
while len(A) > 0:
    A = [a for a in A if a != A[0]]
    R += 1

print(R)
