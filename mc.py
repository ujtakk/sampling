#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(
    rc = {
        "figure.figsize": (10, 6)
    }
)

def random_walk(x):
    y = []
    v = 0
    for i in x:
        y.append(v)
        if v == 100 and i == -1:  v += i
        elif v == 0 and i == 1:   v += i
        elif 0 < v and v < 100:   v += i
    return np.array(y)

y_ = []
# for n in range(10**4):
x = np.random.choice([-1, 1], 10**8)
y = random_walk(x)
# y_.append(y)
# plt.plot(y, lw=1)

sns.distplot(y, label="Walked")
# normal = lambda mean, var: np.sqrt(var) * np.random.randn(10**3) + mean
# sns.distplot(normal(np.mean(y_), np.var(y_)), label="Normal")
# plt.legend()
plt.show()
