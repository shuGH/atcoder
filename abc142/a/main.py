#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())

odd = N / 2 if N % 2 == 0 else ((N - 1) / 2) + 1

print(odd / N)
