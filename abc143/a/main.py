#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A, B = map(int, input().split())

print(max(A - 2 * B, 0))
