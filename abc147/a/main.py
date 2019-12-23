#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A1, A2, A3 = map(int, input().split())

print("bust" if A1 + A2 + A3 >= 22 else "win")
