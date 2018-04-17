#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X = np.random.lognormal(10**6)
Y = X ** 2

print(np.sum(Y)/10**6)

sns.distplot(X)
plt.show()
