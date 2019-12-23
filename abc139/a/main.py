#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = list(input())
T = list(input())

print(len([1 for i in range(3) if S[i] == T[i]]))
