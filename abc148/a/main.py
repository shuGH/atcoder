#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = int(input())
B = int(input())

print([i for i in [1, 2, 3] if (i != A and i != B)][0])

