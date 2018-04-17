#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import numpy as np
import scipy as sp
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool

y = np.array([4, 3, 4, 5, 5, 2, 3, 1, 4, 0, 1, 5, 5, 6, 5, 4, 4, 5, 3, 4])
N_comb_y = sp.misc.comb(8, y)

def likelihood(q):
    return np.prod(N_comb_y * (q ** y) * ((1-q) ** (8-y)))

def update(old_param, old_value, step):
    candidate = old_param + step * np.random.choice([-1, 1])
    new_value = likelihood(candidate)

    if new_value > old_value:
        new_param = candidate
    else:
        prob      = new_value / old_value
        new_param = np.random.choice([candidate, old_param], p=[prob, 1.0-prob])

    return new_param, new_value

def iter_func(idx):
    np.random.seed(idx)
    step       = 0.001
    init_param = step * np.random.randint(1, 1/step)
    max_iter   = 10**6
    history = []

    param = init_param
    value = likelihood(init_param)
    history.append(param)
    for i in range(1, max_iter):
        param, value = update(param, value, step)
        history.append(param)

    print("Iteration {} finished ... ".format(idx))
    return history[10**4:10**6]

def main():
    with Pool(24) as mp:
        history = mp.map(iter_func, range(24))
        samples = np.array(history).flatten()

    # plt.hist(samples, bins=50)
    sns.distplot(samples, norm_hist=True)
    plt.savefig("hoge.pdf")

if __name__ == "__main__": main()
    means = []
    for i in range(10):
        start = time.perf_counter()
        main()
        end = time.perf_counter()
        print(f"elapsed time: {end-start} [s]")
        means.append(end-start)
    print(f"mean: {np.mean(means)} [s]")
