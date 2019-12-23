#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

A, B = map(int, input().split())

# R = 1
# while ((A - 1) * (R - 1)) + A < B:
#     R += 1

print(math.ceil((B - 1.0) / (A - 1.0)))
