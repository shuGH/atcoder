#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = list(map(int, input().split()))

print('YES' if (A.count(5) == 2 and A.count(7) == 1) else 'NO')
