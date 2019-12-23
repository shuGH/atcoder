#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque as deq

A = deq(list(input()))
B = deq(list(input()))
C = deq(list(input()))

S = {
    'a': A,
    'b': B,
    'c': C
}

def check(s):
    if len(S[s]) == 0:
        return s.upper()
    else:
        return check(S[s].popleft())

print(check('a'))
