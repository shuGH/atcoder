#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A, B = map(int, input().split())

print("Even" if ((A * B) % 2 == 0) else "Odd")
