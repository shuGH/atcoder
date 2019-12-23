#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
M = []
for i in range(N):
    A = int(input())
    XY = []
    for j in range(A):
        X, Y = map(int, input().split())
        XY.append([X, Y])
    M.append(XY)

# 残り嘘つき人数を渡して全パターンを列挙する
def check(n, l):
    # 残り0なら以降を全部正直者にして判定
    if n == 0:
        l += [1] * (N - len(l))
        return judge(l)
    # 残りと未確定人数が同じなら全部嘘つきにして判定
    if n == N - len(l):
        l += [0] * (N - len(l))
        return judge(l)

    # iが正直者1
    if check(n, l + [1]):
        return True
    # iが嘘つき0
    if check(n - 1, l + [0]):
        return True

    return False

# 矛盾がないかチェックする
def judge(l):
    for i in range(len(M)):
        # 嘘つきなら無視する
        if l[i] == 0:
            continue
        # 正しいかチェック
        ii = M[i]
        for j in range(len(ii)):
            jj = ii[j]
            if l[jj[0] - 1] != jj[1]:
                return False
    return True

# 嘘つき人数を増やしながら調べる
for i in range(N + 1):
    if check(i, []):
        print(N - i)
        break;
