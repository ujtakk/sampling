#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# two uniform distributions
X = np.random.rand(10**6)
Y = np.random.rand(10**6)

# generating two gaussian distributions
Z1 = np.sqrt(-2 * np.log(X)) * np.cos(2*np.pi*Y)
Z2 = np.sqrt(-2 * np.log(X)) * np.sin(2*np.pi*Y)

mean = np.sum(Z1) / 10**6
var = np.sum(Z1**2) / 10**6 - mean**2
print({"mean": mean, "var": var})

sns.distplot(Z2)
plt.show()
