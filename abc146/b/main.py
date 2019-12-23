#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
S = list(str(input()))

r = ''
for i in range(len(S)):
    r += chr(ord('A') + (((ord(S[i]) + N) - ord('A')) % 26))

print(r)
