#!/usr/bin/env python3

import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    r,c = data.shape
    col = data.columns
    print(f'Shape: {r},{c}')
    print('Columns:')
    print (*col, sep='\n')
    return 


if __name__ == "__main__":
    main()


