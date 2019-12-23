#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

S = list(str(input()))

r = 0
for i in range(math.floor(len(S) / 2.0)):
    if (S[i] != S[len(S) - (i + 1)]):
        r += 1

print(r)
