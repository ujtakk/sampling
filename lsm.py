#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def least_square(x, t):
    assert(len(t) == len(x))

    N = len(x)
    alpha = (N * np.dot(x, t) - np.sum(x) * np.sum(t)) \
          / (N * np.sum(x**2) - np.sum(x)**2)
    beta  = (np.sum(t) * np.sum(x**2) - np.sum(x) * np.dot(x, t)) \
          / (N * np.sum(x**2) - np.sum(x)**2)
    print((alpha, beta))

    y = alpha * x + beta
    return y

x = np.arange(0, 10, 0.1)
t = x + np.random.randn(100)
y = least_square(x, t)

sns.set_style("whitegrid")
plt.scatter(x, t, s=16)
plt.plot(x, y, c="k")
plt.show()
