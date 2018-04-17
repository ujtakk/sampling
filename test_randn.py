#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normal = lambda mu=0, sigma=1: \
         lambda num: \
             sigma * np.random.randn(num) + mu

num = 10**6
X = normal(0, 3)(num)

mean = np.sum(X) / num
var1 = np.sum((X - mean) ** 2) / num
var2 = np.sum(X**2)/num - mean**2

print("mean: {}, var1: {}, var2: {}".format(mean, var1, var2))

iter_count = 20000
answer = np.zeros(iter_count)
for n in range(iter_count):
    filtered = np.where(X < -100 + n/100, 1, 0)
    answer[n] = np.sum(filtered)/num

plt.plot(np.arange(-100, 100, 0.01), answer)
plt.show()

