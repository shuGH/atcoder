#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, K = map(int, input().split())
D = list(map(int, input().split()))

# 嫌いじゃないソート済み数字
D = [i for i in range(10) if D.count(i) == 0]

print(D)

def dfs(n):
    if n == 0:
        return - 1


    for i in D:
        r = -1
        for j in D:
            ss = s + str(j)
            if N < int(ss):
                r = int(ss)
                break
        if r > 0:
            return r
    return dfs(str(D[0]) + s)

def digit(n):
    r = dfs(n)
    if r > 0:
        return r
    else:
        return digit(n + 1)

print(digit(0))
