#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    ind, val = s.index, s.values
    res = np.repeat(val.reshape(val.shape[0],1), k, axis=1)
    res = np.power(res, np.arange(1,k+1))
    return pd.DataFrame(res, index=ind, columns=np.arange(1,k+1))

def main():
    s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
    powers_of_series(s, 3)
    
if __name__ == "__main__":
    main()

