#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns

num = 10**7
upper = 6
for k in range(1, upper):
    X = np.random.randn(k, num)
    Z = np.sum(X**2, axis=0)
    plt.hist(
        Z,
        histtype="step",
        bins=10000,
        normed=True,
        lw=1.5,
        label="Num: {}".format(k)
    )

plt.xlim(0.0, 20.0)
plt.ylim(0.0, 1.0)
plt.legend()
plt.show()
