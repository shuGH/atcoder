#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A, B = map(int, input().split())

print(max(A + B, A - B, A * B))

