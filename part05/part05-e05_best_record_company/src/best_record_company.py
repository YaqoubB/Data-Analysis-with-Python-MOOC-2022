#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    data = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    dat = data.groupby('Publisher')
    pub = dat['WoC'].sum().idxmax()
    res = dat.get_group(pub)
    return res

def main():
    return print(best_record_company())
    

if __name__ == "__main__":
    main()
