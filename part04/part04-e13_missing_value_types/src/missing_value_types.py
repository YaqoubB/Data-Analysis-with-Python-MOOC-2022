#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    dat = [[np.nan, None], [1917, 'Niinistö'], [1776, 'Trump'], [1523, None], [np.nan, 'Steinmeier'], [1992, 'Putin']]
    state = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    return pd.DataFrame(data=dat, columns=['Year of independence', 'President'], index=state)
               
def main():
    return

if __name__ == "__main__":
    main()
