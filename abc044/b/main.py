#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

W = list(input())

for i in W:
    if W.count(i) % 2 == 1:
        print('No')
        sys.exit()
    W = [j for j in W if j != i]

print('Yes')
