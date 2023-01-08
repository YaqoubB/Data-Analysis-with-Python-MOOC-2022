#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    data = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    dat1 = pd.to_numeric(data['LW'], errors='coerce')
    dat1 = dat1.fillna(len(data))
    return data[dat1 < data['Pos']]

def main():
    return print(special_missing_values())

if __name__ == "__main__":
    main()

    