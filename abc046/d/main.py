#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = list(input())

p = 0
g = 0
w = 0
for s in S:
    # 出せるのならpを出す
    t = 'p' if p < g else 'g'
    p += 1 if t == 'p' else 0
    g += 1 if t == 'g' else 0
    # あいこでない
    if s != t:
        # 負け確
        if s == 'p':
            w -= 1
        # 勝ち確
        elif s == 'g':
            w += 1

print(w)
