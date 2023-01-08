#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    data = pd.read_csv("src/data.tsv", sep="\t")
    model = PCA()
    model.fit(data)
    v = data.var()
    ev = model.explained_variance_
    plt.plot(np.arange(1,len(ev)+1), np.cumsum(ev))
    plt.show()
    return v, ev

def main():
    v, ev = explained_variance()
    print(f'The variances are: ',end=' ')
    for i in range(len(v)):
        print(f'{v[i]:.3f}',end=' ')
    print()
    print(f'The explained variances after PCA are: ',end=' ')
    for i in range(len(ev)):
        print(f'{ev[i]:.3f}',end=' ')
    print()
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
