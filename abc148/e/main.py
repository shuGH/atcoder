#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

N = int(input())

# 奇数のときは0
if N % 2 != 0:
    print(0)
    sys.exit()

# １桁のときは0
if N < 10:
    print(0)
    sys.exit()

# 扱いやすいように配列にする
d = len(str(N))
n = [int(s) for s in list(str(N))]

# 含まれる10倍数の個数だけ末尾0が増える
def check(n, c):
    if len(n) == 0:
        return 0

    # 末尾
    a = n.pop()
    # 0のときは10扱いにする
    a = 10 if a == 0 else a

    return c * a + check(n, c * 10)

n.pop()
print(check(n, 1))
