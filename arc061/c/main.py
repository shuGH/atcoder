#!/usr/bin/env python3
# -*- coding: utf-8 -*-

S = list(str(input()))

# 列挙して加算
def dfs(i, s):
    # 最後までいったから返す
    if i + 1 >= len(S):
        return s + int(s)
    # +を入れる
    s += dfs(i + 1, int(n), S[i + 1])
    # +を入れない
    s += dfs(i + 1, 0, n + S[i + 1])
    # 合計を返す
    return s

print(dfs(0, S[0]))
