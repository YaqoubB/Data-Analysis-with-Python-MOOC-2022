#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    iris_data = load()
    x = iris_data[:,0]
    y = iris_data[:,2]
    return np.array(scipy.stats.pearsonr(x, y))[0]

def correlations():
    x = load()
    return np.corrcoef(x, y=None, rowvar=False) 

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
