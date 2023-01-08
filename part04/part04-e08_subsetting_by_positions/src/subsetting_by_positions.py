#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    return pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t').iloc[0:10, 2:4]

def main():
    return print(subsetting_by_positions())

if __name__ == "__main__":
    main()
