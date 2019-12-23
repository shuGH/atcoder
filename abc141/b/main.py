#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = list(str(input()))
O = ['R', 'U', 'D']
E = ['L', 'U', 'D']

for i in range(len(S)):
    if (i + 1) % 2 != 0:
        if O.count(S[i]) == 0:
            print('No')
            break
    else:
        if E.count(S[i]) == 0:
            print('No')
            break
else:
    print('Yes')
