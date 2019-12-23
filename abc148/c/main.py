#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A, B = map(int, input().split())

aa = A
bb = B
while aa != bb:
    if aa < bb:
        aa += A
    else:
        bb += B

print(aa)
