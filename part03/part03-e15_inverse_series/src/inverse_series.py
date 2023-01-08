#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(data=s.index, index=s.values)

def main():
    a=pd.Series([1, 2, 2], index=["c", "c", "c"])
    print(a)
    print(inverse_series(a))
    return

if __name__ == "__main__":
    main()

