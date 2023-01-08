#!/usr/bin/env python3

import pandas as pd

def top_bands():
    data1 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    data2 = pd.read_csv('src/bands.tsv', sep='\t')
    data1['Artist'] = data1['Artist'].str.lower()
    data2['Band'] = data2['Band'].str.lower()
    dat = pd.merge(data1, data2, left_on='Artist', right_on='Band', how='inner')
    return dat

def main():
    return print(top_bands())

if __name__ == "__main__":
    main()
