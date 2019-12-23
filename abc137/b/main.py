#!/usr/bin/env python3
# -*- coding: utf-8 -*-

K, X = map(int, input().split())

print(*[i for i in range(X - K + 1, X + K) if (i > -1000000 and i < 1000000)])
