#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
from collections import deque as deq

N, K = map(int, input().split())

print(K * ((K - 1)**(N - 1)))
