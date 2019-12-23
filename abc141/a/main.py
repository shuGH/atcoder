#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = str(input())
W = ['Sunny', 'Cloudy', 'Rainy']

print(W[(W.index(S) + 1) % len(W)])
